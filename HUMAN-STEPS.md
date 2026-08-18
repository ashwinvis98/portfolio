# HUMAN-STEPS

Everything Kiro can't do (needs a browser, a card, or a DNS panel), in order, with
exact values. Split into two phases because you're starting on a temporary Vercel
domain and deferring the indexing work until you own a real domain.

**Build facts Kiro produced:**

- Hugo version built against: **0.164.0** (extended). Pin this in Vercel.
- The only file with a placeholder domain is `hugo.toml` -> `baseURL`
  (currently `https://ashwinviswamithiran.com/`). `robots.txt` and `sitemap.xml`
  are generated from `baseURL`, so updating that one line updates them too.
- Build command: `hugo --gc --minify` — Output directory: `public`

---

## Phase A — Get it live on the temporary Vercel domain (no purchase needed)

1. **Create a public GitHub repo** (suggested name `site`) and push.
   First, before committing, confirm the configured identity is personal (the `git log`
   check is useless here — there are no commits yet):
   ```bash
   git -C site config user.name    # expect: Ashwin Viswamithiran
   git -C site config user.email   # expect: ashwinvis98@gmail.com
   ```
   Then commit, and verify the commit history carries only the personal identity
   *before* pushing:
   ```bash
   git -C site add -A
   git -C site commit -m "Initial site"
   git -C site log --format='%an <%ae>' | sort -u   # must show only ashwinvis98@gmail.com
   git -C site branch -M main
   git -C site remote add origin https://github.com/ashwinvis98/site.git
   git -C site push -u origin main
   ```

2. **Vercel account + import.** vercel.com, sign in with GitHub, Add New -> Project ->
   import the repo. Confirm:
   - Framework Preset: **Hugo**
   - Build Command: `hugo --gc --minify`
   - Output Directory: `public`

3. **Pin the Hugo version.** Project -> Settings -> Environment Variables:
   ```
   HUGO_VERSION = 0.164.0
   ```
   Without this, Vercel picks a default that can drift and break the build later.

4. **Deploy.** You get a URL like `your-project.vercel.app`.

5. **Set `baseURL` to the temp URL.** Edit `hugo.toml` -> `baseURL` to
   `https://your-project.vercel.app/`, commit, push (auto-redeploys). This makes RSS,
   sitemap, and Open Graph links resolve correctly.

   > NOTE: while you're on a `*.vercel.app` domain, `vercel.json` sets
   > `X-Robots-Tag: noindex` on the whole site. That's fine and intended for this
   > phase — you are not trying to get the temp domain indexed. See Phase B.

---

## Phase B — Make it the indexed canonical home (requires a real domain)

Do this half only once you've bought a domain. This is the whole point of leaving
Medium, so don't run these steps against the temp domain.

6. **Buy the domain.** Personal name is the plan (`ashwinviswamithiran.com` or
   `ashwinvis.com`). Registrars: Cloudflare Registrar (at-cost), Porkbun, or Namecheap.
   Avoid GoDaddy upsells. Cost ~$10-15/year. Vercel Hobby hosting itself is free.

7. **Add the domain in Vercel:** Project -> Settings -> Domains -> add it. Vercel shows
   the exact records for your project.

8. **DNS — read the exact values from your Vercel dashboard**, not from here. Vercel
   issues per-project targets. General-purpose fallbacks, for reference only:
   - Apex `@`  ->  A record  ->  `76.76.21.21`
   - `www`     ->  CNAME     ->  `cname.vercel-dns-0.com`

9. **Three DNS gotchas — check all three:**
   - **Delete stale apex A records** from any previous host. Leftover apex A records
     block verification and cause a confusing "Invalid Configuration" state.
   - **Remove all AAAA records for the apex.** Vercel doesn't support IPv6 via
     third-party DNS; a stray AAAA splits traffic and can stall SSL provisioning.
   - **On Cloudflare, set the records to "DNS only" (grey cloud), not proxied.**
     Proxied + Vercel HTTPS produces redirect loops.

10. **Choose a canonical host** (apex or www), set the other to redirect in Vercel's
    Domains panel, then **update `baseURL` in `hugo.toml`** to match exactly, commit,
    push.

11. **Confirm HTTPS** provisioned (automatic, usually a minute or two after DNS
    resolves).

12. **Verify the preview-noindex actually fires** — a silently non-firing rule is worse
    than none. On the real domain the production site must NOT be noindexed; preview
    URLs must be. Use whichever matches your shell:

    PowerShell / cmd:
    ```
    curl -I https://<some-branch-preview>.vercel.app/ | findstr /I "x-robots-tag"   # expect: noindex
    curl -I https://YOURREALDOMAIN/ | findstr /I "x-robots-tag"                      # expect: no such header
    ```
    bash:
    ```
    curl -sI https://<some-branch-preview>.vercel.app/ | grep -i x-robots-tag        # expect: noindex
    curl -sI https://YOURREALDOMAIN/ | grep -i x-robots-tag                          # expect: no such header
    ```
    (Note: Vercel already noindexes preview deployments automatically, so `vercel.json`
    here is belt-and-suspenders.)

13. **Google Search Console:** add the property, verify by DNS TXT record, submit the
    sitemap `https://YOURREALDOMAIN/sitemap.xml`, then URL Inspection -> Request Indexing
    on the migrated coffee-break post.

14. **Bing Webmaster Tools:** two minutes, imports directly from Search Console.

15. **Update LinkedIn Featured** to point at the new domain instead of Medium.

---

## Content decisions still on you (before publishing)

- **Verify the migrated post body against the Medium original, and re-add the images.**
  It was captured from the Medium URL (you didn't have the file). Prose is intact but
  images didn't come through — they're marked `<!-- image: ... -->` in
  `content/writing/from-half-a-day-to-a-coffee-break.md`.
- **Rewrite the placeholder paragraph** in `content/projects/promptlsh.md` — the "when is
  the 32-byte digest the right choice?" paragraph in the design-decision section is a
  stand-in in your argument, marked with an HTML comment. Put it in your own voice.
- **Write the two draft posts:** `prompt-attack-intelligence-landscape.md` and
  `promptlsh-evaluation.md` are `draft: true` skeletons — section headings and intent
  notes, no prose.

The first-person voice pass and the de-abstraction (OpenCTI / Amazon Bedrock Knowledge
Bases / CPE) are done and applied, so they're off this list.

## Cost note

Vercel **Hobby is free and sufficient** for this static site; the only spend is the
domain. Hobby is **non-commercial use only** — if the site ever fronts consulting or a
paid product, switch to Pro promptly, as it's the kind of terms issue that gets a site
suspended without warning.
