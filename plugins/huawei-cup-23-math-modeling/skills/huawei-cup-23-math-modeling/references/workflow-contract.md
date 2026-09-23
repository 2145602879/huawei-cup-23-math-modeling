# Workflow contract

Use a project-local output directory such as `paper_output/` and keep the following artifacts:

```text
paper_output/
  intake/                 # copied source manifest and requirement matrix
  code/                   # source, environment lock, run config
  results/                # raw outputs and machine-readable tables
  figures/                # source + rendered figures
  paper_source/           # markdown or structured source
  paper/                  # working and frozen DOCX/PDF
  qa/                     # render images, audit JSON, logs
  submission/             # immutable final PDF, MD5, manifest, archive
```

## Evidence record

For every result used in the paper, retain: source input path/hash, code entry point, command/configuration, environment versions, run timestamp, output artifact/hash, validation status, and the paper locations that cite it. Never overwrite a result without changing its hash and invalidating dependent QA.

## Minimum checkpoints

`INTAKE_READY` → `REQUIREMENTS_LOCKED` → `MODEL_REVIEWED` → `COMPUTE_VERIFIED` → `PAPER_DRAFTED` → `AI_DISCLOSURE_REVIEWED` → `PDF_QA_PASSED` → `MD5_FROZEN`.

If a later change affects an earlier artifact, move the status back to the earliest affected checkpoint. `PDF_QA_PASSED` is invalidated by any layout or content change; `MD5_FROZEN` is invalidated by any byte change to the PDF.

## Stop conditions

Stop and report rather than guessing when: the official source conflicts with the digest; the problem data is missing or corrupted; a key number cannot be reproduced; a citation cannot be verified; identity leakage is detected; the template cannot be preserved; or the submission window/filename/team number is unknown.

