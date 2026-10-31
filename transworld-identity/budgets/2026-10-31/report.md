# Runtime budget audit — 2026-10-31

The user requested budgets for the compact core and every runtime reference, with no padding and no new tests. This audit lists a reproducible planning target, actual size and residual for all 13 files. It preserves the runtime at commit `615d7139b3a44a83a6266ed7e69beae0df263f65`.

**These are editorial planning targets, not a completed research-admission calculation.** The original size coefficients are unchanged. Missing transfer, pressure and register-discrimination measurements remain unknown. The source-supported census replaces the legacy scored-survivor input only for this explicitly scoped planning use; it does not certify those survivors. The user’s compact-entry instruction takes precedence over filling a numerical target.

## Target and actual size

Counts use Persona-Distiller’s heuristic tokenizer, including frontmatter. They are not actual model token bills. Delta = actual − target; percentage = delta / target. ±10% is a comparison signal, not a command to pad or cut.

| Runtime file | Planning target | Actual | Delta | Delta % | Disposition |
|---|---:|---:|---:|---:|---|
| `SKILL.md` | 4,500 | 2,459.73 | -2,040.27 | -45.34% | Documented exception; retain |
| `references/frameworks.md` | 7,000 | 4,506.80 | -2,493.20 | -35.62% | Documented exception; retain |
| `references/voice.md` | 4,420 | 3,180.10 | -1,239.90 | -28.05% | Documented exception; retain |
| `references/clusters/action-value.md` | 3,314 | 3,311.20 | -2.80 | -0.08% | Within ±10%; retain |
| `references/clusters/obligation-power.md` | 3,480 | 3,344.67 | -135.33 | -3.89% | Within ±10%; retain |
| `references/clusters/cooperation-care.md` | 3,597 | 4,536.70 | +939.70 | +26.12% | Documented exception; retain |
| `references/clusters/history-possibility.md` | 3,900 | 4,224.40 | +324.40 | +8.32% | Within ±10%; retain |
| `references/clusters/play-inquiry.md` | 3,482 | 3,599.80 | +117.80 | +3.38% | Within ±10%; retain |
| `references/clusters/work-purpose.md` | 3,683 | 3,635.17 | -47.83 | -1.30% | Within ±10%; retain |
| `references/clusters/bureaucracy-technology.md` | 3,541 | 3,477.80 | -63.20 | -1.78% | Within ±10%; retain |
| `references/clusters/violence-audiences.md` | 2,952 | 2,866.47 | -85.53 | -2.90% | Within ±10%; retain |
| `references/clusters/inquiry-revision.md` | 3,969 | 4,531.00 | +562.00 | +14.16% | Documented exception; retain |
| `references/clusters/dialogue-episodes.md` | 3,323 | 2,849.23 | -473.77 | -14.26% | Documented exception; retain |

## What was counted

[Inventory](inventory.json) enumerates every counted concept, move, application and evidence passage with F-record source locators. These are already retained material, not new personality claims. A repeated episode is not independent corroboration. Cross-module conceptual homes are editorial assignments for accounting, not fixed roles assigned to books.

The voice already distinguishes scholarly exposition, public explanation, friendly dialogue, polemic and personal vulnerability. They supply provisional register-cost inputs; they are not empirical register families. Absent measured gradients, quantified avoidance entries, paired anti-drift demonstrations and no-pooling comparisons are not fabricated. Results include sensitivity to one register.

[Source mass](source-mass.json) records supplied-text hashes, eligible line ranges and exact counts. The pool keeps source-authored context and joint work with attribution, removes editorial opening material, keeps DG turns in dialogues, and removes the identified UT reprints of UR/BJ passages. It is not a count of exclusively Graeber-spoken words: embedded attributed quotations remain primary-source context. Only explicit located spans contribute module mass; chapter-only pointers are conservatively omitted. Module overlaps do not make sources independent. This documented mapping adapts the old `words_firsthand` parameter to a cross-book package; results expose the 0–400-token sensitivity rather than pretending the mass estimate is exact completeness.

The core ceiling uses the documented primary-context pool, ten current thematic groups and represented periods. These are editorial source groups, not ten independent books or certified statistical clusters. The lower-ceiling sensitivity is also recorded.

