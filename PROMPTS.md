# 017777.com — Research, concept and phase-wise build prompts

## 1. Research summary: what "017777" means

| Lens | Finding | Use on the site |
|---|---|---|
| Maths | 017777 = 17,777 = 29 × 613. Digit sum 29 divides it (Harshad number). Binary 100010101110001, hex 0x4571. | Hero facts, decoder, contest puzzle |
| AI / computing | "01" = binary, the base layer of every model (tokens → integer IDs → numeric weights). | AI & economy pillar |
| Telephony (UK) | 01777 = Ofcom dialling code for Retford, Nottinghamshire (was 0777 until 1995). | Prefix notes, disclaimer of non-affiliation |
| Telephony (Korea) | 017 = Shinsegi Telecom → SK Telecom legacy mobile prefix; unified to 010 from 2004; SKT 2G shut 2020. 017 once carried a "power" image. | Culture + commerce stories |
| Commerce | 7-ending prices are a marketing habit; 9-endings have stronger evidence. Lucky price endings raise intent among superstitious / stressed buyers (Chen et al. 2022, n=450). Localised superstitious pricing improves brand attitude in Singapore. | Charm-price tool, commerce guide, strategy-call leads |
| Economy | Rule of 72: 7% doubles in ~10.3 yrs (exact 10.24). | Rule of 72 tool |
| People / culture | 7 = Western luck (777 jackpot), Japan's Seven Lucky Gods; mixed in Chinese (Qixi vs Ghost Month); 8 prized, 4 avoided in East Asia. Angel-number "7777" queries are a large evergreen search category. | Number-meanings library (traffic engine) |

## 2. The decision: Number Intelligence Hub

**Why this beats the alternatives**
- *Angel-number blog only*: huge traffic, low RPM ($1–4), thin-content risk at AdSense review. Rejected as the whole site; kept as the traffic layer.
- *Phone/area-code lookup*: needs live data and scam reports; the 01777 angle is too local.
- *Hub = tools + number library + commerce/AI/economy research + lead gen*: tools earn repeat visits and backlinks, number pages capture evergreen search, commerce/finance pages lift RPM ($8–20), and the strategy-call form monetises high-intent visitors (numeric domains, vanity numbers, pricing).

**Revenue model (planning assumptions, month 12)**

| Stream | Assumption | Monthly |
|---|---|---|
| AdSense | 150k pageviews × blended $5 RPM | ~$750 |
| Strategy-call leads | 0.3% of 50k tool users = 150 leads × 5% close × $500 avg | ~$3,750 |
| Sponsorships | 1–2 tool/newsletter sponsors | $300–1,500 |
| Reader support | 0.05% of visitors × $15 avg | ~$100 |

Leads, not ads, are the profit centre. Ads pay hosting and content; the form pays for growth.

## 3. Benchmark — 25 sites studied

numerology.com, Sacred Scribes, angelnumber.org, astrology.com, number.academy, mathsisfun.com, calculator.net, omnicalculator.com, rapidtables.com, wolframalpha.com, timeanddate.com, area-codes.org.uk, whosringing.co.uk, numberbarn.com, phonespell.org, dnjournal.com, sedo.com, ourworldindata.org, ko-fi.com, buymeacoffee.com, gleam.io, areacodelocations.info, calculatorsoup.com, affinitynumerology.com, thecalculatorsite.com.

**Adopted:** search/tool-first hero (Wolfram, NumberBarn, phonespell); page-per-number with maths + culture + belief separated (number.academy); belief labelled "entertainment" + named policy pages (Sacred Scribes, affinity); category grids and footer index (calculator.net, OWID); "how it works" 3 steps and buyer/seller split (Sedo); preset-amount tip jar (BMC/Ko-fi); free-entry contests with official rules (Gleam); sourced claims + editorial policy + last-reviewed dates (OWID, Omni, calculatorsoup); labelled ads and stated funding model (whosringing, thecalculatorsite).
**Avoided:** thin template pages with no About/authors (angelnumber.org, areacodelocations).

## 4. Phase-wise build prompts

