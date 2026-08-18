---
title: "The Prompt-Attack Intelligence Landscape"
date: 2026-08-17
draft: true
categories: ["Notes"]
tags: ["threat-intelligence", "adversarial-ai", "prompt-injection", "stix"]
description: "The pieces of prompt-attack threat intelligence exist separately — representation, correlation, vendor-neutral formats — but nobody has composed them into one thing that survives rewording and moves between platforms without bespoke glue. A survey of who does what, and the gap."
---

<!-- SKELETON ONLY. No prose yet — you write this. One-line intent notes per section. -->

## The opening problem
<!-- Intent: set up the thesis as "thin and uncomposed," NOT "nobody can share." Representation (dogesec's ai-prompt SCO), correlation (0DIN's LSH signatures), and interchange formats (MISP/STIX) all exist separately; no one composes representation + rewording-survivable correlation + vendor-neutrality into one thing that moves between platforms without bespoke glue. Frame as a composition gap, not novelty. -->

## Roccia — IoPC and NOVA
<!-- Intent: the Indicator of Prompt Compromise concept and the NOVA behavioural-pattern engine. What it does well; that it is a detection pattern, not an interchange format. -->

## dogesec — the `ai-prompt` SCO
<!-- Intent: modelling prompts as a STIX observable. The closest existing standards-based work; credit prominently. -->

## 0DIN — LSH signatures and the commercial jailbreak feed
<!-- Intent: 256-bit SimHash prompt signatures + a commercial jailbreak feed + classifier. The nearest near-collision to promptlsh's semantic digest; a vendor SDK, not a neutral format. -->

## Guardrail vendors — Lakera, Protect AI, HiddenLayer, Prompt Security, Cisco AI Defense
<!-- Intent: runtime detection/guardrail products. They stop attacks; they do not publish a shareable representation of one. Note consolidation (Protect AI -> Palo Alto, Robust Intelligence -> Cisco) as evidence the vendor map is a wasting asset - which is itself an argument for leading with the measurement, not this survey. -->

## Individual researchers and open-source tooling
<!-- Intent: the gap Ashwin flagged - the survey must not be vendor-only. Status-verified: Simon Willison (coined "prompt injection"; ongoing series), Johann Rehberger / embracethered (Month of AI Bugs), Kai Greshake (indirect prompt injection, arXiv:2302.12173), Leon Derczynski (garak, NVIDIA). OSS tooling: garak, PyRIT, Promptfoo, rebuff, LLM Guard, promptmap, InjectLab. Public corpora incl. L1B3RT4S (elder-plinius) - licensing unclear, verify before citing as data. These do detection / red-team / attack-cataloguing, not shareable CTI representation. -->

## MISP — the incumbent interchange format, and whether it fits
<!-- Intent: the established sharing format. Could it carry prompt attacks today? Where it fits and where it strains. -->

## What falls between them
<!-- Intent: the gap, load-bearing. The pieces exist - dogesec's SCO represents a prompt, 0DIN's signatures correlate one, MISP/STIX can carry it - but no one composes them into vendor-neutral representation + rewording-survivable correlation + cross-platform portability in a single thing. Thin and uncomposed, not absent. -->

## What I built, and what it doesn't do
<!-- Intent: adversarial-ai-cti + promptlsh as the small neutral interchange piece. State plainly it is complementary, NOT "nobody has done this" — the novelty claim has been walked back three times. Lead with limitations. -->