The inventory was made after the existing prose, so it is a retrospective audit, not evidence of prospective sizing or independent calibration. Default coefficients were not tuned to the observed lengths.

## Decisions by module

### SKILL.md

KEEP COMPACT by explicit user instruction. Detailed argument chains live in mandatory standing modules and topic references; the numerical shortfall is not filled. Implementation safeguards are excluded from persona-supply counts.

Counts: `{"cost_refusal": 2, "interactional": 4, "procedure": 2, "projectible": 4, "variation": 1, "verdict": 0}`. Formula contributions: `{"cost_refusal": 500, "frame": 2200, "interactional": 560, "procedure": 400, "projectible": 720, "variation": 120, "verdict": 0}`.

### references/frameworks.md

KEEP. The legacy formula budgets separate entries and an index; current prose combines them and routes concrete cases to topic modules. Do not duplicate those cases or add an index solely to consume the allowance.

Counts: `{"constructs": 29, "epistemic": 6, "moves": 6, "personal": 4, "procedure": 7, "verdict": 9}`. Formula contributions: `{"construct_index_allowance": 725, "constructs": 2400, "epistemic": 780, "frame": 700, "moves": 660, "personal": 280, "procedure": 1200, "verdict": 810}`.

### references/voice.md

KEEP. Five evidenced expressive occasions are represented concisely; they are not five statistically certified families. No quantified avoidance table or artificial contrast pairs are added to satisfy a legacy layout.

Counts: `{"avoid": 0, "nopool_pairs": 0, "pairs": 0, "registers": 5, "rules": 18, "within_family_gradient": 0}`. Formula contributions: `{"avoid": 0, "frame": 600, "gradient": 0, "nopool_pairs": 0, "pairs": 0, "registers": 2200, "rules": 1620}`.

### references/clusters/action-value.md

KEEP. Retain rival arguments, distinct ethnographic examples and the difference between efficacy, meaning and social consequence. No passage is removed to reduce the residual.

Counts: `{"apparatus": 9, "applications": 6, "fragments": 13, "moves": 7, "registers": 1, "siblings": 9}`. Formula contributions: `{"apparatus": 810, "applications": 510, "fixed_frame": 600, "fragments": 390, "mass": 159, "moves": 630, "prohibitions": 215, "registers": 0}`.

### references/clusters/obligation-power.md

KEEP. Retain the causal correction and unresolved remedy objections; they prevent debt critique becoming a fixed instruction to cancel every obligation.

Counts: `{"apparatus": 6, "applications": 6, "fragments": 15, "moves": 6, "registers": 3, "siblings": 9}`. Formula contributions: `{"apparatus": 540, "applications": 510, "fixed_frame": 600, "fragments": 450, "mass": 185, "moves": 540, "prohibitions": 215, "registers": 440}`.

### references/clusters/cooperation-care.md

KEEP. Retain access conditions, institutional interfaces, evolution of care, costs of attachment and the means/ends qualification. These do different work even where they share sources.

Counts: `{"apparatus": 6, "applications": 7, "fragments": 16, "moves": 7, "registers": 3, "siblings": 9}`. Formula contributions: `{"apparatus": 540, "applications": 595, "fixed_frame": 600, "fragments": 480, "mass": 97, "moves": 630, "prohibitions": 215, "registers": 440}`.

### references/clusters/history-possibility.md

KEEP. Retain distinct counterexamples, archaeological qualifications and the Osage revision chain. Shared authorship is preserved; length is not converted into individual-attribution confidence.

Counts: `{"apparatus": 9, "applications": 7, "fragments": 21, "moves": 7, "registers": 2, "siblings": 9}`. Formula contributions: `{"apparatus": 810, "applications": 595, "fixed_frame": 600, "fragments": 630, "mass": 200, "moves": 630, "prohibitions": 215, "registers": 220}`.

### references/clusters/play-inquiry.md

KEEP. Retain enjoyment, cruelty, ambivalence and conjectural limits together; the apparent surplus includes qualifications necessary to avoid a universally cheerful or pseudoscientific persona.

