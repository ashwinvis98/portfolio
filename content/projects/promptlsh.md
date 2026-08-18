---
title: "promptlsh"
date: 2026-08-17
description: "A portable similarity digest for prompt attacks, so reworded jailbreaks correlate instead of reading as unrelated items. A decision record."
---

## What it is

A similarity digest (fuzzy hash) for adversarial prompts: a fingerprint that stays similar when an attack is reworded, so near-duplicates line up instead of looking unrelated.

## The problem

Malware intelligence has fuzzy hashes — `ssdeep`, `TLSH` — where similar inputs produce similar digests, so a platform clusters a family on its own. Prompt attacks have no equivalent. Store a prompt keyed on its exact text and changing one word makes it look completely unrelated, so a feed of four hundred reworded jailbreaks reads as four hundred separate things. On a real corpus that redundancy is large, not hypothetical: on the full HackAPrompt attack set, 52.6% of prompts are exact duplicates after normalisation, before you even reach the reworded ones.

## The design decision

The load-bearing choice is what goes on the wire: a small lossy digest, or the embedding itself.

If two parties can exchange a few hundred bytes per prompt, the honest answer is **ship an int8-quantised embedding, not a hash.** Measured on WildJailbreak paraphrase pairs, an 8-bit quantised embedding holds essentially the entire retrieval ceiling (recall@1 0.767 vs 0.767 on a general model; 0.820 vs 0.820 domain-tuned) at roughly 384 bytes per vector. The 256-bit SimHash digest this tool emits is 32 bytes but gives up 11 to 21 points against that ceiling. So the semantic options are a genuine size/fidelity curve: full embedding (~1.5 KB, the ceiling) → int8-quant (~384 B, ~ceiling) → SimHash (32 B, −11–21 pts). You pick by byte budget and by how much you mind putting something near-invertible to an embedding on the wire.

The dependency-free lexical MinHash baseline (`plm1`) is deliberately **not** a point on that curve, and the page says so plainly rather than dressing it up. At 128 permutations it is about 1.1 KB — larger than the int8 embedding — and scores 0.537, below it. It is beaten on both size and accuracy. Its only justification is that it needs no ML at all: no model to download, pin, or run, fully deterministic and offline. That is a real reason to want it, and it is the only one.

The tradeoff accepted: choosing a portable digest over shipping embeddings buys cross-party correlation and data minimisation, and costs measurable accuracy. The tool ships the two ends (dependency-free lexical, 32-byte semantic) and treats the mid-size quantised option as measured-but-not-yet-built.

So when is the 32-byte digest the right choice? The measurement narrows it to two cases, and it is worth being precise about both. Where the byte budget genuinely binds — a fingerprint attached to every observable across a high-volume feed, where 32 bytes against 384 is a twelvefold difference in storage and index size. And where you would rather not hand a counterparty something close to invertible: a SimHash of an embedding is lossy in a way a quantised embedding is not. That is a difference in degree of exposure, not a privacy guarantee, and the limitations below say so plainly. If neither case applies, ship the int8 embedding — that is what the numbers say, and this page is not going to pretend otherwise.

## What it doesn't do

- It is not an adversarially robust hash. The scheme is public and deterministic, so someone who knows it can evade it on purpose — reordering words defeats the lexical digest almost entirely, and targeted perturbation can move an embedding across a threshold. It clusters and triages a noisy feed; it is not a security boundary.
- It is not a detector or a classifier. It answers "are these two the same attack reworded," not "is this an attack."
- It does not anonymise. A digest is derived from the prompt and leaks information about it — for near-duplicates, by design. Data minimisation, not a privacy guarantee.

## Limitations

- **Hashing costs accuracy.** The shipping 256-bit digest trails the embedding ceiling by 11–21 points (e.g. domain-tuned centered 0.708 vs 0.820 at a 400-candidate pool). That is the price of 32 bytes.
- **Lexical is order-sensitive.** Under word reordering the lexical similarity collapses to ~0.004 — reshuffling evades it completely.
- **Recall degrades with scale.** Same-attack recall@1 drops as the candidate pool grows (0.708 at N=400 → 0.580 at N=1000, domain-tuned centered), as expected for nearest-neighbour retrieval.
- **The cross-org number is not universal.** The ~2.9x correlation gain over exact matching (35.1% vs 12.2% overlap sharing digests only) comes from random splits of a single high-redundancy corpus. It shows the exact-vs-digest gap on shared source material, not a portable rate. A genuinely cross-corpus test is still outstanding.
- **The strongest backend is mildly in-distribution.** The domain-tuned `0din` model was fine-tuned on WildJailbreak-derived data; the clean general-model reference (`bge-small`, ~0.61 recall@1 at N=400) is the honest number to lead with.

## Links

- Repository: https://github.com/ashwinvis98/promptlsh
- Full reproducible evaluation: [RESULTS.md](https://github.com/ashwinvis98/promptlsh/blob/main/RESULTS.md)
- STIX representation this plugs into: [adversarial-ai-cti](/projects/adversarial-ai-cti/)

## Status

Apache-2.0, published on PyPI as `promptlsh`. Early and pre-1.0: the lexical digest (`plm1`) is implemented and tested; the semantic digest (`pls1`/`pls1c`) is implemented and evaluated, and experimental. The digest is carried on the observable today as a custom STIX property — `x_promptlsh_digest`, specified in `adversarial-ai-cti` — rather than a spec-defined one. Publishing it as a spec-defined property via a STIX 2.1 extension-definition is the outstanding step, and the reason that roadmap item is still open.
