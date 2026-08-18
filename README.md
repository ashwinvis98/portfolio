# Personal site — Ashwin Viswamithiran

Hugo + PaperMod. Two jobs: canonical home for technical writing, and a place that presents projects. Deployed on Vercel.

Positioning everything supports: **"I build the platform layer that makes threat intelligence operational."**

## Structure

```
/                 home — positioning line, recent writing, recent projects
/writing/         all posts, categories Research and Notes only
/projects/        one page per project (decision records, not product pages)
/about/
```

## Categories (posts only)

Blog categories are **Research** and **Notes** — nothing else. `Projects` is a
top-level section, **not** a category (creating a "Projects" category collides
with the section).

- **Research** — findings from measurement. The `promptlsh` evaluation and the
  feed-quality series belong here.
- **Notes** — design and modelling arguments, no repo attached. The
  "coffee-break" post is a Note.

## Conventions

- Every post needs a `description` — it is the meta description and the
  LinkedIn card text. No post ships without one.
- Project pages follow a decision-record structure (what it is → the problem →
  the design decision with the tradeoff named → what it doesn't do →
  limitations → links → status). The limitations section is mandatory.
- No employer name, internal hostname, infrastructure detail, or internal
  metric anywhere on this site.

## Local development

Requires Hugo **extended** (PaperMod compiles SCSS).

```bash
hugo server -D        # preview with drafts at http://localhost:1313
hugo --gc --minify    # production build into public/
```

The theme is vendored under `themes/PaperMod/` (not a git submodule) so Vercel
builds it reliably.

## Deploy

Vercel, framework preset **Hugo**, build `hugo --gc --minify`, output `public`.
Pin `HUGO_VERSION` to the version in `HUMAN-STEPS.md`. See `HUMAN-STEPS.md` for
the full manual checklist (domain, DNS, Search Console).
