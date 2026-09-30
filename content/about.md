---
title: "About"
summary: "Security engineer in Denver, building the threat research program at a satellite, 5G and media company, and writing about what works."
description: "About Ashwin Viswamithiran — security engineer building threat intelligence platforms, detection pipelines and the automation between them."
hideMeta: true
---

{{< portrait >}}

I'm a security engineer in Denver. For the last two years I've been building
the threat research program at DISH Network, now part of EchoStar.

It's an unusual place to do threat intelligence. Most companies have one
business to defend. This one runs satellite TV, Hughes satellite internet, a 5G
wireless network under Boost Mobile, in-home technology services, and a
streaming and content business on top of it all. Every one of those has its own
threat actors, its own vendors and its own ways of being attacked. That breadth
is the best part of the job and the hardest part of it. There is always more
threat than there is time, so the whole program comes down to one skill:
deciding what matters to us, and ignoring the rest with a clear conscience.

## What I've built

When I joined in 2024, the program was a plan, a MISP server that kept falling
over, and a handful of dark web keyword alerts. Today it runs on a production
OpenCTI platform in AWS that pulls from more than fifty open-source, dark web
and commercial sources, and pushes what it learns into our firewalls and
endpoint protection automatically. It has a tiered list of the threat actors
that actually go after our industries, a way of deciding whether a feed is worth
paying for, an assistant that answers analysts' questions from the threat graph
with its sources attached, and an AI track that treats malicious prompts as
threat intelligence. I did most of the building, with a small team, and some of
it I've since open-sourced.

## Where I came from

I studied instrumentation and control engineering at NIT Trichy, which is
mostly the study of sensors, signals and feedback loops. I didn't expect that to
follow me into security, but it did. A SIEM is a wall of sensors, and three
years of SOC engineering at Wipro taught me that a lot of its alarms are bad
plumbing rather than bad actors. A threat feed is a sensor too, one whose
readings go stale. After Wipro came a master's in computer science at CU
Boulder, a stint building LLM services, and then threat intelligence.

**2024 — now · Security Engineer II, DISH Network (EchoStar), Denver**\
Threat intelligence platform and threat research program, built from nothing.

**2023 · AI Software Engineer Intern, Alliant National**\
LLM-backed backend services for document summarisation and retrieval.

**2022 — 2024 · MS Computer Science, University of Colorado Boulder**

**2019 — 2022 · Senior Project Engineer, Wipro**\
SIEM and SOC engineering. Owned the SIEM workstream of a global SOC transition,
migrated a 120TB QRadar deployment from on-premises to AWS, built fifty-odd
custom parsers, and modelled detection use cases against the log sources they
fed.

**2015 — 2019 · B.Tech Instrumentation and Control Engineering, NIT Trichy**

## Things I believe

**A score of 50 is not a score.** When we started pulling in feeds, a lot of
indicators arrived stamped with a default score of 50, and some sources rated
nearly everything above 90. Neither number tells you anything. Nothing we push
to a firewall should inherit someone else's guess, so it gets re-scored on its
source, its age and whether anyone else has seen it.

**Every block should expire.** An indicator is a reading, and readings go
stale. An IP that hosted malware in March is somebody's web server by June.
Every block we push gets a lifetime, and when an indicator stops earning its
place, the block comes off on its own.

**Prioritise by who you are, not by how scary they are.** Our threat actor list
had grown past three hundred names. We cut it to a core set by asking which
actors go after satellite, wireless, streaming and in-home services, not which
ones are the most sophisticated. A brilliant actor who never targets your
industry is someone else's problem. The ones we retired stay searchable, so old
hunts still work.

**A forecast you can't be wrong about isn't a forecast.** When we built a
pipeline that forecasts cyber activity from world events, every prediction had
to name an actor, a target and a time window, so that it could later be marked
right or wrong. Most predictive intelligence is never checked. Ours keeps
score.

**Intelligence is an input, not a product.** A threat report nobody acts on is
a well-formatted opinion. The test for anything we produce is whether it changes
a decision: a block, a hunt, a patch, a priority. If it doesn't, it's noise,
however interesting it is.

## What I work with

**Threat intelligence and detection:** OpenCTI, Intsights, STIX/TAXII, Sigma,
YARA, MITRE ATT&CK, D3FEND and ATLAS, OSINT.

**SIEM, SOAR and XDR:** Cortex XSIAM, Palo Alto XDR, IBM QRadar, Splunk, Azure
Sentinel, Elastic Stack, IBM Resilient SOAR.

**Cloud and infrastructure:** AWS (EC2, ALB, Bedrock, Redshift, S3), Microsoft
Azure, GCP, Docker, Kubernetes. AWS Certified Solutions Architect – Associate.

**Languages and automation:** Python (pycti, GraphQL), Bash, SQL, REST APIs.

**AI:** Amazon Bedrock Knowledge Bases, retrieval-augmented generation, prompt
engineering.

## Off the clock

Denver is a good city to land in if you like being outside. Summers are for
alpine lakes that take most of a morning to reach. Winters are for skiing, where
I'm still working my way onto the black runs, on bluebird days and in whiteouts
alike.

{{< photos >}}

## Get in touch

I'm glad to talk about threat intelligence platforms, detection engineering and
AI security. Email is the fastest way to reach me:
[ashwinvis98@gmail.com](mailto:ashwinvis98@gmail.com).
My résumé is [here](/resume.pdf), and my code is on
[GitHub](https://github.com/ashwinvis98). I'm also on
[LinkedIn](https://www.linkedin.com/in/ashwinviswamithiran/).
