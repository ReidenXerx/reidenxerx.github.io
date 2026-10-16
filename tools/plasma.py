"""The KDE Plasma 6 editions: one source for the /plasma/ page and every plugin page's "Also on KDE Plasma" section.

Until they are on the KDE Store they install from each repository's `plasma` branch, and the pages say they are in
testing.
"""
from __future__ import annotations

import html

# slug: (name, repository name, what is different on Plasma)
PLASMA = {
    "hourglass": ("Hourglass", "omarchy-hourglass",
                  "Plasma's task manager says which app is in front; a small recorder service on your session bus keeps "
                  "the clock and asks Plasma how long you have been idle. One press of Start recording sets it up."),
    "reserve": ("Reserve", "omarchy-reserve",
                "Fits the panel or the system tray beside Plasma's own battery widget; the level comes from Plasma's power "
                "management, the history from the same sampler."),
    "varta": ("Varta", "omarchy-varta",
              "The band is a strip Plasma keeps above everything, full-screen video included, and alerts, all-clears and "
              "a lost feed are Plasma notifications too; the alert one stays until you dismiss it."),
    "dgpu-status": ("dGPU status", "omarchy-dgpu-status",
                    "An icon in the panel or the tray that is muted while the card sleeps, and gpuwho's list in its popup. "
                    "Hidden on computers without an NVIDIA card."),
    "dusk": ("Dusk", "omarchy-dusk",
             "A companion to Plasma's own Night Light rather than a second one: true colour for the apps you name or any "
             "fullscreen one, off until morning, presets you can preview, and the night on a dial."),
    "cockpit": ("Cockpit", "omarchy-cockpit",
                "The same hub and providers, your own included. Chats and running sessions come from Claude Code's own "
                "records; terminals and folders open in Konsole, Dolphin or your defaults."),
    "emoji-picker": ("Emoji picker", "omarchy-emoji-picker",
                     "A popup on the key you give it. Picks are typed by pasting through Plasma's remote-input "
                     "permission, which it asks for once; GIFs go as their link."),
    "keyboard-cleaner": ("Keyboard cleaner", "omarchy-keyboard-cleaner",
                         "Switches off the keyboards KWin knows, never the touchpad or mouse, with the same four ways "
                         "back, and switches on any keyboard left off at your next login."),
    "mynah": ("Mynah", "omarchy-mynah",
              "The bird in the panel, a pill while you speak, and its own shortcut. It types by pasting through "
              "Plasma's remote-input permission; what you dictate passes through Plasma's clipboard history."),
}

SITE_REPO = "https://github.com/ReidenXerx"


def install(slug: str) -> str:
    repo = PLASMA[slug][1]
    return (f"git clone -b plasma {SITE_REPO}/{repo}.git && cd {repo} && tools/build-plasma && "
            f"kpackagetool6 -t Plasma/Applet -i dist/app.duduphudu.{slug}")


def section(slug: str) -> str:
    """The "Also on KDE Plasma" section of a plugin's page, between markers so it can be replaced in place."""
    name, repo, differs = PLASMA[slug]
    esc = lambda t: html.escape(t, quote=True)  # noqa: E731
    return f"""<!-- plasma -->
  <section aria-labelledby="plasma-h">
    <p class="eyebrow kicker">Also on KDE Plasma <span class="badge testing">In testing</span></p>
    <h2 id="plasma-h">{esc(name)} for Plasma 6</h2>
    <p class="lede">{esc(differs)}</p>
    <div class="actions">
      <button class="copy" type="button" data-copy="{esc(install(slug))}">Copy Plasma install</button>
      <a class="button" href="{SITE_REPO}/{repo}/tree/plasma">The plasma branch</a>
      <a class="button" href="/plasma/">All Plasma widgets</a>
    </div>
    <p class="note">Then right click the panel, choose Add or Manage Widgets, and drag {esc(name)} onto it.
    Until it is on the KDE Store it installs from its <code>plasma</code> branch.</p>
  </section>
<!-- /plasma -->"""


def apply(root) -> list[str]:
    """Put the section on every plugin page that has a Plasma edition, just before "Getting it", replacing any
    earlier copy; generated and hand-written pages alike."""
    import re
    done = []
    for slug in PLASMA:
        page = root / "plugins" / slug / "index.html"
        if not page.exists():
            continue
        # Exactly what the insertion below adds, so running this twice changes nothing.
        text = re.sub(r"\n[ \t]*<!-- plasma -->.*?<!-- /plasma -->", "", page.read_text(encoding="utf-8"), flags=re.S)
        anchor = re.search(r'\n([ \t]*)<section aria-labelledby="get-h">', text)
        if not anchor:
            raise SystemExit(f"{page}: no 'Getting it' section to put the Plasma one before")
        indent = anchor.group(1)
        block = "\n".join(indent + line if line and not line.startswith("  ") else (indent + line if line else line)
                          for line in section(slug).splitlines())
        text = text[:anchor.start()] + "\n" + block + text[anchor.start():]
        page.write_text(text, encoding="utf-8")
        done.append(slug)
    return done


# What stays on Omarchy, and why: (names, reason).
NOT_PORTED = [
    ("Clipboard shelf", "Plasma's own clipboard already pins items: star one in its history and it stays."),
    ("Idle dim", "Plasma's Power Management already dims the screen before it turns off."),
    ("Barber, Tile blueprints, Aerial, Tactile, Omalang",
     "They reshape Hyprland and Omarchy's bar themselves; on Plasma, System Settings and KWin do those jobs."),
    ("Omagram and PenguID", "Later: Omagram's window would have to be rewritten for Plasma, and face unlock needs "
     "Plasma's lock screen and PAM work first."),
]

