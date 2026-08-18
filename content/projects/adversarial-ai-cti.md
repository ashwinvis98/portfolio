---
title: "adversarial-ai-cti"
date: 2026-08-17
description: "A vendor-neutral STIX 2.1 representation for prompt injection and jailbreaks, so any STIX platform can ingest prompt attacks as structured intelligence. A decision record."
---

## What it is

A STIX 2.1 data model and reference implementation that turns prompt-attack records — prompt injection, jailbreaks — into standard STIX objects any OpenCTI or STIX 2.1 platform can ingest.

## The problem

Most threat intelligence tooling has no first-class way to represent a prompt attack. A dozen vendors now collect them, but each in its own shape: a feed, an SDK, a report format. So an organisation that wants to store, attribute, score, and share a prompt attack the way it already handles every other indicator has nowhere standard to put it, and no way to move it between tools without a bespoke integration each time.

## The design decision

The choice worth defending is **a vendor-neutral STIX 2.1 representation instead of a vendor SDK.**

An SDK is the tempting path: it is turnkey, it ships a client and a feed, and it works the day you install it. But an SDK cannot, by construction, be the cross-vendor interchange format — it ties every consumer to one vendor's client and one vendor's feed. This project takes the other route: define the prompt attack as standard STIX 2.1 — an `ai-prompt` observable for the fact, indicators for the analysis, MITRE ATLAS technique mappings, OWASP-LLM labels, TLP markings — so any platform ingests it from any source with no vendor code in the path.

The tradeoff is real and worth naming. Standards-based interchange gives up turnkey convenience. It depends on platforms understanding the community `ai-prompt` observable and STIX extensions, which are themselves still evolving. It ships code, not a corpus, so you bring your own sources. And it is deliberately not a runtime detector — detection logic belongs in engines built for it. What you get for those costs is the one property an SDK can never have: it belongs to no vendor, so it can sit between them.

## What it doesn't do

- Not a runtime detection engine. Detection logic belongs in tools built for it, such as NOVA.
- Not a new sharing format. It uses STIX 2.1 and existing community extensions rather than inventing another standard.
- Not a corpus. It ships code; sources are yours to bring.

## Limitations

- **Early and unstable.** Layout and interfaces will change; this is work in progress, not a frozen spec.
- **Mapping is conservative, and prefix-anchored.** ATLAS/OWASP mapping anchors each keyword to a leading word boundary, with a whole-word allowlist for short ambiguous keywords (`dan`, `rag`, `worm`, `persona`) that would otherwise collide with unrelated text. So `inject` matches `injection` — intended, cheap stemming — while `dangerous` no longer matches `dan`. Ambiguous input is left unmapped rather than guessed, which avoids false confidence at the cost of under-mapping; every mapping records how it was derived so a consumer can weight it.
- **It inherits the maturity of what it builds on.** It leans on community STIX extensions (the `ai-prompt` observable, `stix2extensions`) that are evolving in parallel.
- **Two indicators per prompt has a cost.** It emits both a STIX-pattern indicator (portable, exact, brittle to rewrites) and a NOVA-pattern indicator (durable against paraphrase, but needs a NOVA engine). That covers both correlation and behavioural matching, at the price of keeping two objects' metadata in sync per prompt.

## Prior art

This builds on public work and is framed as complementary to it, not a replacement:

- **[Thomas Roccia](https://github.com/fr0gger)** — the Indicator of Prompt Compromise concept and the [NOVA framework](https://github.com/Nova-Hunting/nova-framework).
- **[dogesec / David Greenwood](https://github.com/muchdogesec)** — modelling prompts in STIX (the `ai-prompt` observable) and `stix2extensions`.
- **[0DIN](https://0din.ai) (Mozilla)** — a jailbreak threat feed and the [`prompt-toolkit`](https://github.com/0din-ai/prompt-toolkit) SDK, including prompt-similarity LSH signatures. 0DIN ships a vendor SDK and feed; this project defines a vendor-neutral STIX representation any platform can ingest from any source. The two are complementary.
- **[Push Security](https://pushsecurity.com/blog/the-pyramid-of-pain-in-the-ai-era)** — the Pyramid of Pain in the AI era.

## Links

- Repository: https://github.com/ashwinvis98/adversarial-ai-cti
- Correlation building block: [promptlsh](/projects/promptlsh/)
- Design rationale: `docs/SPEC.md` in the repository

## Status

Apache-2.0, public, and early — layout and interfaces will change. Includes a reference OpenCTI enrichment connector that computes the correlation digest on ingest and links similar prompts.
