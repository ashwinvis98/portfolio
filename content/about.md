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

## How I approach the work

Most security work is reactive by design. An alert fires, a report lands, an
indicator shows up in a feed, and someone responds. That work matters, but it
means the adversary always moves first. The team I'm on is trying to change
the order: to study how the groups that target us build their tools and shift
their habits, so we can anticipate the next technique, the next piece of
infrastructure or the next campaign before it reaches us.

Two years of working that way has changed how I approach any problem. I start
by asking what will be true in six months, not only what is true today. I build
things so they can be checked, because a system that measures itself gets
better instead of just getting bigger. And I treat research and engineering as
one job: the research says where to look, and the engineering makes looking
cheap enough to do every day.

That's what I bring to a team. Not a particular tool, but the habit of getting
ahead of the problem, and building the feedback loop that shows whether I did.

## What I've built

When I joined in 2024, the program was a plan, a MISP server that kept falling
over, and a handful of dark web keyword alerts. Today it runs on a production
OpenCTI platform in AWS that pulls from more than fifty open-source, dark web
and commercial sources, and pushes what it learns into our firewalls and
endpoint protection automatically. It has a tiered list of the threat actors
that actually go after our industries, a way of deciding whether a feed is worth
paying for, an assistant that answers analysts' questions from the threat graph
with its sources attached (and now feeds the team's risk prioritisation and
forecasting work), and an AI track that treats malicious prompts as
threat intelligence. I did most of the building, with a small team, and some of
it I've since open-sourced.

I also do part of this in the open, mostly on attacks against AI systems. The
[projects](/projects/) are the tools that came out of it, and the
[writing](/writing/) is where I show the measurements, including the ones that
argue against my own work.

## Where I came from

I studied instrumentation and control engineering at NIT Trichy, which is
mostly the study of sensors, signals and feedback loops. I didn't expect that to
follow me into security, but it did. A SIEM is a wall of sensors, and three
years of SOC engineering at Wipro taught me that a lot of its alarms are bad
plumbing rather than bad actors. A threat feed is a sensor too, one whose
readings go stale. After Wipro came a master's in computer science at CU
Boulder, a stint building LLM services, and then threat intelligence.

**2024 — now · Security Engineer II, DISH Network (EchoStar), Denver**\
Threat intelligence platform and threat research program.

**2022 — 2024 · MS Computer Science, University of Colorado Boulder**

**2023 · AI Software Engineer Intern, Alliant National**\
LLM-backed backend services for document summarisation and retrieval.

**2019 — 2022 · Senior Project Engineer, Wipro**\
SIEM and SOC engineering, supporting a global SOC's transition and
transformation.

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

**A forecast you can't be wrong about isn't a forecast.** My team does
forecasting work, and the rule I care about most is simple: every prediction
names an actor, a target and a time window, so it can be marked right or wrong
later. Most predictive intelligence is never checked. That's the gap worth
closing.

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
