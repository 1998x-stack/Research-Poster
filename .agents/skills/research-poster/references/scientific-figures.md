# Scientific visualization and architecture redraws

## General
Preserve *semantics* first: nodes, edges, direction, multiplicity, masking, normalization, residuals, ordering. Prefer editable vector shapes and a single illustrative code path. Label visual simplifications.

## Common CS diagram grammar
- **Neural architectures**: data-flow arrows, repeated \`×N\` blocks, attention/masks, embeddings, norm, logits.
- **Algorithms**: definition → invariant → complexity → proof sketch; complexity claims require assumptions (sequence length n, width d).
- **Systems**: topology, boundary, hot path, failure modes, throughput/latency units, percentiles.
- **Security**: threat model, attacker capabilities, trust boundary, guarantees and exclusions.
- **HCI**: participant n, task, effect size, uncertainty, accessible screenshots and informed-consent context.

## Experimental plot integrity
- Name task, test split, metric, direction, baseline and source table.
- Show actual data and axis origin; explain truncation. Use error bars only when provided.
- Do not visually imply significance from one point estimate.
- Distinguish \`single\`, \`ensemble\`, \`base\`, \`big\`, pretraining and fine-tuning budgets.
- State computational complexity with symbols and assumptions. For vanilla dense self-attention: O(n²d) time and O(n²) attention score memory for a head, not an unqualified O(n²) end-to-end model claim.

## Transformer illustration checks
Scaled dot-product attention: **softmax(QKᵀ / √dₖ) V**. Multihead: projection of Q/K/V per head, concat and output projection. Position signals enter before the stacks. Encoder has bidirectional source self-attention; decoder self-attention is causally masked; decoder cross-attends encoder representations. Residuals and LayerNorm appear around each sublayer in the original architecture; do not inadvertently depict a different model. An illustration with 4 visible heads must disclose that the base model used 8.