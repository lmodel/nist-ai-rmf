# About nist-ai-rmf

This page says why the repository exists, what it adds to the two it copies, and what it leaves out.

## Why it exists

A knowledge bundle that names both the AI RMF's and the Profile's classes needs one domain schema. The adapt copies of lmodel/nist-ai-100-1 and lmodel/nist-ai-600-1 share elements, since the second vendors two modules of the first. They validate side by side, but `lokf convert` stops with `Conflicting URIs`. This repository's copy holds each shared element once.

## What it adds

- **`NistAiRmfFamily`**, one class that holds both publications. It gives the JSON Schema a top level, because each publication's root stays a root.
- **Proof that the two hold together.** `tests/test_catalogue.py` validates both whole catalogues under one schema, holds every element to its publication's IRI, and checks that the Profile names only subcategories the framework holds.
- **A builder for the ISO/IEC 42001 crosswalk.** `scripts/build_crosswalk.py` reads the crosswalk that Microsoft provided and NIST's AI Resource Center lists, and writes it as SSSOM under `tmp/`.

## The crosswalk

The document names no relation between its two columns, and NIST's listing says inclusion implies no endorsement, so each row is a `skos:relatedMatch`. It was written against ISO/IEC FDIS 42001 and nothing here compares it with the published text. It cites Annex B's guidance, so a row names the Annex A control of the same number and its comment gives the number as printed.

Three rows print a number with a heading the document gives that number nowhere else. Each row keeps the number and says so in its comment, and the constants at the top of the script list them. This project does not settle whether the author meant the number or the heading.

The document states no licence, so the repository carries neither it nor its pairs. The set exists only on the machine that runs `just build-crosswalk`.

## What it leaves out

- **A model of its own.** A change to a class belongs in its repository, and the release carries it here.
- **The earlier third-party fixtures.** A script turned a snapshot of a governance toolkit into this schema's shape, so they tested the script and not the schema. The 11 MB snapshot went with them.
- **The earlier SSSOM set.** A matching tool wrote its rows, and many named targets that no schema holds.
- **Other crosswalks on NIST's page.** Their targets have no lmodel schema to hold their objects.
