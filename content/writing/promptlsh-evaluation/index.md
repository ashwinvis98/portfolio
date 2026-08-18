---
title: "What a Prompt-Attack Fuzzy Hash Actually Buys You"
date: 2026-08-17
draft: true
categories: ["Research"]
tags: ["threat-intelligence", "adversarial-ai", "prompt-injection", "similarity-hashing", "evaluation"]
description: "Measuring a similarity digest for prompt attacks against the embedding it is derived from, and finding it loses. What it buys anyway, and when that is worth it."
---

<!-- KIRO DRAFT for Claude's voice pass. Every figure traces to promptlsh/RESULTS.md.
     Do not add a number that isn't in RESULTS.md. -->

I built a fuzzy hash for prompt attacks — `promptlsh`, a similarity digest where a reworded jailbreak produces a digest close to the original's, so near-duplicates line up instead of reading as unrelated. Then I measured whether it earns its place, against the thing it is derived from. The honest answer is that for most uses you should ship a quantised embedding instead. This is the measurement that says so, and the two cases where the 32-byte digest still wins.

## The question

Malware intelligence has had this for years. `ssdeep` and `TLSH` are fuzzy hashes: similar inputs produce similar digests, so a platform clusters a malware family on its own. Prompt attacks have no equivalent. Store a prompt keyed on its exact text and changing one word makes it look completely unrelated — so a feed of reworded jailbreaks reads as a pile of separate items rather than one campaign seen many times.

The obvious fix is to give a prompt a fuzzy fingerprint. The non-obvious question — the one worth measuring — is *what form that fingerprint should take*, because there is more than one option and they are not equally good.

## The corpus is more redundant than you'd guess

First, is the problem even real? Yes, and measurably so. On the full HackAPrompt attack set — 579,953 inputs — **52.6% are exact duplicates** after normalisation, leaving 274,804 unique. The rate holds across models (36% to 52%) and climbs by challenge level (31% to 100%).

One caveat that has to come first, because the number depends on it: HackAPrompt is multilingual. Around 7.4% of prompts have no ASCII alphanumerics at all, and about 13% carry material non-Latin content. A tokeniser that stripped non-Latin text would collapse all of those together and inflate the duplicate rate. The figures above use a Unicode-aware tokeniser that keeps them distinct, so the redundancy is real, not an artifact.

Beyond exact duplicates, near-duplicates matter more. On a seeded 40k slice, 25% are exact duplicates and roughly another 35% of the *unique* prompts pull into near-duplicate clusters — an overall ~1.8x collapse. Deduplicating by digest genuinely cuts what an analyst reviews. (HackAPrompt is a competition corpus, so its redundancy sits on the high side; treat the shape, not the exact factor, as the takeaway.)

## The measurement

So a fingerprint is worth having. The real design question is what goes on the wire, and the options form a size/fidelity curve:

- a full float embedding — the ceiling, roughly 1.5 KB per prompt;
- an **int8-quantised embedding** — roughly 384 bytes;
- a **256-bit SimHash digest** — 32 bytes (this is what `promptlsh` emits as `pls1`/`pls1c`);
- a **dependency-free lexical MinHash** (`plm1`) — no embedding model at all.

The task: recall@1 on WildJailbreak paraphrase pairs. Each vanilla request (about 113 characters) has a jailbroken rewrite (about 979 characters) — same intent, very different surface. For each vanilla request, is its true rewrite the top match among N candidates? I ran it on a general model (`bge-small`, the clean reference) and a domain-tuned one (`0din`).

## The result that argues against my own tool

Here is the part that undercuts the tool, stated first because it is the most important finding.

**The int8-quantised embedding keeps essentially the entire ceiling** — 0.767 vs a 0.767 ceiling on the general model, 0.820 vs 0.820 on the domain-tuned one (both at a 400-candidate pool) — at about 384 bytes. **The 256-bit SimHash digest gives up 11 to 21 points** against that ceiling; the best case, domain-tuned and centered, is 0.708 against 0.820. That gap is the price of shrinking 384 bytes down to 32.

And the dependency-free lexical digest is worse than that: at 128 permutations a `plm1` digest is about 1.1 KB — *larger* than the 384-byte int8 embedding — and scores 0.537, well *below* it. It is beaten on both axes at once. It is not a point on the size/fidelity curve; it sits off it.

The blunt version: **if you can exchange a few hundred bytes per prompt, ship the int8-quantised embedding, not a hash.** That is what the numbers say, and there is no point pretending otherwise.

## What the hashing buys anyway

So why does the 32-byte digest exist at all? The measurement narrows it to two honest cases.

First, **where the byte budget genuinely binds.** Thirty-two bytes against 384 is about a twelvefold difference in storage and index size. Attach a fingerprint to every observable across a high-volume feed and that multiple stops being academic.

Second, **where you would rather not put something near-invertible on the wire.** A SimHash of an embedding is lossy in a way a quantised embedding is not — the quantised vector is close to recoverable, the bit-signature much less so. That is a difference in *degree of exposure*, not a privacy guarantee, and I would not dress it up as one.

The lexical `plm1` has exactly one reason to exist, and it is neither size nor accuracy: **zero ML dependency.** No model to download, pin, or run; fully deterministic and offline. Use it when you cannot run an embedding model at all. Otherwise the embedding path wins.

Two smaller findings worth carrying: mean-centering (`pls1c`) buys the digest about 5 to 6 points and is essentially free, and a domain-tuned model beats a general one at both the ceiling and the digest. But a general model already gives a usable result — around 0.61 recall@1 at a 400-candidate pool — so no fine-tuning is required to get value.

## What this doesn't show

- These are matching rates on one dataset's paraphrase pairs, not a detection benchmark. The digest answers "are these the same attack reworded," not "is this an attack."
- The cross-org correlation figure I quote elsewhere — digests finding about 2.9x the overlap of exact matching (35.1% vs 12.2%) — comes from random splits of a single high-redundancy corpus. It shows the exact-vs-digest gap on shared source material, not a portable rate. A genuine cross-corpus test is still outstanding.
- The strongest model (`0din`) was fine-tuned on WildJailbreak-derived data, so its numbers are mildly in-distribution; `bge-small`, a general model with no such exposure, is the honest reference to quote.
- Recall@1 degrades as the candidate pool grows — the domain-tuned centered digest drops from 0.708 at 400 candidates to 0.580 at 1000, as expected for nearest-neighbour retrieval.
- The lexical digest is order-sensitive: reordering words collapses similarity to about 0.004. It catches copy-paste-and-tweak rewording, not reshuffling.

## Reproduce it

The full tables, datasets, and scripts are in [`RESULTS.md`](https://github.com/ashwinvis98/promptlsh/blob/main/RESULTS.md) and `eval/`. Everything runs on public corpora — HackAPrompt, JailbreakBench, HarmBench, WildJailbreak — and no corpus is committed to the repo.