### Phase 1 — Foundation and design system
> Build a static, dependency-free website for 017777.com hostable on GitHub Pages (free plan). Plain HTML/CSS/JS with GitHub Pages' built-in Jekyll: one `_layouts/default.html` holds the head, header and footer for every page, and a small Python generator (`src/`) writes the page sources. Design tokens: ink #14223D, paper #F5F7FA, jackpot yellow #F4C430, teal #0F766E, rose #BE3455; Bricolage Grotesque (display) + Atkinson Hyperlegible (body); left-aligned, 72ch text columns; light/dark themes; responsive to 360px; visible focus; reduced-motion support. On every page, above the header, show the bar "Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership" linking to https://web.works/contact. Add the AdSense script `ca-pub-6620975821265271` in every `<head>`, `ads.txt`, `robots.txt`, `sitemap.xml`, `CNAME`, `_config.yml`, favicon, OG image and web manifest.

### Phase 2 — Signature interaction and tools
> Create a hero split-flap board that shows 01 7777 and flips once on load; a number input re-flips the board and shows digit sum, prime factors and binary. Build `numbers.js` with BigInt analysis (primality to 10¹², factoring, digit sum, digital root with master numbers, binary/hex/octal/Roman, repdigit/palindrome/run patterns, keypad letters, prefix notes for 01777/017/011/010/00/0/1/7, cultural notes per digit, a labelled belief reading). Tools page: decoder, charm-price calculator with margin, Rule of 72 (estimate vs exact), memorability score, Pythagorean name numerology + life path, seeded lucky-number picker with honest odds note, base converter, phone-word dialler. Everything runs client-side; nothing typed is stored.

### Phase 3 — Content for traffic and AdSense approval
> Write original, sourced pillar pages: "What does 017777 mean?", Numbers in commerce, Numbers in AI & the economy, Lucky numbers by culture (comparison table), Videos (YouTube facades, privacy-enhanced embeds, load on click). Generate a number-meanings library (7, 11, 22, 33, 77, 88, 000–999, 0000–9999, 1212, 1234, 1717, 17777) where each page has computed maths, a unique fact, culture, business use, a labelled belief section with the frequency-illusion explanation, FAQ schema and related numbers. Add About, Contact, Editorial policy, Privacy (AdSense cookie language + opt-out links), Terms, Disclaimer & trademark notice, HTML sitemap, 404 and noindex thank-you page. No placeholder text, no copied passages, quotes under 15 words.

### Phase 4 — Lead generation (the profit engine)
> Build `/number-strategy.html`: a three-step form with progress bar (goal → asset, budget, timeline → contact + consent), choice cards for buy/sell numeric domain, build a site, memorable phone number, pricing, numeric brand naming, sponsorship, acquire 017777.com. Add a short lead form on the homepage and pillar pages, a sticky mobile "Strategy call" button, and a memorability-score result that links to the form. Submit via FormSubmit AJAX to an address stored only as reversed base64 in `config.js` and decoded at send time; mailto fallback; honeypot field; redirect to thank-you. The address must never appear in page source.

### Phase 5 — Donations, contests, hiring, advertising
> Support page: tiers $7 / $77 / $777 / $7,777, allocation table (operations, hiring talent, contests & prizes, promotion & marketing, reserve), goal bar, pledge form (amount, frequency, designation), and PayPal/Stripe/BMC/Ko-fi buttons that appear automatically when links are added in `config.js`. Contests page: monthly Lucky 7 Challenge puzzle with entry form, creator challenge, tool-idea prize, official rules (no purchase necessary, 18+, random draw, notification). Careers page with six paid contributor roles and an application form. Advertise page with sponsorship packages, standards and a media-kit request form.

### Phase 6 — Launch, approval and growth
> Push to github.com/webworksa1/017777-com, enable Pages (main branch, root), point DNS (A records 185.199.108–111.153, CNAME www → webworksa1.github.io), tick "Enforce HTTPS". Submit sitemap in Google Search Console; apply in AdSense once indexed; enable Google's certified CMP (Privacy & messaging) for EEA/UK visitors. Then: add 20 new number pages per month from Search Console queries, a monthly numeric-domain sales report, embeddable tool widgets for backlinks, and Hindi/Spanish/Chinese editions.

## 5. AdSense readiness checklist
- [x] 50+ indexable pages of original content; maths-first number pages with unique facts
- [x] About, Contact, Privacy (with Google cookie disclosure), Terms, Disclaimer, Editorial policy
- [x] Clear navigation, HTML + XML sitemaps, no broken internal links, mobile responsive
- [x] Belief content labelled; no medical, financial-guarantee or gambling claims
- [x] ads.txt with pub-6620975821265271; AdSense script in every head
- [ ] Custom domain live over HTTPS and indexed in Search Console (do before applying)
- [ ] CMP enabled in AdSense for EEA/UK traffic
