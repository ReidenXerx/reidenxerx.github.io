"""What each plugin page says.

Written from each plugin's own README so the pages stay true to what the thing
actually does. `only` is the part that matters: what no alternative does.
"""

SITE = "https://duduphudu.app"

PLUGINS = [
    {
        "slug": "varta",
        "name": "Varta",
        "eyebrow": "Air raid alerts · Bar and screen",
        "badge": ("new", "New"),
        "tagline": "An air raid alert watch that says when it has gone blind.",
        "lede": "Your oblast in the bar, and a band across every screen the moment it goes under "
                "alert — built for the case where you are at the desk in headphones.",
        "only": [
            ("It tells you when it has stopped watching.",
             "A monitor that cannot reach its source looks exactly like one reporting calm: the same quiet "
             "shield, the same silence. That is the failure that gets somebody hurt, so “not watching” is "
             "drawn in the warning colour and struck through, never greyed out and quietly forgotten."),
            ("It notices a feed that has frozen, not just one that has stopped answering.",
             "Staleness is timed separately from the request succeeding, so a source still returning a "
             "cheerful 200 over a reading from an hour ago is caught. One really was, during development."),
            ("It does not cry wolf.",
             "A watcher restarting after a settings change says “reconnecting”, not “not watching”, and "
             "closing the lid is recognised as sleep rather than an outage. A warning that fires when "
             "nothing is wrong stops being believed."),
            ("Other oblasts are news, not alarm.",
             "Watch where your family live: it shows in the bar and sounds once, quietly, and never puts "
             "the band across your screen. Only where you are does that."),
            ("The rehearsal is unmistakably a rehearsal.",
             "It runs the whole path — band, sound, repeat — marked ТЕСТ throughout, because a drill "
             "nobody can tell from the real thing is its own kind of harm."),
        ],
        "use": [
            ("Click the shield", "Everything it knows, and everything you can do about it"),
            ("Tick a region, Save", "Watch somewhere else as well as where you are"),
            ("Find my region", "Detect your oblast again, from two sources that must agree"),
            ("Test the alert", "Rehearse the whole thing, clearly marked"),
            ("The × on the band", "Put it away for this alert, not for good"),
        ],
        "notes": "Unofficial, and oblast-wide: a companion to the official app and to the sirens outside, "
                 "never a replacement. It reads one public feed once a minute and writes nothing but its "
                 "own entry in your shell config. Needs paplay for the sound; nothing else.",
        "repo": "https://github.com/ReidenXerx/omarchy-varta",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-varta.git --enable",
        "preview": "assets/previews/varta.webp",
        "licence": "MIT",
    },
    {
        "slug": "aerial",
        "name": "Aerial",
        "eyebrow": "Window overview · Touchpad",
        "badge": ("new", "New"),
        "tagline": "Mission Control for Omarchy, attached to your fingers.",
        "lede": "Swipe up with three fingers and every window on the workspace spreads out, live, "
                "with your desktops along the top. Let go half way and it goes back.",
        "only": [
            ("It follows your hand, frame by frame.",
             "The swipe is not a trigger that plays an animation. Hyprland reports it continuously, so the "
             "overview is drawn at whatever fraction of the way your fingers have got to — stop half way and "
             "it stays there; swipe back and it never opened."),
            ("The thumbnails are the windows.",
             "Each one is a real capture, so a video keeps playing and a build keeps scrolling while you look "
             "for it. Eight windows cost about 6% of one core."),
            ("Type to narrow the spread.",
             "Start typing and what does not match steps out, growing what is left. When one window is "
             "standing, enter goes there."),
            ("Drag a window where it belongs.",
             "Drop it on a desktop to send it there, or on another window to trade places in the tiling "
             "layout. Workspaces one to five are always offered, so you can aim at one before it exists."),
            ("Nothing to install into the compositor.",
             "No Hyprland plugin to rebuild every time Hyprland updates: the gesture is registered through "
             "Hyprland 0.56's own Lua API."),
        ],
        "use": [
            ("Three fingers up", "Open this workspace, following your fingers"),
            ("Four fingers up", "Open every window you have, grouped by workspace"),
            ("Three or four fingers down", "Close again"),
            ("SUPER + A", "Open or close from the keyboard"),
            ("Type anything", "Narrow the spread; enter goes to what is left"),
            ("Drag a window", "Onto a desktop to send it, onto a window to swap them"),
            ("Middle-click, or the ×", "Close that window"),
        ],
        "notes": "Needs Hyprland 0.56 or newer for the Lua gesture API, and a touchpad for the part that "
                 "makes it worth having. It writes no files and keeps no state; the gestures exist only "
                 "while the plugin is loaded and go away with it.",
        "repo": "https://github.com/ReidenXerx/omarchy-aerial",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-aerial --enable",
        "preview": "assets/previews/aerial.webp",
        "licence": "MIT",
    },
    {
        "slug": "omagram",
        "name": "Omagram",
        "eyebrow": "Telegram client · Bar and window",
        "badge": ("review", "In review"),
        "tagline": "The unofficial Telegram client that lives in your bar, not in another window.",
        "lede": "Reply from the bar without leaving what you were doing, with your theme's colours and the "
                "keyboard first everywhere.",
        "only": [
            ("Answer from the bar.",
             "The quick view opens under Omagram's mark, or over everything on a key — so a reply does not "
             "cost you the window you were in."),
            ("Know who wrote without looking.",
             "Every person can have a notification sound of their own, so you learn who it is before you "
             "have turned your head."),
            ("Notifications that do the work.",
             "One per chat, carrying the photo, sticker or video that came in, and you can read, mute or "
             "react without opening anything."),
            ("Emoji by name, in three languages.",
             "The emoji panel finds emoji, symbols and kaomoji by their English, Ukrainian or Russian names "
             "at once."),
        ],
        "use": [],
        "notes": "Unofficial, and not affiliated with or endorsed by Telegram. Your session stays on your "
                 "machine.",
        "repo": "https://github.com/ReidenXerx/omarchy-omagram",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-omagram.git --enable",
        "preview": "assets/previews/omagram.webp",
        "licence": "MIT",
    },
    {
        "slug": "cockpit",
        "listing": "reidenxerx.cockpit",
        "name": "Cockpit",
        "eyebrow": "Status hub · Bar widget",
        "badge": ("listed", "On the marketplace"),
        "tagline": "What your machine is doing right now, in one dropdown.",
        "lede": "One hub for the things you would otherwise switch workspaces to find out: which AI sessions "
                "are working, which are waiting for you, and on what.",
        "only": [
            ("Agent sessions, working or waiting.",
             "See at a glance which sessions need you, and which are still thinking."),
            ("The chat you closed an hour ago, back in a terminal.",
             "One click resumes it where it was, instead of hunting for the session."),
            ("Transfers, long jobs, repos and updates.",
             "File transfers with real progress, and the state of the things you are waiting on."),
            ("Add your own section with one script.",
             "Anything that prints can become a row, so the hub covers what your machine actually does."),
        ],
        "use": [],
        "notes": "A bar widget: it needs a place on the bar to stay loaded.",
        "repo": "https://github.com/ReidenXerx/omarchy-cockpit",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-cockpit.git --enable",
        "preview": "assets/previews/cockpit.webp",
        "licence": "MIT",
    },
    {
        "slug": "tactile",
        "listing": "reidenxerx.tactile",
        "name": "Tactile",
        "eyebrow": "Input tuning · Touchpad and mouse",
        "badge": ("listed", "On the marketplace"),
        "tagline": "Tune your touchpad and mouse by feel, and never get stuck with a bad setting.",
        "lede": "Every touchpad and mouse Hyprland reports gets its own tab, with a feel lab beside the "
                "settings so you can try each change the moment you make it.",
        "only": [
            ("Every change undoes itself unless you keep it.",
             "A change applies at once and a countdown puts it back after fifteen seconds, so a setting that "
             "makes the pointer unusable cannot strand you."),
            ("A feel lab next to the settings.",
             "Scroll a ruler that measures each swipe, and see which button a tap or a press actually sends."),
            ("Draw your own acceleration.",
             "Pick Custom and drag the points of the curve, or start from one of the named shapes."),
            ("Gestures with a map of what your fingers do.",
             "Add swipes and pinches, with an opt-in live view that draws each finger where it lands, at the "
             "pad's real size."),
            ("Your Hyprland config stays yours.",
             "Tactile applies its settings while Hyprland runs; it does not rewrite your config behind you."),
        ],
        "use": [("SUPER + ALT + T", "Open Tactile"),
                ("Omarchy menu", "Setup → Touchpad & mouse")],
        "notes": "",
        "repo": "https://github.com/ReidenXerx/omarchy-tactile",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-tactile.git --enable",
        "preview": "assets/previews/tactile.webp",
        "licence": "MIT",
    },
    {
        "slug": "barber",
        "listing": "reidenxerx.barber",
        "name": "Barber",
        "eyebrow": "Bar editor · Layouts",
        "badge": ("listed", "On the marketplace"),
        "tagline": "Edit the Omarchy bar on the bar itself.",
        "lede": "Every widget gets a frame. Pick one, move it, take it off, add a new one next to it, or "
                "change its settings right where it sits.",
        "only": [
            ("Edit where the widgets are.",
             "No list of ids in a settings window: the frames sit over the real widgets, so you are moving "
             "the thing you are looking at."),
            ("Undo and redo for every change.",
             "Even a widget you took off comes back in the same place, with its options."),
            ("Layouts that switch by themselves.",
             "Save the bar as a layout — Docked, Battery, Presenting — and add rules for when each applies."),
            ("Scriptable.",
             "Save and switch layouts from a key binding or a script."),
        ],
        "use": [("SUPER + ALT + B", "Edit on the bar"),
                ("Omarchy menu", "Style → Menu Bar → Edit on the bar")],
        "notes": "",
        "repo": "https://github.com/ReidenXerx/omarchy-barber",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-barber.git --enable",
        "preview": "assets/previews/barber.webp",
        "licence": "MIT",
    },
    {
        "slug": "emoji-picker",
        "listing": "reidenxerx.emoji-picker",
        "name": "Emoji picker",
        "eyebrow": "Overlay · Emoji, symbols, GIFs",
        "badge": ("listed", "On the marketplace"),
        "tagline": "Emoji, symbols, kaomoji and GIFs, typed straight into what you were using.",
        "lede": "Whatever you pick is typed into the app you came from, so there is no copy, no switch and "
                "no paste.",
        "only": [
            ("Search in three languages at once.",
             "English, Ukrainian and Russian names all match, so heart, серце and сердце find the same "
             "thing."),
            ("Typed, not copied.",
             "The pick lands in the window you were in, rather than on your clipboard."),
            ("Kaomoji and symbols too.",
             "Not only emoji: the arrows, marks and faces you would otherwise go looking for."),
            ("GIFs in the same place.",
             "Search and send without opening a browser tab."),
        ],
        "use": [],
        "notes": "",
        "repo": "https://github.com/ReidenXerx/omarchy-emoji-picker",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-emoji-picker.git --enable",
        "preview": "assets/previews/emoji-picker.webp",
        "licence": "MIT",
    },
    {
        "slug": "clipboard-shelf",
        "listing": "reidenxerx.clipboard-shelf",
        "name": "Clipboard shelf",
        "eyebrow": "Clipboard · Bar widget",
        "badge": ("listed", "On the marketplace"),
        "tagline": "Pin the snippets you paste all day, one keystroke away.",
        "lede": "Omarchy's built-in clipboard is a search-only overlay and everything ages out of it. The "
                "shelf keeps what you actually reuse.",
        "only": [
            ("Pinned snippets that do not age out.",
             "The address, the command, the block of boilerplate — kept where you can reach them, beside "
             "your ordinary history."),
            ("Rows tell you what they hold.",
             "A colour, a path, a URL and a block of text each look like themselves, so you pick by sight."),
            ("It captures nothing itself.",
             "The shelf reads the history Omarchy already records, rather than watching your clipboard."),
            ("Password managers are already filtered.",
             "Entries marked sensitive are skipped by that capture."),
        ],
        "use": [],
        "notes": "Leave omarchy.clipboard enabled — disable it and history stops being recorded.",
        "repo": "https://github.com/ReidenXerx/omarchy-clipboard-shelf",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-clipboard-shelf.git --enable",
        "preview": "assets/previews/clipboard-shelf.webp",
        "licence": "MIT",
    },
    {
        "slug": "omalang",
        "listing": "reidenxerx.keyboard-layout-per-app",
        "name": "Omalang",
        "eyebrow": "Keyboard layout · Bar widget",
        "badge": ("listed", "On the marketplace"),
        "tagline": "Remembers the keyboard layout per application, and puts it back.",
        "lede": "Focus your terminal and get the layout you write commands in; focus the chat and get the "
                "one you write to people in.",
        "only": [
            ("Per application, not per window.",
             "The layout you chose in an app is the layout you get the next time you are in it."),
            ("It understands how Hyprland really reports layouts.",
             "Layout is tracked per input device, and an input method adds one of its own — switching them "
             "one at a time is what makes other approaches drift a layout out of step."),
            ("It does not mistake its own changes for yours.",
             "Applying a layout, a keymap recompile and a hotplugged keyboard all look alike on the socket; "
             "Omalang tells them apart before recording anything."),
        ],
        "use": [],
        "notes": "It used to be called Keyboard layout per app.",
        "repo": "https://github.com/ReidenXerx/omarchy-omalang",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-omalang.git --enable",
        "preview": "assets/previews/omalang.webp",
        "licence": "MIT",
    },
    {
        "slug": "tile-blueprints",
        "listing": "reidenxerx.tile-blueprints",
        "name": "Tile blueprints",
        "eyebrow": "Tiling · Per-workspace layouts",
        "badge": ("listed", "On the marketplace"),
        "tagline": "Draw the tiles for a workspace, and your apps open straight into them.",
        "lede": "Say which app lives in each tile at the proportions you set, and from then on the workspace "
                "builds itself.",
        "only": [
            ("Draw it, do not configure it.",
             "Drag the tiles into the shape you want instead of writing window rules."),
            ("A snapshot remembers more than the grid.",
             "Which app sits in which tile and at what proportions, windows that share a tile, floating "
             "windows and whether they were pinned, and anything you left fullscreen."),
            ("Per workspace.",
             "Your writing desktop and your build desktop can have completely different shapes."),
        ],
        "use": [("SUPER + ALT + SHIFT + L", "Snapshot the current workspace as a blueprint")],
        "notes": "",
        "repo": "https://github.com/ReidenXerx/omarchy-tile-blueprints",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-tile-blueprints.git --enable",
        "preview": "assets/previews/tile-blueprints.webp",
        "licence": "MIT",
    },
    {
        "slug": "idle-dim",
        "listing": "reidenxerx.idle-dim",
        "name": "Idle dim",
        "eyebrow": "Power · Bar widget",
        "badge": ("listed", "On the marketplace"),
        "tagline": "Dims the screen when you stop, and gives back the brightness you had.",
        "lede": "Stock Omarchy has no dim step: its idle service knows screensaver, lock and sleep, and "
                "nothing gentler.",
        "only": [
            ("The step that was missing.",
             "A dim before the screensaver, so the machine tells you it is about to go rather than going."),
            ("It gives your brightness back.",
             "The level you were on is restored on any input, after a sleep, and when the widget starts."),
            ("It drives the same backlight your keys do.",
             "Not an overlay that paints the screen darker: the actual backlight Omarchy's brightness keys "
             "control."),
        ],
        "use": [],
        "notes": "",
        "repo": "https://github.com/ReidenXerx/omarchy-idle-dim",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-idle-dim.git --enable",
        "preview": "assets/previews/idle-dim.webp",
        "licence": "MIT",
    },
    {
        "slug": "keyboard-cleaner",
        "listing": "reidenxerx.keyboard-cleaner",
        "name": "Keyboard cleaner",
        "eyebrow": "Utility · Full-screen",
        "badge": ("listed", "On the marketplace"),
        "tagline": "Switches every key off while you wipe the keyboard.",
        "lede": "A full-screen card in your theme counts down while you clean. Hold a click on the ring for "
                "three seconds to end it early.",
        "only": [
            ("Every key is off.",
             "Letters, Super shortcuts, media, brightness and power keys — not a screensaver you can type "
             "through."),
            ("The touchpad and mouse do nothing.",
             "Clicks, scrolls and drags land on the card instead of on your work."),
            ("The display stays awake.",
             "The card shows on every monitor with the time left, so you can see what you are doing."),
        ],
        "use": [],
        "notes": "",
        "repo": "https://github.com/ReidenXerx/omarchy-keyboard-cleaner",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-keyboard-cleaner.git --enable",
        "preview": "assets/previews/keyboard-cleaner.webp",
        "licence": "MIT",
    },
    {
        "slug": "dgpu-status",
        "listing": "reidenxerx.dgpu-status",
        "name": "dGPU status",
        "eyebrow": "Hardware · Bar widget",
        "badge": ("listed", "On the marketplace"),
        "tagline": "Whether the discrete GPU is asleep or awake, and what woke it.",
        "lede": "A laptop with an NVIDIA card spends its battery on whatever quietly keeps that card awake. "
                "This tells you which it is.",
        "only": [
            ("Asleep or awake, at a glance.",
             "On the bar, where you will actually notice it."),
            ("gpuwho names the culprit.",
             "A read-only CLI for seeing what is holding the card open — often something you did not know "
             "was asking."),
            ("It does not wake the card to check.",
             "A status widget that polls the GPU is the reason the GPU is awake; this one avoids that."),
        ],
        "use": [("gpuwho", "See what is keeping the discrete GPU awake")],
        "notes": "For laptops with an NVIDIA discrete GPU.",
        "repo": "https://github.com/ReidenXerx/omarchy-dgpu-status",
        "install": "omarchy plugin add https://github.com/ReidenXerx/omarchy-dgpu-status.git --enable",
        "preview": "assets/previews/dgpu-status.webp",
        "licence": "MIT",
    },
]
