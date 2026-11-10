# Case study: Attention Is All You Need

**Primary source:** Vaswani et al., *Attention Is All You Need*, NeurIPS 2017 proceedings PDF:
https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf

## Narrative
- **Motivation:** recurrence enforces sequential dependency along token positions; convolution has a different locality/stacking tradeoff.
- **Mechanism:** scaled dot-product attention, multi-head projections, positional encoding, 6 encoder + 6 decoder layers, encoder–decoder cross-attention.
- **Experiment:** WMT 2014 machine translation; Transformer (big), BLEU. Cite **28.4** English→German and **41.0** English→French from the **2017 proceedings Table 2**.
- **Version warning:** later arXiv versions (e.g. v7) have reported 41.8 English→French. Mark the version explicitly, not interchangeable data.
- **Architecture data:** base: 6/6 layers, 8 heads, d_model=512, d_ff=2048, d_k=64, about 65M parameters.
- **Limitations:** dense full self-attention has quadratic token-pair interaction, and the original decoder remains token-autoregressive.

## Poster hierarchy
Banner: “NO RECURRENCE. ALL ATTENTION.” → left column sequential vs parallel and equation → dominant central architecture → right column quantitative evidence, model specification and limitation → full citation + QR.

The diagram is an educational redraw. A 4-head cartoon is illustrative only; label base-model 8 heads separately.