Counts: `{"apparatus": 7, "applications": 6, "fragments": 16, "moves": 6, "registers": 3, "siblings": 9}`. Formula contributions: `{"apparatus": 630, "applications": 510, "fixed_frame": 600, "fragments": 480, "mass": 67, "moves": 540, "prohibitions": 215, "registers": 440}`.

### references/clusters/work-purpose.md

KEEP. Retain the heterogeneous worker accounts and unknown outcomes; collapsing them would erase different conditions behind similar job labels.

Counts: `{"apparatus": 7, "applications": 6, "fragments": 20, "moves": 6, "registers": 3, "siblings": 9}`. Formula contributions: `{"apparatus": 630, "applications": 510, "fixed_frame": 600, "fragments": 600, "mass": 148, "moves": 540, "prohibitions": 215, "registers": 440}`.

### references/clusters/bureaucracy-technology.md

KEEP. Retain positive uses of procedure and the technological antithesis; an across-the-board anti-bureaucratic verdict would lose the judgment conditions.

Counts: `{"apparatus": 7, "applications": 6, "fragments": 17, "moves": 6, "registers": 3, "siblings": 9}`. Formula contributions: `{"apparatus": 630, "applications": 510, "fixed_frame": 600, "fragments": 510, "mass": 96, "moves": 540, "prohibitions": 215, "registers": 440}`.

### references/clusters/violence-audiences.md

KEEP. Retain chronology, audience, personal risk and the unresolved maxim contradiction. Do not expand the short module with speculative psychological explanations.

Counts: `{"apparatus": 5, "applications": 5, "fragments": 11, "moves": 5, "registers": 3, "siblings": 9}`. Formula contributions: `{"apparatus": 450, "applications": 425, "fixed_frame": 600, "fragments": 330, "mass": 42, "moves": 450, "prohibitions": 215, "registers": 440}`.

### references/clusters/inquiry-revision.md

KEEP. Retain multiple types of revision, not one generic rule to admit error. Historical contradiction, better data, failed prediction and a broken analogy require different responses.

Counts: `{"apparatus": 7, "applications": 8, "fragments": 20, "moves": 8, "registers": 3, "siblings": 9}`. Formula contributions: `{"apparatus": 630, "applications": 680, "fixed_frame": 600, "fragments": 600, "mass": 84, "moves": 720, "prohibitions": 215, "registers": 440}`.

### references/clusters/dialogue-episodes.md

KEEP. Retain separate dialogue mechanisms and source attribution. Brief anecdotes remain situated evidence rather than being enlarged into personality laws.

Counts: `{"apparatus": 5, "applications": 6, "fragments": 17, "moves": 6, "registers": 3, "siblings": 9}`. Formula contributions: `{"apparatus": 450, "applications": 510, "fixed_frame": 600, "fragments": 510, "mass": 58, "moves": 540, "prohibitions": 215, "registers": 440}`.

## Loading cost

Default core + voice + frameworks: **10,146.63** estimated tokens. With the two largest distinct topic files: **19,214.33**. All runtime files together: **46,523.07**.

Current routing permits more than two topic modules. The legacy two-module formula is a comparison scenario, not an enforced worst-case ceiling. User input, history, tool output and response allowance are additional.

## Reproduction and validation

Run `python3 transworld-identity/budgets/2026-10-31/recalculate.py --tool-root /path/to/persona-distiller` from the checkout. It calls the metatool cluster calculator and tokenizer, and reproduces the saved targets and residuals from the inspectable census. [Cluster inputs](cluster-inputs.json), [raw cluster calculation](cluster-calculation.json) and [full results](results.json) retain parameters and formula hashes. To reproduce source-mass counts first, run `python3 transworld-identity/budgets/2026-10-31/source_mass.py --sources /path/to/supplied/transcriptions`; it requires the matching supplied files. Their raw text is not distributed.

No runtime passage was added, removed or rewritten to change a residual. The module review found no source defect requiring a content correction in this budget-only pass. No new test case, generated answer, judge call or retry was added. Existing diagnostic applicability and Candidate status remain unchanged; budget arithmetic supplies no new recognition evidence.
