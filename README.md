# Personal site — Ashwin Viswamithiran

Hugo + PaperMod. Two jobs: canonical home for technical writing, and a place that presents projects. Deployed on Vercel.

Positioning everything supports: **"I build the engineering that lets a threat research team get ahead of attacks."**

## Structure

```
/                 home and about in one page (content/_index.md): masthead, currently,
                  about, latest writing, projects, notes, timeline, skills, photos, contact
/writing/         all posts, categories Research and Notes only
/projects/        one page per project (decision records, not product pages)
/about/           redirects to /#about (vercel.json)
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

- **`summary` is mandatory** on every content file (posts and project pages). It is
  hand-written and drives the list-page excerpts; without it Hugo dumps the article body
  onto `/` and `/projects/`. `description` (meta/SEO) is also required.
- **Project pages** follow a decision-record structure (what it is → the problem → the
  design decision with the tradeoff named → what it doesn't do → limitations → links →
  status). The limitations section is mandatory.
- **`receipts`** front matter on project pages drives the traceability strip. Only list
  figures from audits actually performed — never invent a count. A receipts strip that
  overstates is worse than none.
- **Employer names** are allowed **only in `content/_index.md` and `data/timeline.yaml`** —
  nowhere else: not in any post, project page, partial, config value, meta tag, or commit
  message. (The specific names are deliberately not repeated here so this file stays
  clean under the employer-name sweep.)
- **Home page sections** are driven by data files: `data/currently.yaml`, `data/notes.yaml`,
  `data/timeline.yaml`, `data/skills.yaml`, `data/life.yaml`. Edit those, not the templates.
- **Internal detail is forbidden everywhere, the home page included:** internal hostnames,
  instance IDs, file paths, private IPs, internal metrics, team names, ticket references,
  and any architecture detail specific to a production deployment.

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
