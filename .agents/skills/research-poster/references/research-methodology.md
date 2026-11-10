# Source fidelity and claim extraction

## Primary-source priority

1. Camera-ready proceedings and peer-reviewed article (venue PDF, DOI).
2. Official author-hosted version or arXiv revision with explicit version date.
3. Official code, reproducibility artifact and supplementary appendix.
4. Independent evaluation and surveys as *context*, never a replacement for the reported result.

Capture: title, complete author list, venue, year, DOI or stable official URL, paper version, task, datasets/splits, model variants, metric direction, baseline type, compute budget, and negative/limitation cases.

## Claim ledger (required for new paper)
| Claim ID | Exact wording for poster | Source URL and page/section/table | Version | Evidence grade | Caveat |
| --- | --- | --- | --- | --- | --- |
| C01 | Method replaces recurrence with self-attention | Official 2017 paper, Sections 1–3 | Proceedings | direct | decoder is still autoregressive |
| C02 | 28.4 BLEU, WMT14 EN–DE | Official 2017 paper, Table 2 | Proceedings | direct | Transformer (big) |
| C03 | 41.0 BLEU, WMT14 EN–FR | Official 2017 paper, Table 2 | Proceedings | direct | later arXiv text differs |

Keep the ledger as `evidence.md` in the poster folder, or include equivalent references in structured metadata.

## Summary workflow
Research question → prior bottleneck → precise contribution → high-level intuition → technical method → experimental conditions → measured results → limitations → lasting impact *only if sourced*.

## Version-conflict protocol
- Never combine a v1 table with a v7 abstract number without mentioning the discrepancy.
- Quote exact values only from the declared source version.
- If the authoritative table is unavailable, label uncertain numbers as pending and omit flashy metric badges.
- If a figure is conceptual, caption it “schematic / not to scale”.
- Do not treat “beat SOTA” as permanent; state the year/task and baseline.

## Plagiarism and publishing
Cite all claims/diagrams; redraw rather than screenshot figures unless the license permits. Verify that any input is public and sharable. Do not expose passwords, manuscript review comments or unpublished third-party information.