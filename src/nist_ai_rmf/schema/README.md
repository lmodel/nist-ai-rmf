# Schema Directory

`nist_ai_rmf.yaml` is the umbrella. The rest are lmodel/nist-ai-600-1's modules beside it and lmodel/nist-ai-100-1's under `nist_ai_100_1/`, each copied unchanged, so that 600-1's imports find 100-1's one copy.

That holds only while 600-1's own copies of the base and profiles modules are the files here. Vendor a release that changes either module together with a release of the other repository that matches it. `tests/test_schema_rules.py` fails when an element of 600-1's released copy differs from the one here.
