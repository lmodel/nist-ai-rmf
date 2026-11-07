"""Checks the upstream watch's decisions against stubbed answers, so they run offline."""

import hashlib
import importlib.util
import io
import json
import urllib.error
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "check_upstream_release.py"


@pytest.fixture
def watch():
    """A fresh copy of the script."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _answers(watch, tag=None, pdf=b"the crosswalk", awaited=None, released=True):
    """A stub of the one network call, answering as GitHub and NIST would. `tag` is the
    vendored repositories' latest release, each one's pin by default, and `released=False`
    gives them none. `awaited` is lmodel/iso42001's latest release, None for none."""
    watch.CROSSWALK_SHA256 = hashlib.sha256(b"the crosswalk").hexdigest()
    watch.AWAITED = {"lmodel/iso42001": "tests/neighbours/absent.yaml"}

    def download(url):
        if url == watch.CROSSWALK_URL:
            return pdf
        repository = url.split("/repos/")[1].rsplit("/releases/", 1)[0]
        if repository in watch.AWAITED:
            latest = awaited
        else:
            latest = (tag or watch.VENDORED_FROM[repository]) if released else None
        if latest is None:
            raise urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO())
        return json.dumps({"tag_name": latest}).encode()

    watch._download = download


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_nothing_changed(watch, tmp_path):
    """The pinned releases and bytes exit 0."""
    _answers(watch)
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "matches its pin" in text
    assert "lmodel/iso42001: no release yet" in text


def test_a_new_release_is_reported(watch, tmp_path):
    """Another tag sets attention and names what to do."""
    _answers(watch, tag="v0.2.0")
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "lmodel/nist-ai-100-1 released `v0.2.0`" in text
    assert "lmodel/nist-ai-600-1 released `v0.2.0`" in text


def test_a_vendored_repository_without_a_release_is_reported(watch, tmp_path):
    """A repository the modules come from that answers with no release sets attention."""
    _answers(watch, released=False)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "lmodel/nist-ai-100-1 has no release now" in text
    assert "None" not in text


def test_an_awaited_first_release_is_reported(watch, tmp_path):
    """lmodel/iso42001's first release sets attention and says where its asset goes."""
    _answers(watch, awaited="v0.1.0")
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "lmodel/iso42001 released `v0.1.0`" in text
    assert "tests/neighbours/absent.yaml" in text


def test_an_awaited_copy_in_place_asks_nothing(watch, tmp_path):
    """Once the copy is here, the check reads no address."""
    _answers(watch)
    watch.AWAITED = {"lmodel/iso42001": "tests/test_watch.py"}
    asked = []
    answer = watch._download
    watch._download = lambda url: asked.append(url) or answer(url)
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert not [url for url in asked if "iso42001" in url]


def test_server_text_is_one_code_span_on_one_line(watch):
    """A blank line or a backtick in a server's answer cannot end the code span."""
    assert watch._code("v1`\n\n@someone") == "`v1' @someone`"


def test_a_changed_crosswalk_is_reported(watch, tmp_path):
    """Other bytes at the crosswalk's address set attention."""
    _answers(watch, pdf=b"another crosswalk")
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "now serves other bytes" in text


def test_a_failed_download_still_writes_a_report(watch, tmp_path):
    """A check that fails is reported as unfinished, and the other still runs."""

    def fail(url):
        raise urllib.error.URLError("Connection refused")

    watch._download = fail
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert text.count("A check could not finish") == 3


def test_a_redirect_to_plain_http_is_refused(watch):
    """A file is followed only over https."""
    with pytest.raises(urllib.error.URLError):
        watch._HttpsOnly().redirect_request(
            None, None, 302, "Found", {}, "http://airc.nist.gov/docs/file.pdf"
        )


def test_a_redirect_to_another_host_is_refused(watch):
    """A file is followed only to a host the script reads from."""
    with pytest.raises(urllib.error.URLError):
        watch._HttpsOnly().redirect_request(
            None, None, 302, "Found", {}, "https://example.com/file.pdf"
        )


def test_an_address_off_the_list_is_refused(watch):
    """The first address is held to the redirect's rule."""
    with pytest.raises(urllib.error.URLError):
        watch._download("http://airc.nist.gov/docs/file.pdf")
    with pytest.raises(urllib.error.URLError):
        watch._download("https://example.com/file.pdf")
