# Research-paper archetypes and layout selection

Choose the poster's **argument shape from the paper's contribution**. A shared brand does not imply a shared method diagram. Layout wireframes are structural suggestions; their placeholder graphics are not claims.

## Decision process

1. Identify contribution type: theory, mechanism, system, empirical observation, user study, dataset, benchmark or intervention.
2. Find the strongest **version-verified** evidence: theorem, quantitative comparison, case analysis or replicated evaluation.
3. Pick one dominant visual that answers the reader's main question *without hiding important limitations*.
4. Select a visual wireframe from `assets/templates/` only after the story is clear; revise it to meet the venue's dimensions and the content's actual needs.
5. Write captions stating whether images are paper-derived data, author-redrawn schematics, or conceptual illustrations.

| Archetype | Dominant visual | Supporting material | Failure to avoid |
| --- | --- | --- | --- |
| ML / neural architecture | Data-flow or mechanism diagram; clear training vs inference | Data split, baseline table, ablation and compute | Architectural edges/masks missing, incompatible baseline |
| Computer vision / multimodal | Input → representation → output pipeline; representative cases | Accuracy metric, task split, failure cases | Cherry-picked examples or blurred qualitative limits |
| Systems / distributed systems | Component topology and critical path | Load/scale curves, latency percentiles, hardware/workload | Throughput without workload, unshown tail latency |
| Databases / information retrieval | Query/index architecture or execution path | Query mix, memory/storage, quality–latency trade-offs | Comparing different hardware, index freshness or recall |
| Algorithms / complexity theory | Formal problem → invariant → proof intuition or reduction | Complexity conditions, example/edge case | Claiming a bound without conditions or theorem scope |
| Security / privacy / cryptography | Trust boundary, attacker → defense path or protocol | Threat model, attack assumptions, evaluation limits | Generalizing beyond attacker model or implying absolute guarantees |
| HCI / accessibility | Research question → protocol → observed outcomes | Sample details, comparison, uncertainty and constraints | Treating qualitative study as population-wide causal proof |
| Robotics / control | Observation → estimation → policy → actuation loop | Deployment scenario, safety and success/failure rates | Omitted real-world conditions or failure recovery |
| Dataset / benchmark | Collection, labeling, splits and evaluation pipeline | Coverage, reliability, fairness, licensing | Presenting benchmark score as universal capability |
| Interdisciplinary | Domain problem → computational method → validation | Domain measurement and relevance | Missing domain-specific assumptions |

## Suggested composition modes

- **Mechanism-led hybrid:** one dominant diagram, short context, two or three meaningful empirical comparisons.
- **Results-led:** one central, correctly scaled chart and experiment summary; best for measured performance gains and trade-offs.
- **Proof-led:** central theorem (including assumptions) and a visually honest proof skeleton; empirical results may be absent.
- **Study-led:** protocol and participant context must be prominent; avoid unsupported universal conclusions.
- **Methods atlas:** two or more side-by-side techniques only when a single hero figure would distort the actual contribution.

## Cross-disciplinary review questions

- Could someone infer a **false mechanism or theorem** from this diagram?
- Is each numeric comparison drawn from comparable conditions?
- Does the poster say *when and for whom* the result holds?
- Can the reader find the primary source and exact cited experiment?
- Are figures and claims readable at physical poster scale and on a small preview?
