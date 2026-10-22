"""Shared layout for 017777.com static pages."""
import json

SITE = "https://017777.com"
BRAND = "017777 Number Intelligence"
ADS = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
OWNER_URL = "https://web.works/contact"
UPDATED = "2026-10-22"

NAV = [
    ("/tools.html", "Tools"),
    ("/meaning-of-017777.html", "017777"),
    ("/numbers/", "Number meanings"),
    ("/commerce.html", "Commerce"),
    ("/ai-economy.html", "AI & economy"),
    ("/culture.html", "Culture"),
    ("/contests.html", "Contests"),
    ("/support.html", "Support"),
]


def head(title, desc, path, extra_ld=None):
    canonical = SITE + path
    ld = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": desc,
        "url": canonical,
        "dateModified": UPDATED,
        "isPartOf": {"@type": "WebSite", "name": BRAND, "url": SITE + "/"},
    }
    lds = [ld] + (extra_ld or [])
    ld_html = "".join('<script type="application/ld+json">%s</script>' % json.dumps(x) for x in lds)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#14223D">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">
{ADS}
{ld_html}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="owner-bar"><a href="{OWNER_URL}" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership</a></div>
"""


def header(path):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if (href == path or (href != "/" and path.startswith(href.rstrip("/")) and href.endswith("/"))) else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    links.append('<a class="cta" href="/number-strategy.html">Get a strategy call</a>')
    return f"""<header class="site-head">
  <div class="wrap">
    <a class="brand" href="/" aria-label="017777 home"><span class="tiles"><b>01</b><b>7777</b></span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{''.join(links)}<button class="theme-toggle" type="button" aria-label="Switch light or dark theme" title="Light / dark">◐</button></nav>
  </div>
</header>
"""


def footer():
    return f"""<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="/"><span class="tiles"><b>01</b><b>7777</b></span></a>
        <p style="margin-top:12px">Free number tools and plain-language research on how numbers shape prices, technology, the economy and everyday belief.</p>
        <form class="newsletter" data-relay="Newsletter" aria-label="Newsletter signup">
          <label class="hp">Leave empty <input name="_hp" tabindex="-1" autocomplete="off"></label>
          <input type="email" name="email" required placeholder="Your email" aria-label="Email address">
          <button class="btn gold" type="submit">Subscribe</button>
          <p class="form-status" role="status"></p>
        </form>
        <p class="form-note" style="color:#93A1BD">One email a week: a number decoded, a tool tip, contest news. Unsubscribe any time.</p>
      </div>
      <div><h4>Explore</h4><ul>
        <li><a href="/tools.html">Number decoder & tools</a></li>
        <li><a href="/numbers/">Number meanings A–Z</a></li>
        <li><a href="/meaning-of-017777.html">What 017777 means</a></li>
        <li><a href="/commerce.html">Numbers in commerce</a></li>
        <li><a href="/ai-economy.html">Numbers in AI & the economy</a></li>
        <li><a href="/culture.html">Lucky numbers by culture</a></li>
        <li><a href="/videos.html">Videos</a></li>
      </ul></div>
      <div><h4>Get involved</h4><ul>
        <li><a href="/number-strategy.html">Number strategy call</a></li>
        <li><a href="/support.html">Support the project</a></li>
        <li><a href="/contests.html">Contests & prizes</a></li>
        <li><a href="/careers.html">Careers & contributors</a></li>
        <li><a href="/advertise.html">Advertise & sponsor</a></li>
        <li><a href="{OWNER_URL}" target="_blank" rel="noopener">Buy or partner on this domain</a></li>
      </ul></div>
      <div><h4>About & legal</h4><ul>
        <li><a href="/about.html">About</a></li>
        <li><a href="/contact.html">Contact</a></li>
        <li><a href="/editorial-policy.html">Editorial policy</a></li>
        <li><a href="/privacy.html">Privacy policy</a></li>
        <li><a href="/terms.html">Terms of use</a></li>
        <li><a href="/disclaimer.html">Disclaimer & trademark notice</a></li>
        <li><a href="/sitemap.html">Sitemap</a></li>
      </ul></div>
    </div>
    <div class="foot-legal">
      <p>© <span class="year">2026</span> 017777.com. Original text and tools on this site are copyright 017777.com. “017777” is used here only as a domain name and site identifier; it is not a registered trademark of this site, and this site is not affiliated with any telephone operator, area code, lottery, government body or company that uses the same digits. Numerology and “angel number” content is presented as cultural tradition and entertainment, not as prediction or professional advice. See the <a href="/disclaimer.html">full disclaimer and trademark notice</a>.</p>
      <p>This site is funded by advertising (Google AdSense), reader support and sponsorships. Advertisements are labelled and kept separate from editorial content.</p>
    </div>
  </div>
</footer>
<div class="cookie" role="dialog" aria-label="Cookie notice">
  <p style="margin:0">We use cookies for basic site features and, with Google AdSense, to show and measure ads. See our <a href="/privacy.html">privacy policy</a>.</p>
  <div class="btn-row"><button class="btn" data-ck="all" type="button">Accept</button><button class="btn ghost" data-ck="essential" type="button">Essential only</button></div>
</div>
<a class="btn gold sticky-cta" href="/number-strategy.html">Strategy call</a>
<script src="/assets/js/config.js"></script>
<script src="/assets/js/numbers.js"></script>
<script src="/assets/js/main.js"></script>
</body>
</html>
"""


def page_head(title, intro, crumbs=None):
    c = ""
    if crumbs:
        c = '<p class="crumbs"><a href="/">Home</a> / ' + " / ".join(
            f'<a href="{h}">{t}</a>' if h else t for h, t in crumbs) + "</p>"
    return f"""<section class="page-head"><div class="wrap">{c}<h1>{title}</h1><p>{intro}</p></div></section>"""


def page(path, title, desc, body, extra_ld=None):
    return head(title, desc, path, extra_ld) + header(path) + '<main id="main">' + body + "</main>" + footer()


def byline():
    return f'<p class="muted" style="font-size:.92rem">By the 017777 editorial team · Last reviewed {UPDATED} · <a href="/editorial-policy.html">How we research</a></p>'


def faq_ld(pairs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}


def faq_html(pairs):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in pairs)


def honeypot():
    return '<label class="hp">Leave this empty <input name="_hp" tabindex="-1" autocomplete="off"></label>'


def consent(text="I agree that 017777.com may contact me about this request. See the privacy policy."):
    return f'<label class="check"><input type="checkbox" name="consent" value="yes" required> {text}</label>'


def video(vid, title, note=""):
    n = f'<p class="muted" style="margin-top:8px;font-size:.92rem"><strong>{title}</strong>{(" — " + note) if note else ""}</p>'
    return f'<div><div class="video" data-id="{vid}" data-title="{title}"></div>{n}</div>'
