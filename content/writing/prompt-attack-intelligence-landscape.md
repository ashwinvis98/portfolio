---
title: "The Prompt-Attack Intelligence Landscape"
date: 2026-08-17
draft: true
categories: ["Notes"]
tags: ["threat-intelligence", "adversarial-ai", "prompt-injection", "stix"]
description: "A dozen vendors are now collecting prompt attacks. None of them can share one with each other. A survey of who is doing what, and the gap between them."
---

<!-- SKELETON ONLY. No prose yet — you write this. One-line intent notes per section. -->

## The opening problem
<!-- Intent: set up the thesis. Lots of parties now collect prompt attacks; none can exchange one. Frame as an interchange problem, not a novelty claim. -->

## Roccia — IoPC and NOVA
<!-- Intent: the Indicator of Prompt Compromise concept and the NOVA behavioural-pattern engine. What it does well; that it is a detection pattern, not an interchange format. -->

## dogesec — the `ai-prompt` SCO
<!-- Intent: modelling prompts as a STIX observable. The closest existing standards-based work; credit prominently. -->

## 0DIN — LSH signatures and the commercial jailbreak feed
<!-- Intent: 256-bit SimHash prompt signatures + a commercial jailbreak feed + classifier. The nearest near-collision to promptlsh's semantic digest; a vendor SDK, not a neutral format. -->

## Guardrail vendors — Lakera, Protect AI, HiddenLayer, Prompt Security, Cisco AI Defense
<!-- Intent: runtime detection/guardrail products. They stop attacks; they do not publish a shareable representation of one. -->

## MISP — the incumbent interchange format, and whether it fits
<!-- Intent: the established sharing format. Could it carry prompt attacks today? Where it fits and where it strains. -->

## What falls between them
<!-- Intent: the gap. Detection engines, feeds, and guardrails exist; a vendor-neutral, platform-agnostic way to store/attribute/share a single prompt attack does not. This is the load-bearing section. -->

## What I built, and what it doesn't do
<!-- Intent: adversarial-ai-cti + promptlsh as the small neutral interchange piece. State plainly it is complementary, NOT "nobody has done this" — the novelty claim has been walked back three times. Lead with limitations. -->