PAGE_URL = "https://duduphudu.app/plasma/"


def write_page(root) -> None:
    """The /plasma/ page: every Plasma edition, how it is installed, how typing works there, and what stays."""
    esc = lambda t: html.escape(t, quote=True)  # noqa: E731
    pages = {"mynah": "/mynah/"}
    cards = []
    for slug, (name, repo, differs) in PLASMA.items():
        page = pages.get(slug, f"/plugins/{slug}/")
        cards.append(f"""    <article class="card" id="{slug}">
      <div class="card-body">
        <div class="card-top"><h3><a class="stretch" href="{page}">{esc(name)}</a></h3><span class="badge testing">In testing</span></div>
        <p>{esc(differs)}</p>
        <div class="actions">
          <button class="copy" type="button" data-copy="{esc(install(slug))}">Copy Plasma install</button>
          <a href="{page}">Page</a>
          <a href="{SITE_REPO}/{repo}/tree/plasma">plasma branch</a>
        </div>
      </div>
    </article>""")
    stays = "\n".join(f'      <li><b>{esc(names)}</b><span>{esc(why)}</span></li>' for names, why in NOT_PORTED)
    every = ("mkdir -p ~/plasma-widgets && cd ~/plasma-widgets && for w in "
             + " ".join(PLASMA) + "; do git clone -q -b plasma " + SITE_REPO
             + "/omarchy-$w.git && (cd omarchy-$w && tools/build-plasma >/dev/null && "
             "kpackagetool6 -t Plasma/Applet -i dist/app.duduphudu.$w); done")
    description = ("Nine of DuduPhudu's Omarchy plugins also run on KDE Plasma 6 as widgets: screen time, battery, "
                   "air raid alerts, the dGPU, Night Light, a status hub, emoji, dictation and a keyboard cleaner.")
    out = root / "plasma" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>On KDE Plasma · DuduPhudu</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{PAGE_URL}">
<meta name="author" content="DuduPhudu">
<meta name="theme-color" content="#F2F3F0" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0F1215" media="(prefers-color-scheme: dark)">
<meta property="og:site_name" content="DuduPhudu">
<meta property="og:type" content="website">
<meta property="og:title" content="On KDE Plasma — nine widgets from DuduPhudu">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{PAGE_URL}">
<meta property="og:image" content="https://duduphudu.app/assets/previews/plasma-hero.webp">
<meta property="og:image:width" content="1400">
<meta property="og:image:height" content="860">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>

<header class="nav">
  <a class="back" href="/#plugins"><span>&larr;</span> All plugins</a>
  <a class="brand" href="/">Dudu<span class="two">Phudu</span></a>
  <nav class="nav-links" aria-label="Sections">
    <a href="/#flagships">Flagships</a>
    <a href="/#plugins">Omarchy plugins</a>
    <a href="/#support">Support</a>
  </nav>
</header>

<main class="detail">

  <div class="detail-head">
    <p class="eyebrow">KDE Plasma 6</p>
    <h1>On Plasma too<span class="badge testing">In testing</span></h1>
    <p class="tagline">Nine of the Omarchy plugins, as Plasma widgets.</p>
    <p class="lede">The same work underneath: the same helpers, recorders and samplers, with a panel or tray widget in
    Plasma's own controls and colours on top. Where Plasma already does something well, they work with it instead of
    beside it: Dusk drives Plasma's Night Light, Reserve sits next to its battery widget. They are being tested on a
    real Plasma desktop now, and install from each repository's <code>plasma</code> branch until they are on the KDE
    Store.</p>
    <div class="actions">
      <button class="copy" type="button" data-copy="{esc(every)}">Copy: install all nine</button>
    </div>
  </div>

  <figure class="figure">
    <div class="shot">
      <img src="/assets/previews/plasma-hero.webp" alt="Hourglass open from the Plasma panel, showing an example day: time by hour, by category and by app, with Firefox's sites listed" width="1400" height="860">
    </div>
    <figcaption class="caption">Hourglass on Plasma 6, open from the panel, with an example day. The other eight sit beside it in the panel and the tray.</figcaption>
  </figure>

  <section aria-labelledby="widgets-h">
    <p class="eyebrow kicker">The widgets</p>
    <h2 id="widgets-h">What each one is on Plasma</h2>
    <div class="grid">
{chr(10).join(cards)}
    </div>
    <p class="note">After installing, right click the panel, choose Add or Manage Widgets, and drag the widget onto the
    panel or into the system tray. They need Plasma 6 on Wayland, Python 3 and, for some, <code>python-gobject</code>
    and <code>notify-send</code>; each page says which.</p>
  </section>

  <section aria-labelledby="typing-h">
    <p class="eyebrow kicker">Typing into other apps</p>
    <h2 id="typing-h">How the emoji picker and Mynah type on Plasma</h2>
    <p class="lede">Plasma does not let ordinary programs pretend to be a keyboard, which is how typing works on
    Omarchy. So on Plasma they do what a person would: the text goes onto the clipboard, paste is pressed through
    Plasma's own remote-input permission (Ctrl+Shift+V in a terminal, Ctrl+V elsewhere), and your clipboard is put back
    a moment later. Plasma asks once whether that is allowed; tick “Allow without asking next time” and it never asks
    again. Anything that passes through the clipboard appears in Plasma's clipboard history, so dictated text does
    too.</p>
  </section>

  <section aria-labelledby="stays-h">
    <p class="eyebrow kicker">Not on Plasma</p>
    <h2 id="stays-h">What stays on Omarchy, and why</h2>
    <ul class="only">
{stays}
    </ul>
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
""", encoding="utf-8")
