# 017777.com — Number Intelligence Hub

Free number decoder, number-meanings library and research on numbers in commerce, AI, the economy and culture. Static site for GitHub Pages (free plan).

## Structure
- `index.html`, pillar pages, tools, lead-gen (`number-strategy.html`), support, contests, careers, advertise, legal pages — Jekyll sources (front matter + page body)
- `_layouts/default.html` — shared head (AdSense, SEO, schema), owner bar, header and footer for every page
- `_layouts/number.html` + `_data/digits.json` — renders the `numbers/` library from front matter
- `numbers/` — number-meanings library (30 pages)
- `assets/css/site.css` — design system (light/dark)
- `assets/js/config.js` — site settings: payment links, AdSense client, encoded form key
- `assets/js/numbers.js` — number engine and tools
- `assets/js/main.js` — nav, theme, forms, video facades, hero board
- `src/` — Python sources that generate all pages (`build.py` renders a plain-HTML preview, `jekyll.py` writes the Jekyll sources)

## Edit and rebuild
GitHub Pages builds the site with its built-in Jekyll on every push — no Actions needed. To change content, edit `src/` and regenerate:
```
python3 src/build.py      # plain-HTML preview in _preview/ + sitemap.xml
python3 src/jekyll.py     # rewrites the Jekyll page sources in the repo root
```
Add number pages by extending `NUMBERS` and `SPECIAL` in `src/numbers_pages.py`.

## Turn on instant donations
Paste PayPal / Stripe / Buy Me a Coffee / Ko-fi URLs into `payments` in `assets/js/config.js`. Buttons appear automatically; otherwise the page collects pledges.

## Forms
All forms post through FormSubmit to the site inbox. The address is stored encoded and is never shown on the site. The first submission triggers a one-time activation email from FormSubmit — confirm it once.

## Hosting
GitHub Pages → Settings → Pages → Deploy from branch `main`, folder `/ (root)`. Custom domain `017777.com` (see `CNAME`). DNS: A records 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153; `www` CNAME → webworksa1.github.io.

See `PROMPTS.md` for the research, concept, benchmark and phase-wise build prompts.

© 017777.com. “017777” is used only as a domain name; not affiliated with any telephone operator, dialling area, lottery or company using the same digits.
