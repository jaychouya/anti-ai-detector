# AI-Trace Phrase Blacklist (CS Academic)

This file lists wording patterns that strongly correlate with AI-generated academic prose, plus suggested rewrites. The list is meant to be conservative: not every word here is wrong, but each one is a high-signal flag worth re-examining.

---

## A. Stock Hype Words

| Avoid | Why it flags AI | Prefer |
|---|---|---|
| comprehensively | Vague universal claim | scoped wording: "across the three benchmarks" |
| seamlessly | Marketing tone | "without manual configuration" |
| robust and scalable | Slogan, no measurable referent | name the specific stress test |
| state-of-the-art | Overused | "the strongest prior method on dataset X" |
| novel | Cheap claim | describe what is actually new |
| paramount | Inflated | "central", or just remove |
| crucial | Inflated | "required for", "necessary because" |
| remarkable | Marketing | give the number instead |
| significant / significantly | Often non-statistical | give magnitude or p-value |
| groundbreaking | Marketing | remove |
| paving the way | Cliché | "this enables", or remove |
| play(s) a vital role | Vague | name the role concretely |

---

## B. Filler Connectors

| Avoid | Prefer |
|---|---|
| It is worth noting that | drop, or rewrite as the actual claim |
| In the context of | "for", or scope it concretely |
| In conclusion | "Overall" or remove |
| Furthermore / Moreover (repeated) | rotate based on logical relation |
| Therefore / Thus (repeated) | tie to actual cause |
| In this paper / In this work (every paragraph) | use only once or twice |

---

## C. AI-Style Hedges

| Avoid | Prefer |
|---|---|
| Delve into | "examine", "study" |
| Shed light on | "explain", "show" |
| A wide range of | give the actual range |
| A myriad of | "many", or count |
| Pivotal | "needed for", drop |

---

## D. Empty Comparison Patterns

| Avoid | Prefer |
|---|---|
| outperforms existing methods | name which methods, on what metric |
| achieves superior performance | give the number and the dataset |
| demonstrates the effectiveness | show the experiment that demonstrates it |
| various datasets | list them |
| diverse settings | list them |

---

## E. Bullet vs Prose Smell

AI text often shows:

- Three-item lists where two would do.
- Parallelism that is too clean ("efficient, accurate, and robust").
- Every paragraph ending with a forward-looking summary line.

When you spot this pattern, prefer:

- Mixed-length bullets, or convert to prose.
- Asymmetric phrasing (different sentence shapes).
- Let some paragraphs end on a concrete fact instead of a meta sentence.

---

## F. Quick Self-Check Heuristics

If a paragraph contains 3+ entries from sections A-D, rewrite it.
If 2+ adjacent sentences start with the same connector, rotate them.
If every paragraph has the shape "Topic sentence -> three claims -> wrap-up", break the pattern in at least half of them.

---

## G. Whitelist Reminder

Do NOT replace these even if they look "stocky":

- Domain method names: SVM, CRF, BiLSTM, Transformer, fuzzy neural network.
- Evaluation protocols: 5-fold cross-validation, leave-one-out.
- Tool/environment names: MATLAB, Python, PyTorch, TensorFlow.
- Math symbols and equation references.

These are the protected terms from `SKILL.md`. The blacklist never overrides term protection.
