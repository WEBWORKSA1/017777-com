"""Render every page as plain HTML into _preview/ (for local review) and write sitemap.xml at the repo root.

python3 src/build.py && python3 src/jekyll.py   # then commit the regenerated Jekyll sources
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import page, page_head, SITE, UPDATED
import pages_main, pages_biz, numbers_pages

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ROOT = os.path.join(REPO, "_preview")


def write(rel, html):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    out = {}
    for name, fn in {**pages_main.PAGES, **pages_biz.PAGES}.items():
        out[name] = fn()
    out.update(numbers_pages.build_all())

    # HTML sitemap
    groups = [
        ("Explore", [("/", "Home"), ("/tools.html", "Number decoder & tools"), ("/meaning-of-017777.html", "What 017777 means"),
                     ("/commerce.html", "Numbers in commerce"), ("/ai-economy.html", "Numbers in AI & the economy"),
                     ("/culture.html", "Lucky numbers by culture"), ("/videos.html", "Videos"), ("/numbers/", "Number meanings")]),
        ("Number pages", [(f"/numbers/{n}.html", n) for n in numbers_pages.NUMBERS]),
        ("Get involved", [("/number-strategy.html", "Strategy call"), ("/support.html", "Support"), ("/contests.html", "Contests"),
                          ("/careers.html", "Careers"), ("/advertise.html", "Advertise")]),
        ("About & legal", [("/about.html", "About"), ("/contact.html", "Contact"), ("/editorial-policy.html", "Editorial policy"),
                           ("/privacy.html", "Privacy"), ("/terms.html", "Terms"), ("/disclaimer.html", "Disclaimer & trademark notice")]),
    ]
    body = page_head("Sitemap", "Every page on 017777.com.", [("/sitemap.html", "Sitemap")]) + '<section class="block"><div class="wrap grid g4">' + "".join(
        f'<div><h2 style="font-size:1.2rem">{t}</h2><ul>' + "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in links) + "</ul></div>" for t, links in groups) + "</div></section>"
    out["sitemap.html"] = page("/sitemap.html", "Sitemap | 017777", "All pages on 017777.com.", body)

    for rel, html in out.items():
        write(rel, html)

    # XML sitemap (skip noindex pages)
    urls = []
    for rel in sorted(out):
        if rel in ("thank-you.html", "404.html"):
            continue
        loc = "/" if rel == "index.html" else "/" + rel.replace("index.html", "")
        pr = "1.0" if loc == "/" else "0.8" if rel in ("tools.html", "meaning-of-017777.html", "numbers/index.html", "number-strategy.html") else "0.6"
        urls.append(f"  <url><loc>{SITE}{loc}</loc><lastmod>{UPDATED}</lastmod><priority>{pr}</priority></url>")
    with open(os.path.join(REPO, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    print(f"Built {len(out)} pages, {len(urls)} URLs in sitemap.xml")


if __name__ == "__main__":
    main()
