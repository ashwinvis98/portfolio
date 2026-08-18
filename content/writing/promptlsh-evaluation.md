---
title: "What a Prompt-Attack Fuzzy Hash Actually Buys You"
date: 2026-08-17
draft: true
categories: ["Research"]
tags: ["threat-intelligence", "adversarial-ai", "prompt-injection", "similarity-hashing", "evaluation"]
description: "Measuring a similarity digest for prompt attacks against the embedding it is derived from, and finding it loses. What it buys anyway, and when that is worth it."
---

<!-- SKELETON ONLY. No prose yet — you write this. Every number that goes in must trace to RESULTS.md. -->

## The question
<!-- Intent: why anyone would want a fuzzy hash for prompts at all; the ssdeep/TLSH analogy and why prompt attacks have no equivalent. -->

## The corpus is more redundant than you'd guess
<!-- Intent: the HackAPrompt redundancy result; note the tokenisation caveat prominently, since the number depends on it. -->

## The measurement
<!-- Intent: set up the size/fidelity curve — full embedding -> int8-quant -> SimHash -> lexical. State the task (recall@1 on WildJailbreak paraphrase pairs) before any number. -->

## The result that argues against my own tool
<!-- Intent: int8-quant holds the ceiling; SimHash costs 11-21 points; the lexical baseline is dominated on both axes. Lead with this, do not bury it. -->

## What the hashing buys anyway
<!-- Intent: the two surviving cases. Must stay consistent with the promptlsh project-page paragraph (byte budget binds; not wanting something near-invertible on the wire). -->

## What this doesn't show
<!-- Intent: single corpus, random splits not a genuine cross-corpus test, domain model mildly in-distribution, matching rates not detection benchmarks. -->

## Reproduce it
<!-- Intent: point at RESULTS.md and eval/. -->
