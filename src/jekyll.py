"""Export 017777.com as a compact Jekyll source tree for GitHub Pages' built-in Jekyll build.

python3 src/jekyll.py <out_dir>

Shared chrome lives once in _layouts/default.html; number pages are front matter rendered by
_layouts/number.html, so the repo stays small and GitHub Pages builds the HTML itself.
"""
import json, os, re, sys, math
sys.path.insert(0, os.path.dirname(__file__))
import layout as L
import pages_main, pages_biz, numbers_pages as NP

OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), ".."))


def w(rel, text):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)


def fm(d):
    return "---\n" + "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in d.items()) + "---\n"


def default_layout():
    nav = []
    for href, label in L.NAV:
        cond = f'page.url contains "{href}"' if href.endswith("/") else f'page.url == "{href}"'
        nav.append(f'<a href="{href}"{{% if {cond} %}} aria-current="page"{{% endif %}}>{label}</a>')
    nav.append('<a class="cta" href="/number-strategy.html">Get a strategy call</a>')
    url = L.SITE + "{{ page.url }}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{{{ page.title }}}}</title>
<meta name="description" content="{{{{ page.description }}}}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{{{{ page.robots | default: 'index, follow, max-image-preview:large' }}}}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{L.BRAND}">
<meta property="og:title" content="{{{{ page.title }}}}">
<meta property="og:description" content="{{{{ page.description }}}}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{L.SITE}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#14223D">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">
{L.ADS}
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebPage","name":{{{{ page.title | jsonify }}}},"description":{{{{ page.description | jsonify }}}},"url":"{url}","dateModified":"{L.UPDATED}","isPartOf":{{"@type":"WebSite","name":"{L.BRAND}","url":"{L.SITE}/"}}}}</script>
{{{{ page.ld }}}}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="owner-bar"><a href="{L.OWNER_URL}" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership</a></div>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="/" aria-label="017777 home"><span class="tiles"><b>01</b><b>7777</b></span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{''.join(nav)}<button class="theme-toggle" type="button" aria-label="Switch light or dark theme" title="Light / dark">◐</button></nav>
  </div>
</header>
<main id="main">{{{{ content }}}}</main>
{L.footer()}"""


NUMBER_LAYOUT = """---
layout: default
---
<section class="page-head"><div class="wrap"><p class="crumbs"><a href="/">Home</a> / <a href="/numbers/">Number meanings</a> / {{ page.s }}</p><h1>{{ page.s }}: meaning, maths and lucky-number lore</h1><p>The number {{ page.s }} decoded — its mathematics first, then what cultures and belief traditions say about it, and how businesses use it.</p></div></section>
<section class="block"><div class="wrap layout-side"><article class="prose">
<p class="muted" style="font-size:.92rem">By the 017777 editorial team · Last reviewed UPDATED · <a href="/editorial-policy.html">How we research</a></p>
<h2>The maths of {{ page.s }}</h2>
<p>{{ page.special }}</p>
<table><tr><th>Property</th><th>Value</th></tr>{% for r in page.rows %}<tr><td>{{ r[0] }}</td><td>{{ r[1] }}</td></tr>{% endfor %}</table>

<h2>{{ page.s }} across cultures</h2>
<ul>{% for d in page.digits %}{% assign g = site.data.digits[d] %}<li><strong>{{ d }} ({{ g.name }}):</strong> {{ g.culture }}</li>{% endfor %}</ul>

<h2>{{ page.s }} in business and commerce</h2>
<ul>{% for d in page.digits %}{% assign g = site.data.digits[d] %}<li>{{ g.commerce }}</li>{% endfor %}</ul>

<h2>{{ page.s }} as an “angel number” <span class="tag">Belief tradition</span></h2>
<p>Angel-number writers read {{ page.s }} as a message about {{ page.themes }}. Repeated digits are said to amplify the meaning of the base digit. Common moments people report seeing it: {{ page.clock }}.</p>
<div class="callout"><strong>What the evidence says:</strong> there is no scientific evidence that numbers carry messages. The experience is real, though: the frequency illusion makes recently noticed patterns seem to appear everywhere. Use these readings as prompts for reflection, not as guidance for money, health or safety decisions.</div>

