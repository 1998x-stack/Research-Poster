# Source evidence ledger — Attention Is All You Need

Canonical source: Vaswani et al. (2017), *Attention Is All You Need*, NeurIPS 30, [official PDF](https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf).

| Claim | Exact reference | Caveat |
| --- | --- | --- |
| Transformer uses attention rather than recurrence in encoder–decoder | Sections 1 and 3 | Decoder still emits tokens autoregressively |
| 28.4 BLEU on WMT14 English→German | Table 2, Transformer (big) | Task, split, configuration are required |
| 41.0 BLEU on WMT14 English→French | Table 2, Transformer (big) | Later arXiv revisions report 41.8; version not interchangeable |
| Base uses 6 encoder, 6 decoder layers; 8 attention heads, d_model 512, d_ff 2048 | Sections 3 and 5 | 4-head illustration in SVG is a didactic schematic |
| Dense attention compares token pairs | Section 4 / discussion | Quadratic relationship does not describe every part of total model complexity |

Poster art is an educational reinterpretation of the earlier Modern Research Poster V2. Text and figures are recreated as portable vectors for browser use. The original locally generated V2 PDF and PPTX remain separate deliverables until binary rendering is connected to the repository.
