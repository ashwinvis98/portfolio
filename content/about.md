---
title: "About"
summary: "Security engineer in Denver, a founding engineer on the threat research team at a satellite, 5G and media company, and writing about what works."
description: "About Ashwin Viswamithiran — security engineer building threat intelligence platforms, detection pipelines and the automation between them."
hideMeta: true
---

{{< portrait >}}

I'm a security engineer in Denver. I joined DISH Network, now part of
EchoStar, in 2024 as a founding engineer on its threat research team.

It's an unusual place to do threat intelligence. Most companies have one
business to defend. This one runs satellite TV, Hughes satellite internet, a 5G
wireless network under Boost Mobile, in-home technology services, and a
streaming and content business on top of it all. Every one of those has its own
threat actors, its own vendors and its own ways of being attacked. That breadth
is the best part of the job and the hardest part of it. There is always more
threat than there is time, so the whole program comes down to one skill:
deciding what matters to us. That means the actors and techniques aimed at our
industries today, and the emerging capabilities that could be aimed at them
tomorrow.

## How I approach the work

Most security work is reactive by design. An alert fires, a report lands, an
indicator shows up in a feed, and someone responds. That work matters, but it
means the adversary always moves first. My team works the other way round. We
study how the groups that target us build their tools and how their habits
shift over time, so we can anticipate the next technique, the next piece of
infrastructure or the next campaign before it reaches us.

Two years of working that way has shaped how I take on any problem. I solve
the one in front of me, and I design for the version of it that will show up
next. I build things so they can be checked, because a system
that measures itself gets better instead of just getting bigger. And I treat
research and engineering as one job: the research says where to look, and the
engineering makes looking cheap enough to do every day.

AI has changed the engineering half of that. With coding assistants and agents
alongside me, the distance between an idea and a working system has shrunk from
months to days. I spend the time that frees up on testing more ideas, and on
checking that the ones I keep actually work.

That's what I bring to a team. Not a particular tool, but the habit of getting
ahead of the problem, and building the feedback loop that shows whether I did.

## What I've built

When I joined in 2024, the program was a plan, a MISP server that kept falling
over, and a handful of dark web keyword alerts. Today it runs on a production
OpenCTI platform in AWS that pulls from a wide range of open-source, dark web
and commercial sources, and pushes what it learns into our firewalls and
endpoint protection automatically. I did most of the building, with a small
team.

Two directions interest me most from here. The first is what happens when
security tools start talking to each other. Through the Model Context Protocol,
an AI agent can reach a threat intelligence platform, a commercial intelligence
service and a security operations platform in the same conversation, and carry
a question from "what is this?" all the way to "it's contained". I'm exploring
how far that chain can run, from intelligence to remediation, with a person
still deciding at the points that matter.

The second is AI as a target. Two years ago there was almost no threat
intelligence about attacks on AI systems. Now there are feeds, frameworks like
MITRE ATLAS and the OWASP Top 10 for LLMs, and a small community working out how
to describe a malicious prompt the way we already describe malware. I lead
our research on it, and I expect it to become as ordinary a part of a
threat program as phishing is today.

Some of this I work on in public. The [projects](/projects/) are tools I've
released, and the [writing](/writing/) is where I test ideas against real data
and report what I find, even when it cuts against my own work.

## Where I came from

I studied instrumentation and control engineering at NIT Trichy, which is
mostly the study of sensors, signals and feedback loops. I didn't expect that to
follow me into security, but it did.

I spent three years in SOC engineering at Wipro, onboarding new client
organisations onto a managed security service. That meant sitting with each
team to work out what their systems could log and what they should, building
the parsers that turned raw logs into normalised fields a rule could read, and
threat modelling each environment to decide which detections it needed first.
A SIEM is a wall of sensors, and it is only as good as what it has been wired
to read. A threat feed is a sensor too, and its readings decay.

After Wipro came a master's in computer science at CU Boulder, a stint building
LLM services, and then the move into the threat intelligence landscape.

**2024 — now · Security Engineer II, DISH Network (EchoStar), Denver**\
Threat intelligence platform and threat research program.

**2022 — 2024 · MS Computer Science, University of Colorado Boulder**

**2023 · AI Software Engineer Intern, Alliant National**\
LLM-backed backend services for document summarisation and retrieval.

**2019 — 2022 · Senior Project Engineer, Wipro**\
SIEM and SOC engineering, supporting a global SOC's transition and
transformation.

**2015 — 2019 · B.Tech Instrumentation and Control Engineering, NIT Trichy**

## What being ahead of the curve means

**The clock starts before the report.** Intelligence has a shelf life, and much
of it is spent waiting: to be validated, written up, published and read. Every
hour of that is an hour the adversary gets for free. Being ahead is often less
about knowing more than about shortening the distance between knowing something
and acting on it.

**Watch capability, not just activity.** Activity tells you what an adversary
did. Capability tells you what they could do next. New tools, new techniques
and new services for sale on criminal markets appear well before the campaigns
that use them, and that lead time is the whole advantage.

**AI raises the floor for attackers first.** AI hasn't created a new kind of
adversary so much as made the existing ones faster, cheaper and more fluent. An
average operator with the right model writes better lures, runs reconnaissance
at scale and reworks tooling in hours. The question isn't whether that shift
reaches you, but whether you saw it before it did.

**You can't detect what you never logged.** Onboarding organisations onto a
SIEM taught me that the most important conversation happens before any rule is
written: sitting with the people who run each system and agreeing what it
should record. Nearly every detection gap I've seen traces back to that
conversation, or to its absence.

**Detection is won in normalisation.** A log the SIEM can't parse might as
well not exist. Most of the value of a detection program sits in the
unglamorous layer that maps every source into the same fields, so a rule
written once works everywhere.

**Coverage should be something you can count.** Once you know what you can
see, threat model what you can't: what an attacker could do in this
environment that nothing would record or flag. Map both the detections you
have and the gaps you've found to a common framework like MITRE ATT&CK, and
coverage stops being a feeling and becomes a list you can work through.

## What I work with

**Threat intelligence and detection:** OpenCTI, STIX/TAXII, Sigma, YARA,
OpenAEV, OSINT, Intsights.

**Frameworks:** MITRE ATT&CK, MITRE ATLAS, D3FEND.

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
My résumé is [here](/Ashwin-Viswamithiran-Resume.pdf), and my code is on
[GitHub](https://github.com/ashwinvis98). I'm also on
[LinkedIn](https://www.linkedin.com/in/ashwinviswamithiran/).
