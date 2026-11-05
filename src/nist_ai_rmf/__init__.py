"""nist-ai-rmf.

NIST AI RMF family: NIST AI 100-1 and NIST AI 600-1 as one schema (LinkML)
"""

try:
    from nist_ai_rmf._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
