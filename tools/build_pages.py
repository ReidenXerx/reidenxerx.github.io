#!/usr/bin/python3
"""Generate a detail page for every plugin, and point the cards at them.

One template, one stylesheet, twelve pages: a plugin's page should differ from
its neighbour's in what it says, not in how it looks.
"""
from __future__ import annotations

import html
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from plugins import PLUGINS, SITE  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def page(p: dict) -> str:
    url = f"{SITE}/plugins/{p['slug']}/"
    wide = f"assets/previews/{p['slug']}-wide.webp"
    image = f"{SITE}/{wide}"
    badge_class, badge_text = p["badge"]
    description = f"{p['tagline']} {p['lede']}"

    only = "\n".join(
        f'      <li><b>{esc(head)}</b><span>{esc(body)}</span></li>'
        for head, body in p["only"]
    )

    using = ""
    if p["use"]:
        rows = "\n".join(
            f'        <tr><td><kbd>{esc(key)}</kbd></td><td>{esc(what)}</td></tr>'
            for key, what in p["use"]
        )
        using = f"""
    <section aria-labelledby="using-h">
      <p class="eyebrow kicker">Using it</p>
      <h2 id="using-h">How you reach it</h2>
      <div class="keys-wrap">
      <table class="keys">
        <thead><tr><th>Do this</th><th>And</th></tr></thead>
        <tbody>
{rows}
        </tbody>
      </table>
      </div>
    </section>
"""

    note = f'\n    <p class="note">{esc(p["notes"])}</p>' if p["notes"] else ""

    ld = f"""{{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "{esc(p['name'])}",
  "url": "{url}",
  "description": "{esc(description)}",
  "applicationCategory": "DesktopEnhancementApplication",
  "operatingSystem": "Linux",
  "license": "https://opensource.org/license/mit",
  "codeRepository": "{p['repo']}",
  "isAccessibleForFree": true,
  "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "USD" }},
  "author": {{ "@type": "Person", "name": "DuduPhudu", "url": "{SITE}/" }}
}}"""

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(p['name'])} — Omarchy plugin · DuduPhudu</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<meta name="author" content="DuduPhudu">
<meta name="theme-color" content="#F2F3F0" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0F1215" media="(prefers-color-scheme: dark)">
<meta property="og:site_name" content="DuduPhudu">
<meta property="og:type" content="website">
<meta property="og:locale" content="en">
<meta property="og:title" content="{esc(p['name'])} — {esc(p['tagline'])}">
<meta property="og:description" content="{esc(p['lede'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1440">
<meta property="og:image:height" content="810">
<meta property="og:image:alt" content="{esc(p['name'])} preview card">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p['name'])} — {esc(p['tagline'])}">
<meta name="twitter:description" content="{esc(p['lede'])}">
<meta name="twitter:image" content="{image}">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>

<header class="nav">
  <a class="back" href="/#plugins"><span>&larr;</span> All plugins</a>
  <a class="brand" href="/">Dudu<span class="two">Phudu</span></a>
  <nav class="nav-links" aria-label="Sections">
    <a href="/#flagships">Flagships</a>
    <a href="/#plugins">Omarchy plugins</a>
    <a href="{p['repo']}">GitHub</a>
    <a href="/#support">Support</a>
  </nav>
</header>

<main class="detail">

  <div class="detail-head">
    <p class="eyebrow">{esc(p['eyebrow'])}</p>
    <h1>{esc(p['name'])}<span class="badge {badge_class}">{esc(badge_text)}</span></h1>
    <p class="tagline">{esc(p['tagline'])}</p>
    <p class="lede">{esc(p['lede'])}</p>
    <div class="actions">
      <button class="copy" type="button" data-copy="{esc(p['install'])}">Copy install</button>
      <a class="button" href="{p['repo']}">GitHub</a>
    </div>
  </div>

  <div class="shot">
    <img src="/{wide}" alt="{esc(p['name'])} preview card" width="1440" height="810">
  </div>

  <section aria-labelledby="only-h">
    <p class="eyebrow kicker">What only {esc(p['name'])} does</p>
    <h2 id="only-h">Why this one</h2>
    <ul class="only">
{only}
    </ul>{note}
  </section>
{using}
  <section aria-labelledby="get-h">
    <p class="eyebrow kicker">Getting it</p>
    <h2 id="get-h">One command</h2>
    <div class="actions">
      <button class="copy" type="button" data-copy="{esc(p['install'])}">{esc(p['install'])}</button>
    </div>
    <p class="lede">Then restart the shell with <code>omarchy-restart-shell</code>. Licensed {esc(p['licence'])};
    remove it any time with <code>omarchy plugin remove</code>.</p>
  </section>

  <div class="pagefoot">
    <a class="back" href="/#plugins"><span>&larr;</span> All plugins</a>
    <span>Free and open source. <a href="https://donatello.to/DuduPhudu">Support its development</a>.</span>
  </div>

</main>

<script>
  document.querySelectorAll("[data-copy]").forEach(function (button) {{
    button.addEventListener("click", function () {{
      var label = button.textContent
      var done = function (text) {{
        button.textContent = text
        setTimeout(function () {{ button.textContent = label }}, 1600)
      }}
      if (!navigator.clipboard) return done("Copy failed")
      navigator.clipboard.writeText(button.dataset.copy).then(
        function () {{ done("Copied") }}, function () {{ done("Copy failed") }})
    }})
  }})
</script>
</body>
</html>
"""


def write_pages() -> list[str]:
    written = []
    for p in PLUGINS:
        out = ROOT / "plugins" / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(p), encoding="utf-8")
        written.append(f"/plugins/{p['slug']}/")
    return written


def write_sitemap(today: str) -> int:
    """Keep the sitemap's plugin entries exactly in step with the pages."""
    p = ROOT / "sitemap.xml"
    xml = p.read_text()
    # Drop any plugin entries from a previous run, then add the current set.
    xml = re.sub(r"\n  <url>\s*<loc>[^<]*/plugins/[^<]*</loc>.*?</url>", "", xml, flags=re.S)
    block = "".join(
        f"\n  <url>\n    <loc>{SITE}/plugins/{pl['slug']}/</loc>"
        f"\n    <lastmod>{today}</lastmod>\n    <priority>0.7</priority>\n  </url>"
        for pl in PLUGINS
    )
    xml = xml.replace("\n</urlset>", block + "\n</urlset>")
    p.write_text(xml)
    return len(PLUGINS)


if __name__ == "__main__":
    import datetime
    today = datetime.date.today().isoformat()
    pages = write_pages()
    n = write_sitemap(today)
    print(f"wrote {len(pages)} pages and {n} sitemap entries")
