---
title: "opencti-ai-enrichment"
date: 2026-09-30
summary: "An OpenCTI enrichment connector where the language model proposes entities and relationships and deterministic code decides which ones reach the graph."
description: "An OpenCTI enrichment connector where the language model proposes entities and relationships and deterministic code decides which ones reach the graph. A decision record."
related:
  - "it-reads-better-than-it-decides"
  - "twelve-ways-to-make-a-threat-intel-bot-lie"
  - "cozy-bear-the-dukes-and-apt29"
receipts:
  - "Apache-2.0"
  - "374 tests, no credentials"
  - "Gemini + OpenCTI"
  - "pre-1.0"
---

{{< receipts >}}

## What it is

An OpenCTI internal-enrichment connector that reads a report with Google Gemini and connects it to the actors, malware families, techniques and sectors it is about. The model extracts; a deterministic guard layer decides what, if anything, is written to the knowledge graph.

## The problem

Threat intelligence feeds are excellent at the mechanical half of the job and mostly decline the other half. Indicators arrive in bulk, correctly typed and attached. What rarely arrives is the link between the report and the thing the report is about — most visibly in reports named after something they are not connected to, like a write-up titled *DarkMe RAT* that is hundreds of indicators deep and barely linked to that malware family.

That is a defensible choice rather than a bug: being wrong about an indicator is cheap, while "this campaign is Konni" is an attribution claim that needs someone to read prose and accept being wrong in a way that misleads people. So the consumer inherits the judgement work and usually cannot staff it. The cost is invisible — a report with hundreds of indicators and no actor link looks productive, and the query "what do we know about Konni" quietly returns an incomplete answer that nobody gets paged for.

## The design decision

The choice worth defending is **the model never decides anything — it proposes, and deterministic code disposes.**

Gemini's extraction is genuinely good, and that is not the part in question. The problem is what a mistake costs in this specific destination. A hallucinated indicator is noise: it sits in a list, nobody builds on it, it ages out. A hallucinated *relationship* is a false claim about the world, carrying a confidence score, structurally indistinguishable from the true relationships beside it, and it will be picked up by a query and acted on. Nothing about its appearance marks it as invented.

So every proposal passes through a funnel — shape guards, category vocabularies, controlled taxonomies, dedup, a groundedness check against the source text, and OpenCTI's own relationship schema — and **every stage can only subtract.** There is no path where a model's confidence unlocks something the guards refused. The consequence is that reasoning about what this connector can do to your graph means reading `guards.py`, not predicting a model's behaviour. An optional second model pass exists as a critic, and it is restricted to dropping and reclassifying: two models from the same family agreeing is correlated error with extra steps, not verification.

The tradeoff is real: this is slower to build and slower to trust than pointing a model at a feed and enabling writes, and it front-loads unglamorous work — vocabularies recording that Microsoft Exchange is infrastructure and CrowdStrike is a security product, so a report *about* exploiting Exchange does not file Exchange as the malware. There is no elegant general rule for that. You write it down once, and it then holds on every report at 3am without attention.

**One failure made the decision for me.** Gemini proposes CVE identifiers that exist at neither NVD nor CVE.org — and some arrive verbatim in the source feed's own report title, so the groundedness check finds them and waves them through. The guard built for exactly that error was structurally incapable of seeing it, and a blind guard is worse than a weak one because it makes you confident. CVE creation is now removed rather than disabled, with a test asserting it stays gone.

## What it doesn't do

- Not a general AI-for-CTI platform. One connector, one model provider, six entity types.
- Not autonomous. Which entity categories may write is a human decision, made per category, informed by what the logs show.
- Not a fix for attribution gaps. Where the source material does not attribute, the model generally does not either — on a report whose missing attribution was the interesting part, it named no actor and no malware family, only techniques.
- Not a corpus. The labelled victim data behind the guard work is real breach reporting about real organisations and is not published. The labelling and scoring methodology is.

## Limitations

- **The confidence score is the model's own self-report,** and it comes back high on nearly every document regardless of how thin or contradictory the source was. The connector writes it into the entity's score, which makes it provenance rather than quality; using it as a filter would be a mistake. The weakest part of the design as it stands.
- **Only Gemini has been run.** The vendor SDK is isolated to a fifteen-line module, which would make another provider a contained change, but I have not done it — and there is deliberately no provider abstraction, because an interface with one implementation advertises portability it has not demonstrated.
- **Victim extraction is the noisiest category by a wide margin,** and stays gated for that reason. A large share of the organisations named are not in the knowledge base: some real and merely unrecorded, some artefacts of a partially-read name.
- **The vocabularies are a maintenance surface.** Every "this software is infrastructure, not malware" entry is hand-written and drifts as the software landscape does.
- **Guards are code, and code is wrong.** The mitigations are cautious defaults, reversibility — everything created carries an `ai-suggested` label, so undoing it is one query — and a test suite concentrated on the guard layer. Not a belief that the layer is correct.

## Prior art

- **[OpenCTI](https://github.com/OpenCTI-Platform/opencti) / Filigran** — the platform, its STIX data model, and the connector framework this plugs into.
- **[MITRE ATT&CK](https://attack.mitre.org/)** — the authoritative technique catalogue. Attack-Patterns here are lookup-only against it, permanently.
- **[NVD](https://nvd.nist.gov/) and [CVE.org](https://www.cve.org/)** — the authoritative source of vulnerability identifiers, and the reason CVE creation was removed.
- **AlienVault OTX** (now LevelBlue-operated) — the OSINT feed the worked examples are drawn from.

## Links

- Repository: https://github.com/ashwinvis98/opencti-ai-enrichment
- What the model got right and wrong: [OBSERVATIONS.md](https://github.com/ashwinvis98/opencti-ai-enrichment/blob/main/OBSERVATIONS.md)
- Reasoning and the six reversals: [DESIGN.md](https://github.com/ashwinvis98/opencti-ai-enrichment/blob/main/DESIGN.md)
- The write-up: [It Reads Better Than It Decides](/writing/it-reads-better-than-it-decides/)
- Related failure mode, in a chatbot rather than a graph: [Twelve Ways to Make a Threat-Intel Bot Lie](/writing/twelve-ways-to-make-a-threat-intel-bot-lie/)

## Status

Apache-2.0, public, and pre-1.0. Run against a live OSINT feed. The extraction does what it is meant to; the guard layer is where most of the engineering went, and the things it refuses are things I watched the model get wrong rather than hypotheticals. Two entity categories — Attack-Patterns and CVEs — had their creation capability removed rather than tuned, and will stay that way. The outstanding work is replacing the self-reported confidence score with something that actually discriminates.