{% capture q1 %}What does {{ page.s }} mean?{% endcapture %}{% capture a1 %}Mathematically, {{ page.value }} = {{ page.fx }}. In angel-number and numerology traditions, {{ page.s }} is read around {{ page.themes }}. Those readings are cultural beliefs, not predictions.{% endcapture %}{% capture q2 %}Is {{ page.s }} a lucky number?{% endcapture %}{% capture a2 %}It depends on culture. {{ site.data.digits[page.main].culture }}{% endcapture %}{% capture q3 %}Why do I keep seeing {{ page.s }}?{% endcapture %}{% capture a3 %}Psychologists point to the frequency illusion (Baader–Meinhof phenomenon): once a pattern is on your mind, you notice it more, and each match feels significant. Clocks, receipts and plates show repeating digits more often than people expect.{% endcapture %}
<h2>Questions</h2>
<details><summary>{{ q1 }}</summary><p>{{ a1 }}</p></details><details><summary>{{ q2 }}</summary><p>{{ a2 }}</p></details><details><summary>{{ q3 }}</summary><p>{{ a3 }}</p></details>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":{{ q1 | jsonify }},"acceptedAnswer":{"@type":"Answer","text":{{ a1 | jsonify }}}},{"@type":"Question","name":{{ q2 | jsonify }},"acceptedAnswer":{"@type":"Answer","text":{{ a2 | jsonify }}}},{"@type":"Question","name":{{ q3 | jsonify }},"acceptedAnswer":{"@type":"Answer","text":{{ a3 | jsonify }}}}]}</script>
</article>
<aside><div class="panel">
<h3>Decode any number</h3>
<form id="decoder-form" data-start="{{ page.s }}"><input style="width:100%;padding:10px;border-radius:6px;border:1px solid var(--line)" name="n" inputmode="numeric" aria-label="Number"><button class="btn" style="margin-top:8px;width:100%">Decode</button></form>
<div class="tool-out" id="decoder-out"></div>
<h3 style="margin-top:18px">Related numbers</h3><div class="kv">{% for x in page.rel %}<a href="/numbers/{{ x }}.html"><span>{{ x }}</span></a>{% endfor %}</div>
<p style="margin-top:14px"><a class="btn gold" href="/number-strategy.html">Own a {{ page.s }} domain or phone number?</a></p>
</div></aside>
</div></section>
""".replace("UPDATED", L.UPDATED)


def number_fm(s):
    n = int(s)
    digits = sorted(set(s))
    dsum = sum(map(int, s))
    D = NP.DIGIT
    rows = [["Value", f"{n:,}"], ["Prime?", "Yes" if NP.is_prime(n) else "No"], ["Prime factors", NP.factors(n)],
            ["Digit sum", f"{dsum}" + (" (divides the number: Harshad)" if dsum and n % dsum == 0 else "")],
            ["Digital root", str(NP.droot(dsum))], ["Binary", bin(n)[2:]], ["Hexadecimal", "0x" + format(n, "X")],
            ["Roman numerals", NP.roman(n)], ["Square root", f"{math.sqrt(n):.4f}"]]
    themes = ", ".join(D[d]["theme"] for d in digits)
    special = NP.SPECIAL.get(s, f"{n:,} is a repdigit — one digit repeated — so it equals {s[0]} × {'1' * len(s)}, and it shares every factor of {'1' * len(s)} ({NP.factors(int('1' * len(s)))}).")
    rel = [x for x in NP.NUMBERS if x != s and (x[0] == s[0] or len(x) == len(s))][:8]
    return {"layout": "number", "permalink": f"/numbers/{s}.html",
            "title": f"{s} Meaning: Maths, Angel Number, Luck & Business | 017777",
            "description": f"What {s} means: {n:,} = {NP.factors(n) if n > 1 else n}, its binary and Roman forms, what it means in Chinese, Japanese and Western culture, and the {s} angel number tradition explained.",
            "s": s, "special": special, "rows": rows, "digits": digits, "themes": themes,
            "clock": D[s[0]]["clock"] if len(digits) == 1 else "—", "rel": rel,
            "value": f"{n:,}", "fx": str(NP.factors(n) if n > 1 else n), "main": s[0] if len(digits) == 1 else "7" if s == "17777" else digits[-1]}


def split_page(html):
    title = re.search(r"<title>(.*?)</title>", html).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', html).group(1)
    robots = re.search(r'<meta name="robots" content="(.*?)">', html).group(1)
    scripts = re.findall(r'<script type="application/ld\+json">.*?</script>', html)[1:]  # first is the generic WebPage
    body = html[html.index('<main id="main">') + len('<main id="main">'):html.index("</main>")]
    d = {"layout": "default", "title": title, "description": desc}
    if robots.startswith("noindex"):
        d["robots"] = robots
    if scripts:
        d["ld"] = "".join(scripts)
    return d, body


def main():
    w("_layouts/default.html", default_layout())
    w("_layouts/number.html", NUMBER_LAYOUT)
    w("_data/digits.json", json.dumps({k: {"name": v["name"], "culture": v["culture"], "commerce": v["commerce"]} for k, v in NP.DIGIT.items()}, ensure_ascii=False, indent=1) + "\n")
    w("_config.yml", "title: 017777 Number Intelligence\nurl: https://017777.com\nmarkdown: kramdown\nexclude: [src, _preview, README.md, PROMPTS.md, \"*.py\"]\ninclude: [ads.txt]\n")

    pages = {**pages_main.PAGES, **pages_biz.PAGES}
    for name, fn in pages.items():
        d, body = split_page(fn())
        if name == "404.html":
            d["permalink"] = "/404.html"
        w(name, fm(d) + body)
    # numbers index + sitemap.html from the full build
    d, body = split_page(NP.index_page())
    w("numbers/index.html", fm(d) + body)
    for s in NP.NUMBERS:
        w(f"numbers/{s}.html", fm(number_fm(s)))
    sm = os.path.join(os.path.dirname(__file__), "..", "_preview", "sitemap.html")  # produced by build.py
    d, body = split_page(open(sm, encoding="utf-8").read())
    w("sitemap.html", fm(d) + body)
    print("Jekyll tree written to", OUT)


if __name__ == "__main__":
    main()
