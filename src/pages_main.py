from layout import *

VIDEOS = [
    ("UDQjn_-pDSs", "Why 7 is weird", "Numberphile on the odd mathematical habits of seven."),
    ("yi-s-TTpLxY", "Divisibility tricks", "Numberphile on testing divisibility by hand — useful for decoding any number."),
    ("EI707AkhvaI", "What is the Rule of 72?", "The shortcut for how fast money, prices or users double."),
    ("DlLtaNxCYNE", "Where the 72 in the Rule of 72 comes from", "The logarithm behind the shortcut."),
    ("QhY5IV7CRhw", "Double your money: the maths of the Rule of 72", "Worked examples at different growth rates."),
    ("USCBCmwMCDA", "How computers work: binary and data", "How zeros and ones store numbers, text and images — the base layer of every AI model."),
]


def lead_mini(title="Have a number that should be earning more?", relay="Quick lead"):
    return f"""<div class="panel big">
  <h2 style="margin-bottom:.3em">{title}</h2>
  <p class="muted">A domain, a phone number, a price point or a brand name built on digits. Tell us what it is; we reply within two business days with a plain assessment and next steps.</p>
  <form class="lead" data-relay="{relay}">
    {honeypot()}
    <div class="row">
      <div><label for="lm-name">Your name</label><input id="lm-name" name="name" required autocomplete="name"></div>
      <div><label for="lm-email">Email</label><input id="lm-email" type="email" name="email" required autocomplete="email"></div>
    </div>
    <div class="row">
      <div><label for="lm-type">What is it?</label>
        <select id="lm-type" name="asset_type" required><option value="">Choose one</option><option>Numeric domain name</option><option>Phone / vanity number</option><option>Pricing strategy</option><option>Numeric brand or product name</option><option>Sponsorship or partnership</option><option>Something else</option></select></div>
      <div><label for="lm-num">The number (optional)</label><input id="lm-num" name="number" inputmode="numeric" placeholder="e.g. 7777.com or 0800 777 7777"></div>
    </div>
    {consent()}
    <div class="btn-row"><button class="btn gold" type="submit">Get my free assessment</button><a class="btn ghost" href="/number-strategy.html">See the full intake</a></div>
    <p class="form-status" role="status"></p>
  </form>
</div>"""


def home():
    faqs = [
        ("What is 017777.com?", "A free number-intelligence site: an instant number decoder, eight calculators, a library of number meanings, and research on how numbers influence pricing, technology, the economy and belief."),
        ("Is the number decoder free?", "Yes. Every tool runs in your browser, needs no account, and does not send the numbers you type to our servers."),
        ("Are angel number meanings real?", "They are a belief tradition. We present them as culture and entertainment and explain the psychology (the frequency illusion) alongside them. Nothing here predicts the future."),
        ("Can you help me buy or sell a numeric domain or phone number?", "Yes. Use the strategy call form; we assess the asset and reply with options within two business days."),
        ("How is the site funded?", "Advertising, reader support, sponsorships and paid strategy calls. Ads never change our editorial content."),
    ]
    body = f"""
<section class="hero">
  <div class="wrap">
    <div>
      <h1>Every number has a story. Decode yours in one second.</h1>
      <p class="lead">Type any number — a price, a phone number, a domain, a date — and see its maths, its patterns, what its digits mean in five cultures, and how businesses use numbers like it.</p>
      <div class="btn-row">
        <a class="btn gold" id="hero-more" href="/tools.html#n=017777">See the full breakdown</a>
        <a class="btn ghost" href="/meaning-of-017777.html">Why 01 7777?</a>
      </div>
    </div>
    <div class="board">
      <div class="flaps" id="flaps" role="img" aria-label="017777"></div>
      <form id="hero-form" aria-label="Decode a number">
        <input name="n" inputmode="numeric" maxlength="12" placeholder="Try 7777, 888 or your price" aria-label="Number to decode">
        <button class="btn gold" type="submit">Decode</button>
      </form>
      <div class="facts" id="hero-facts" aria-live="polite"></div>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Eight free tools, no sign-up</h2>
    <p class="muted prose">Built after studying how the best calculator, numerology, area-code and domain-data sites work — then keeping only what helps.</p>
    <div class="grid g4">
      <div class="panel"><span class="tag">Maths</span><h3><a href="/tools.html#decoder">Number decoder</a></h3><p>Primes, factors, digit sum, binary, hex, Roman numerals and patterns.</p></div>
      <div class="panel"><span class="tag">Commerce</span><h3><a href="/tools.html#charm">Charm-price calculator</a></h3><p>Compare .99, .97, .95 and lucky-digit endings with your margin.</p></div>
      <div class="panel"><span class="tag">Economy</span><h3><a href="/tools.html#rule72">Rule of 72</a></h3><p>How fast money, prices or users double — estimate vs exact.</p></div>
      <div class="panel"><span class="tag">Brands</span><h3><a href="/tools.html#memo">Number memorability score</a></h3><p>Score a domain, phone number or plate for recall and buyer appeal.</p></div>
      <div class="panel"><span class="tag">Belief</span><h3><a href="/tools.html#name">Name numerology</a></h3><p>Expression, soul urge and life path — labelled as tradition.</p></div>
      <div class="panel"><span class="tag">Fun</span><h3><a href="/tools.html#lucky">Lucky number picker</a></h3><p>A repeatable set from your name and date. Honest about the odds.</p></div>
      <div class="panel"><span class="tag">Tech</span><h3><a href="/tools.html#base">Base converter</a></h3><p>Decimal, binary, octal and hex in both directions.</p></div>
      <div class="panel"><span class="tag">Phone</span><h3><a href="/tools.html#word">Phone-word dialler</a></h3><p>Turn a vanity word into the digits to dial.</p></div>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="wrap layout-side">
    <div class="prose">
      <h2>017777, decoded</h2>
      <p>The six digits that name this site carry more than a lucky streak. Here is what our research found:</p>
      <ul>
        <li><strong>01 is the alphabet of computing.</strong> Every image, payment and AI model is ultimately stored as zeros and ones.</li>
        <li><strong>7777 is the West's luck, four times over.</strong> Seven is the most-picked favourite number in surveys, and 777 is the slot-machine jackpot.</li>
        <li><strong>01777 is a real dialling code</strong> — Retford, Nottinghamshire, in the UK.</li>
        <li><strong>017 was a prestige mobile prefix</strong> in South Korea before every mobile number moved to 010.</li>
        <li><strong>17777 = 29 × 613</strong>, and its digits add up to 29 — so the number is divisible by its own digit sum.</li>
      </ul>
      <a class="btn" href="/meaning-of-017777.html">Read the full 017777 report</a>
    </div>
    <aside><div class="panel">
      <h3>Popular number pages</h3>
      <div class="kv">
        <a href="/numbers/7.html"><span>7</span></a><a href="/numbers/77.html"><span>77</span></a><a href="/numbers/777.html"><span>777</span></a><a href="/numbers/7777.html"><span>7777</span></a>
        <a href="/numbers/111.html"><span>111</span></a><a href="/numbers/888.html"><span>888</span></a><a href="/numbers/1111.html"><span>1111</span></a><a href="/numbers/444.html"><span>444</span></a><a href="/numbers/8888.html"><span>8888</span></a><a href="/numbers/17777.html"><span>17777</span></a>
      </div>
      <p style="margin-top:12px"><a href="/numbers/">Browse all number meanings</a></p>
    </div></aside>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Where numbers move money and minds</h2>
    <div class="grid g4">
      <div class="panel"><h3><a href="/commerce.html">Commerce</a></h3><p>Price endings, lucky-number pricing, vanity phone numbers and the market for numeric domains.</p></div>
      <div class="panel"><h3><a href="/ai-economy.html">AI & economy</a></h3><p>Binary, tokens and parameters; compounding, inflation and the Rule of 72.</p></div>
      <div class="panel"><h3><a href="/culture.html">Culture & people</a></h3><p>Why 8 sells in Shanghai, 4 is skipped in Seoul lifts, and 7 wins favourite-number polls.</p></div>
      <div class="panel"><h3><a href="/numbers/">Number meanings</a></h3><p>Repeating numbers from 0 to 9999 — maths first, tradition second, psychology always.</p></div>
    </div>
  </div>
</section>

<section class="block alt" id="lead">
  <div class="wrap">{lead_mini()}</div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Watch: the maths behind lucky numbers</h2>
    <div class="grid g2">{video(*VIDEOS[0])}{video(*VIDEOS[2])}</div>
    <p style="margin-top:16px"><a href="/videos.html">More videos</a></p>
  </div>
</section>

<section class="block alt">
  <div class="wrap grid g2">
    <div class="panel big"><h2>Lucky 7 Challenge</h2><p>Solve the monthly number puzzle. Correct entries go into a prize draw. Free to enter — no purchase necessary.</p><a class="btn gold" href="/contests.html">Enter this month's contest</a></div>
    <div class="panel big"><h2>Keep the tools free</h2><p>Reader support pays for hosting, new tools, research, contest prizes and paid contributors. Tiers start at 7.</p><a class="btn" href="/support.html">Support 017777</a></div>
  </div>
</section>

<section class="block">
  <div class="wrap prose">
    <h2>Questions</h2>
    {faq_html(faqs)}
  </div>
</section>
"""
    ld = [faq_ld(faqs), {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": SITE + "/",
                          "potentialAction": {"@type": "SearchAction", "target": SITE + "/tools.html#n={search_term_string}", "query-input": "required name=search_term_string"}},
          {"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": SITE + "/", "logo": SITE + "/assets/img/favicon.svg"}]
    return page("/", "017777 — Free Number Decoder, Number Meanings & Number Strategy",
                "Decode any number instantly: primes, factors, binary, cultural meanings and patterns. Free tools and research on numbers in commerce, AI, the economy and culture.",
                body, ld)


def meaning():
    faqs = [
        ("What does 017777 mean?", "As a number, 017777 has the value 17,777, which factors as 29 × 613. Read as '01 7777' it pairs the binary pair 0 and 1 with four sevens, the most popular 'lucky' digit in Western culture. As a dialling string it begins with 01777, the UK code for Retford, and with 017, a retired South Korean mobile prefix."),
        ("Is 017777 an angel number?", "Angel number traditions read 7777 as a sign of reflection and study and 01 as a new beginning. That is a belief tradition, not evidence; we cover the psychology on our number pages."),
        ("Is 17777 prime?", "No. 17777 = 29 × 613. Its digit sum is 29, so it is divisible by its own digit sum, which makes it a Harshad (Niven) number."),
        ("Is 017777 a phone number?", "Not as a full number. 01777 is the start of landline numbers in Retford, England, which run 01777 followed by six digits. We are not affiliated with any number holder."),
    ]
    body = page_head("What does 017777 mean? Six digits, five stories",
                     "The number behind this site, decoded across mathematics, telephony, commerce, AI and culture — with sources.",
                     [("/meaning-of-017777.html", "017777")]) + f"""
<section class="block"><div class="wrap layout-side"><article class="prose">
{byline()}
<div class="toc"><strong>On this page</strong><ol>
<li><a href="#maths">The maths of 17,777</a></li><li><a href="#zero-one">01: the language of machines</a></li>
<li><a href="#sevens">7777: luck, repeated</a></li><li><a href="#phone">017 and 01777 in telephone history</a></li>
<li><a href="#commerce">Seven in prices and marketing</a></li><li><a href="#economy">Seven in the economy</a></li>
<li><a href="#people">Seven and people</a></li><li><a href="#verdict">What it adds up to</a></li></ol></div>

<h2 id="maths">The maths of 17,777</h2>
<p>Drop the leading zero and 017777 is the integer 17,777. It is odd and not prime: 17,777 = 29 × 613, and 613 is itself prime. The digits 0 + 1 + 7 + 7 + 7 + 7 add up to 29 — the same 29 that divides the number. Numbers divisible by their own digit sum are called Harshad or Niven numbers, so 17,777 is a Harshad number with an unusually neat twist: its digit sum is one of its two prime factors.</p>
<table><tr><th>Property</th><th>Value</th></tr>
<tr><td>Value</td><td>17,777</td></tr><tr><td>Prime factors</td><td>29 × 613</td></tr><tr><td>Digit sum</td><td>29 (divides 17,777 exactly)</td></tr>
<tr><td>Digital root</td><td>2 (29 → 11 → 2; numerologists stop at master number 11)</td></tr>
<tr><td>Binary</td><td>100010101110001 (15 bits)</td></tr><tr><td>Hexadecimal</td><td>0x4571</td></tr></table>
<p><a href="/tools.html#n=017777">Run 017777 through the decoder</a> to see every property live.</p>

<h2 id="zero-one">01: the language of machines</h2>
<p>Zero and one are the only two symbols a digital computer needs. A transistor is either off or on; strings of those states encode text, money and images. Large language models are the same thing at scale: billions of numeric weights, each stored as a pattern of bits and multiplied trillions of times per answer. Reading 017777 as “01 + 7777” is a convenient metaphor for this site: the binary foundation of technology, followed by the most human of numbers.</p>

<h2 id="sevens">7777: luck, repeated</h2>
<p>Seven holds an unusual position in Western culture. It appears in the seven days of the week, the seven classical planets and the seven wonders, and it is the jackpot digit of slot machines (777). Numerology describes it as the number of analysis and inner wisdom; angel-number writers read 7777 as an amplified call to reflection and study. Those are traditions, not predictions — but they explain why repeated sevens get noticed, searched for and paid for.</p>
<p>In Chinese, seven (qī) is mixed: it sounds close to words for “rise” and “vital energy,” it gives its name to the Qixi lovers' festival on the seventh day of the seventh month, and that same seventh lunar month is also the Ghost Month. That double meaning matters to anyone marketing a 7-heavy number to Chinese-speaking audiences, who tend to prize 8 far more.</p>

<h2 id="phone">017 and 01777 in telephone history</h2>
<p><strong>United Kingdom.</strong> 01777 is the geographic dialling code for Retford in Nottinghamshire, also covering nearby villages such as Tuxford and Ranskill. Local numbers take the form 01777 plus six digits, and the code changed from 0777 in April 1995 when UK codes gained a leading 1 (<a href="https://area-codes.org.uk/01777" rel="nofollow noopener" target="_blank">area-codes.org.uk</a>).</p>
<p><strong>South Korea.</strong> 017 was the mobile prefix of Shinsegi Telecom, later absorbed by SK Telecom. From 2004 all new mobile numbers used 010, and SK Telecom shut its 2G network in 2020, ending 011 and 017 numbers after 25 years (<a href="https://www.asiae.co.kr/en/article/2020072707465774749" rel="nofollow noopener" target="_blank">Asia Economy</a>). Korea JoongAng Daily reported that 017 once carried a “power” image after it was chosen for Blue House staff phones in 1998 (<a href="https://www.koreajoongangdaily.com/business/days-numbered-for-011/11384112" rel="nofollow noopener" target="_blank">JoongAng Daily</a>). Some subscribers fought the switch in court — a reminder that people attach real identity to the first digits of a number.</p>

<h2 id="commerce">Seven in prices and marketing</h2>
<p>Prices ending in 7 are a habit in internet marketing (think 47 or 97). The evidence is mixed: retail pricing research favours endings in 9 and 99, and critics argue the “7 converts better” claim spread through workshops rather than controlled tests (<a href="https://www.blogmarketingacademy.com/prices-ending-in-7/" rel="nofollow noopener" target="_blank">Blog Marketing Academy</a>). Academic work on lucky numbers is more specific. In four experiments with 450 students, Chen and colleagues found lucky price endings raised purchase intention mainly among people who were superstitious, felt a loss of control or faced a significant event (<a href="https://doi.org/10.2224/sbp.11100" rel="nofollow noopener" target="_blank">Social Behavior and Personality, 2022</a>). A Singapore study found superstitious price endings persisted, especially for high-priced items, and that foreign brands localising their price endings gained a more positive brand attitude (<a href="https://fordoc.ku.de/2061" rel="nofollow noopener" target="_blank">KU Eichstätt-Ingolstadt project summary</a>).</p>
<div class="callout teal"><strong>Practical rule:</strong> use 9-endings as your default, test 7-endings for Western impulse buys, and use 8-endings — never 4 — for Chinese-speaking audiences. Try it in the <a href="/tools.html#charm">charm-price calculator</a>.</div>

<h2 id="economy">Seven in the economy</h2>
<p>Seven is also the number that makes compounding intuitive. By the Rule of 72, money growing at 7% a year doubles in about 72 ÷ 7 ≈ 10.3 years; the exact figure is 10.24 years, and 1.07 to the power of 10 is about 1.97. The same arithmetic tells you that 7% inflation halves the purchasing power of savings in roughly a decade. <a href="/tools.html#rule72">Run your own rate</a>.</p>

<h2 id="people">Seven and people</h2>
<p>Seven repeatedly tops informal “favourite number” polls in the West, and memory research made “seven, plus or minus two” a famous (if now debated) estimate of how many items we can hold in mind at once. That is one reason seven-digit local phone numbers felt natural and why short numeric names are easier to recall than long ones.</p>

<h2 id="verdict">What it adds up to</h2>
<p>017777 sits where several worlds meet: binary computing, Western luck, telephone history on two continents and a tidy piece of number theory. That is why this site is built as a hub for <em>all</em> numbers — tools, meanings and research — rather than a page about one number.</p>
<h2>Questions</h2>
{faq_html(faqs)}
</article>
<aside><div class="panel"><h3>Decode another number</h3><form id="decoder-form" data-start="017777"><input class="" style="width:100%;padding:10px;border-radius:6px;border:1px solid var(--line)" name="n" inputmode="numeric" aria-label="Number"><button class="btn" style="margin-top:8px;width:100%">Decode</button></form><div class="tool-out" id="decoder-out"></div></div></aside>
</div></section>
<section class="block alt"><div class="wrap">{lead_mini("Own a number like this? Let's put it to work.", "017777 page lead")}</div></section>
"""
    ld = [faq_ld(faqs), {"@context": "https://schema.org", "@type": "Article", "headline": "What does 017777 mean?",
                          "dateModified": UPDATED, "author": {"@type": "Organization", "name": "017777 editorial team"}}]
    return page("/meaning-of-017777.html", "What Does 017777 Mean? Maths, Phone Codes, Luck & Business",
                "017777 decoded: 17,777 = 29 × 613, the UK 01777 Retford code, Korea's retired 017 prefix, why 7777 means luck, and how seven shapes prices and the economy.",
                body, ld)


def tools():
    body = page_head("Number decoder and free number tools",
                     "Eight tools that run entirely in your browser. Nothing you type is stored or sent anywhere.",
                     [("/tools.html", "Tools")]) + f"""
<section class="block"><div class="wrap">
<div class="panel big" id="decoder">
  <h2>Number decoder</h2>
  <p class="muted">Leading zeros are kept, so you can decode phone prefixes and codes like 017777.</p>
  <form id="decoder-form" class="lead" data-start="017777"><div class="row"><input name="n" inputmode="numeric" maxlength="30" aria-label="Number to decode" placeholder="Any number up to 30 digits"><button class="btn gold" type="submit">Decode</button></div></form>
  <div class="tool-out" id="decoder-out" aria-live="polite"></div>
</div>
<div class="grid g2" style="margin-top:20px">
  <div class="panel" id="charm"><h3>Charm-price calculator</h3>
    <form id="charm-form" class="lead"><div class="row"><div><label for="price">Your price</label><input id="price" name="price" type="number" step="0.01" min="0.01" value="20" required></div><div><label for="cost">Unit cost (optional)</label><input id="cost" name="cost" type="number" step="0.01" min="0" value="12"></div></div><button class="btn" style="margin-top:12px" type="submit">Compare endings</button></form>
    <div class="tool-out" id="charm-out" aria-live="polite"></div></div>
  <div class="panel" id="rule72"><h3>Rule of 72 doubling time</h3>
    <form id="rule72-form" class="lead"><label for="rate">Annual growth or inflation rate (%)</label><input id="rate" name="rate" type="number" step="0.1" min="0.1" value="7" required><button class="btn" style="margin-top:12px" type="submit">Calculate</button></form>
    <div class="tool-out" id="rule72-out" aria-live="polite"></div></div>
  <div class="panel" id="memo"><h3>Number memorability score</h3>
    <form id="memo-form" class="lead"><label for="num">Domain, phone number or code (digits only)</label><input id="num" name="num" inputmode="numeric" value="7777" required><button class="btn" style="margin-top:12px" type="submit">Score it</button></form>
    <div class="tool-out" id="memo-out" aria-live="polite"></div></div>
  <div class="panel" id="name"><h3>Name numerology</h3>
    <form id="name-form" class="lead"><label for="name_input">Full name</label><input id="name_input" name="name_input" required autocomplete="off"><label for="dob">Date of birth (optional)</label><input id="dob" name="dob" type="date"><button class="btn" style="margin-top:12px" type="submit">Calculate</button></form>
    <div class="tool-out" id="name-out" aria-live="polite"></div></div>
  <div class="panel" id="lucky"><h3>Lucky number picker</h3>
    <form id="lucky-form" class="lead"><label for="seed">Name or word</label><input id="seed" name="seed" value="017777"><div class="row"><div><label for="ldate">Date</label><input id="ldate" name="date" type="date"></div><div><label for="count">How many</label><input id="count" name="count" type="number" min="1" max="10" value="6"></div></div><label for="max">Highest number</label><input id="max" name="max" type="number" min="5" max="100" value="49"><button class="btn" style="margin-top:12px" type="submit">Pick numbers</button></form>
    <div class="tool-out" id="lucky-out" aria-live="polite"></div></div>
  <div class="panel" id="base"><h3>Base converter</h3>
    <form id="base-form" class="lead"><div class="row"><div><label for="val">Value</label><input id="val" name="val" value="17777" required></div><div><label for="from">From base</label><select id="from" name="from"><option value="10">Decimal</option><option value="2">Binary</option><option value="8">Octal</option><option value="16">Hex</option></select></div></div><button class="btn" style="margin-top:12px" type="submit">Convert</button></form>
    <div class="tool-out" id="base-out" aria-live="polite"></div></div>
  <div class="panel" id="word"><h3>Phone-word dialler</h3>
    <form id="word-form" class="lead"><label for="w">Vanity word or phrase</label><input id="w" name="word" value="LUCKY7" required><button class="btn" style="margin-top:12px" type="submit">Get digits</button></form>
    <div class="tool-out" id="word-out" aria-live="polite"></div></div>
  <div class="panel"><h3>Need a human answer?</h3><p>The tools give you the arithmetic. For a decision — buying a numeric domain, choosing a business phone number, setting a launch price — book a strategy call.</p><a class="btn gold" href="/number-strategy.html">Request a strategy call</a></div>
</div>
<div class="prose" style="margin-top:40px">
<h2>How the tools work</h2>
<p>Every calculation runs in JavaScript on your device. The decoder uses exact big-integer arithmetic, tests primality by trial division up to one trillion, and factors numbers in the same range. Numerology tools use the Pythagorean letter table (A=1 … I=9, J=1 …) and keep master numbers 11, 22 and 33. The memorability score is a transparent heuristic: shorter strings, fewer distinct digits, repeated runs and culturally favoured digits score higher; the digit 4 scores lower because many East Asian buyers avoid it. It is not a valuation.</p>
<p>Spotted an error or want a new tool? <a href="/contact.html">Tell us</a> — reader suggestions decide what we build next.</p>
</div>
</div></section>
"""
    ld = [{"@context": "https://schema.org", "@type": "WebApplication", "name": "017777 Number Decoder", "applicationCategory": "UtilitiesApplication",
           "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": SITE + "/tools.html"}]
    return page("/tools.html", "Free Number Decoder, Charm Price, Rule of 72 & Numerology Tools | 017777",
                "Decode any number (primes, factors, binary, hex, patterns, cultural meaning), compare price endings, find doubling time, score number memorability and more. Free, private, instant.",
                body, ld)


def commerce():
    body = page_head("Numbers in commerce: prices, phone numbers and numeric domains",
                     "How businesses use digits to sell — what the research supports and what is folklore.",
                     [("/commerce.html", "Commerce")]) + f"""
<section class="block"><div class="wrap layout-side"><article class="prose">
{byline()}
<h2>Price endings: 9, 7 and the left digit</h2>
<p>The most robust pricing effect is the left-digit effect: buyers read the first digit and partly ignore the rest, so 19.99 feels closer to 19 than to 20. That is why 9 and 99 endings dominate retail. Seven-endings (27, 47, 97) are common in online info-products, but the case for them rests mostly on marketing habit; one long-time marketer calls it herd behaviour rather than tested fact (<a href="https://www.blogmarketingacademy.com/prices-ending-in-7/" rel="nofollow noopener" target="_blank">Blog Marketing Academy</a>).</p>
<p>Round prices (20, 100) signal quality and simplicity and tend to suit premium or emotional purchases; precise prices (19.97) signal a calculated, discounted offer. The choice is a positioning decision, not a trick.</p>

<h2>Lucky numbers change purchase intent — for some buyers</h2>
<p>Research from Beijing found lucky price endings lifted purchase intention when buyers were in a negative mood, superstitious, felt a lack of control or had just faced an important event (<a href="https://doi.org/10.2224/sbp.11100" rel="nofollow noopener" target="_blank">Chen et al., 2022</a>). In Singapore, superstitious endings persisted in newspaper ads — especially for expensive items and Eastern brands — and Western brands that localised their price endings were rated more positively (<a href="https://fordoc.ku.de/2061" rel="nofollow noopener" target="_blank">Gelbrich et al.</a>).</p>
<div class="table-scroll"><table><tr><th>Audience</th><th>Favoured endings</th><th>Avoid</th></tr>
<tr><td>US, UK, Canada, EU retail</td><td>.99, .95, 9</td><td>Awkward precision on luxury goods</td></tr>
<tr><td>Chinese-speaking markets</td><td>8, 88, 888, 6</td><td>4, 14, 74</td></tr>
<tr><td>Japan</td><td>7, 8, 5</td><td>4, 9 (in some contexts)</td></tr>
<tr><td>India</td><td>9, 99 and round amounts with an added 1 for gifts (101, 501, 1001)</td><td>Context-dependent</td></tr>
</table></div>

<h2>Memorable phone numbers</h2>
<p>A number customers can recall is free advertising. Vanity numbers spell a word on the keypad (1-800-FLOWERS style), while “golden” numbers use repeats such as 7777 or 8888. In Korea, the early mobile prefixes carried status, and when the government unified them under 010 thousands of subscribers resisted (<a href="https://www.koreajoongangdaily.com/business/days-numbered-for-011/11384112" rel="nofollow noopener" target="_blank">JoongAng Daily</a>). Use our <a href="/tools.html#word">phone-word dialler</a> to check what a word dials.</p>

<h2>Numeric domain names as assets</h2>
<p>Short numeric .com names are scarce by construction: there are only 10,000 four-digit .coms and 100,000 five-digit ones. Chinese buyers drove a well-documented boom in short and numeric names; TechCrunch reported that China had become the largest buyer of domains, with three-letter .coms that once sold for $10,000–$15,000 reaching $50,000 or more (<a href="https://techcrunch.com/?p=1246089" rel="nofollow noopener" target="_blank">TechCrunch</a>). Buyers value numeric names because they cross language barriers, work on any keyboard and can carry cultural luck.</p>
<p>What drives value: length first, then the number of distinct digits, repeats and patterns, culturally lucky digits (8, 6, 9) and absence of 4. Score any string with the <a href="/tools.html#memo">memorability tool</a>, then talk to us before you buy or sell.</p>
<div class="callout"><strong>Thinking of buying, selling or developing a numeric domain or phone number?</strong> <a href="/number-strategy.html">Request a strategy call</a> — we reply within two business days.</div>

<h2>Numbers in brand names</h2>
<p>Digits in brand names (7-Eleven, 3M, Forever 21) are short, global and easy to trademark in combination — but a bare number is hard to own. If you plan a numeric brand, pair the digits with a distinctive word or design mark and check existing registrations first.</p>
</article>
<aside><div class="panel"><h3>Try it</h3><p><a href="/tools.html#charm">Charm-price calculator</a></p><p><a href="/tools.html#memo">Memorability score</a></p><p><a href="/tools.html#word">Phone-word dialler</a></p><a class="btn gold" href="/number-strategy.html">Strategy call</a></div></aside>
</div></section>
"""
    return page("/commerce.html", "Numbers in Commerce: Price Endings, Lucky Pricing, Vanity Numbers & Numeric Domains",
                "What research says about .99 vs 7-ending prices, lucky-number pricing across cultures, memorable phone numbers and why numeric domain names are valuable assets.", body)


def ai_economy():
    body = page_head("Numbers in AI and the economy",
                     "From the zeros and ones under every AI model to the compounding that decides every economy.",
                     [("/ai-economy.html", "AI & economy")]) + f"""
<section class="block"><div class="wrap layout-side"><article class="prose">
{byline()}
<h2>Binary: why everything is 0 and 1</h2>
<p>Digital hardware is built from switches that are either off or on, so every value is written in base 2. The number 17,777 is 100010101110001 in binary — 15 bits. A byte is 8 bits and can hold 256 values (0–255). Hexadecimal groups bits in fours, which is why 17,777 is the compact 0x4571. <a href="/tools.html#base">Convert any value</a>.</p>
{video(*VIDEOS[5])}

<h2>How AI models are made of numbers</h2>
<ul>
<li><strong>Tokens.</strong> Language models split text into tokens — whole words, word pieces or punctuation — and give each one an integer ID.</li>
<li><strong>Embeddings.</strong> Each token ID maps to a long list of decimal numbers that captures meaning by position in a high-dimensional space.</li>
<li><strong>Parameters.</strong> A model's “knowledge” is a very large set of numeric weights adjusted during training. Bigger models have more weights, but data quality and training method matter as much as size.</li>
<li><strong>Precision.</strong> Weights are stored as 32-, 16-, 8- or even 4-bit numbers. Fewer bits mean smaller, cheaper, faster models with a small accuracy trade-off — a pure numbers decision with large cost consequences.</li>
<li><strong>Randomness.</strong> “Temperature” controls how strongly a model favours its most likely next token. Low temperature is predictable; high temperature is varied.</li>
</ul>

<h2>The Rule of 72 and compounding</h2>
<p>Divide 72 by a growth rate to estimate how many years it takes to double. At 7% that is about 10.3 years (exact: 10.24). The rule works for anything that compounds: investments, prices under inflation, users, revenue, even model training compute.</p>
<div class="table-scroll"><table><tr><th>Annual rate</th><th>Rule of 72</th><th>Exact doubling time</th></tr>
<tr><td>2%</td><td>36.0 yrs</td><td>35.0 yrs</td></tr><tr><td>4%</td><td>18.0 yrs</td><td>17.7 yrs</td></tr><tr><td>7%</td><td>10.3 yrs</td><td>10.2 yrs</td></tr><tr><td>10%</td><td>7.2 yrs</td><td>7.3 yrs</td></tr><tr><td>18%</td><td>4.0 yrs</td><td>4.2 yrs</td></tr></table></div>
<div class="grid g2">{video(*VIDEOS[2])}{video(*VIDEOS[3])}</div>

<h2>Numbers that move markets</h2>
<p>Economies run on a handful of headline figures: inflation rates, policy interest rates, unemployment, GDP growth and exchange rates. Two numeric habits help when reading them. First, convert rates into doubling or halving times, which are easier to feel. Second, watch round-number thresholds: markets and media react to levels like 2% inflation targets or index milestones because round numbers anchor attention, even when nothing fundamental changed at that exact point.</p>
<p>Prices themselves are numbers chosen by people. That is why the <a href="/commerce.html">commerce guide</a> covers how digit choices shape what buyers do.</p>
<p class="muted">This page is educational and is not financial or investment advice.</p>
</article>
<aside><div class="panel"><h3>Calculate</h3><p><a href="/tools.html#rule72">Rule of 72</a></p><p><a href="/tools.html#base">Base converter</a></p><p><a href="/tools.html#decoder">Number decoder</a></p></div></aside>
</div></section>
"""
    return page("/ai-economy.html", "Numbers in AI & the Economy: Binary, Tokens, Parameters and the Rule of 72",
                "Plain-language guide to the numbers behind AI (binary, tokens, embeddings, parameters, precision) and the economy (compounding, inflation, the Rule of 72).", body)


def culture():
    body = page_head("Lucky and unlucky numbers around the world",
                     "Why the same digit can sell an apartment in Hong Kong and empty a floor in Seoul.",
                     [("/culture.html", "Culture")]) + f"""
<section class="block"><div class="wrap"><div class="prose">{byline()}</div>
<div class="table-scroll"><table>
<tr><th>Digit</th><th>Western traditions</th><th>Chinese</th><th>Japanese</th><th>Korean</th><th>Indian traditions</th></tr>
<tr><td>0</td><td>Fresh start, nothing</td><td>Neutral (líng)</td><td>Neutral</td><td>Neutral</td><td>Zero as a number is credited to Indian mathematics</td></tr>
<tr><td>1</td><td>First, leader</td><td>Unity (yī)</td><td>Top rank</td><td>Neutral</td><td>Added to gift amounts (101, 501) for a fresh beginning</td></tr>
<tr><td>2</td><td>Balance</td><td>Pairs are lucky</td><td>Neutral</td><td>Neutral</td><td>Duality</td></tr>
<tr><td>3</td><td>Completeness</td><td>Sounds like “life” in some dialects</td><td>Neutral</td><td>Lucky (sam)</td><td>Trinity (trimurti)</td></tr>
<tr><td>4</td><td>Stability</td><td>Unlucky — sounds like “death”</td><td>Unlucky (shi)</td><td>Unlucky (sa) — lifts often show F</td><td>Neutral</td></tr>
<tr><td>6</td><td>Can be unlucky (666)</td><td>Lucky — “smooth, flowing”</td><td>Neutral</td><td>Neutral</td><td>Neutral</td></tr>
<tr><td>7</td><td>Lucky; jackpot 777</td><td>Mixed — Qixi festival vs Ghost Month</td><td>Lucky — Seven Lucky Gods</td><td>Lucky</td><td>Sacred — seven vows (saptapadi)</td></tr>
<tr><td>8</td><td>Infinity on its side</td><td>Very lucky — sounds like “prosper”</td><td>Lucky — the shape widens</td><td>Neutral</td><td>Neutral</td></tr>
<tr><td>9</td><td>Completion</td><td>Lucky — “long-lasting”</td><td>Can sound like “suffering”</td><td>Neutral</td><td>Associated with completion and prosperity</td></tr>
<tr><td>13</td><td>Unlucky — hotels skip floor 13</td><td>Neutral</td><td>Neutral</td><td>Neutral</td><td>Neutral</td></tr>
</table></div>
<div class="prose">
<p class="muted">Traditions vary by region and family; treat this table as a starting point, not a rule. Sources include <a href="https://www.lingoace.com/blog/meaning-of-7-in-chinese-lucky-unlucky/" rel="nofollow noopener" target="_blank">LingoAce on the number 7 in Chinese</a>.</p>
<h2>Why people care: the psychology</h2>
<p>Lucky numbers persist because they give a sense of control in uncertain moments. Lab research links lucky-number preferences to stress, superstition and loss of control (<a href="https://doi.org/10.2224/sbp.11100" rel="nofollow noopener" target="_blank">Chen et al., 2022</a>). Repeated sightings of a number (11:11 on a clock, 777 on a receipt) are explained by the frequency illusion: once something is on your mind, you notice it more, and every match feels meaningful.</p>
<h2>Real consequences</h2>
<ul>
<li>Buildings in East Asia skip 4th, 14th and 24th floors; Western hotels often skip 13.</li>
<li>Licence plates and phone numbers with 8s sell at auction premiums in Hong Kong and mainland China.</li>
<li>South Korean subscribers fought for years to keep old 011 and 017 mobile prefixes they saw as part of their identity (<a href="https://www.asiae.co.kr/en/article/2020072707465774749" rel="nofollow noopener" target="_blank">Asia Economy</a>).</li>
<li>Wedding and launch dates cluster on number patterns such as 8/8/2008 and 7/7/2007.</li>
</ul>
<h2>Explore a number</h2>
<p>Every page in our <a href="/numbers/">number meanings library</a> separates the mathematics from the tradition, so you can enjoy the culture without mistaking it for prediction.</p>
</div></div></section>
"""
    return page("/culture.html", "Lucky and Unlucky Numbers by Culture: Chinese, Japanese, Korean, Indian & Western",
                "A comparison table of what digits 0–9 mean across cultures — why 8 is prized in China, 4 avoided across East Asia, and 7 loved in the West — plus the psychology behind it.", body)


def videos():
    cards = "".join(video(*v) for v in VIDEOS)
    body = page_head("Videos: the maths and money behind numbers",
                     "Hand-picked explainers from YouTube creators. We add context; the videos belong to their creators.",
                     [("/videos.html", "Videos")]) + f"""
<section class="block"><div class="wrap"><div class="grid g2">{cards}</div>
<div class="prose" style="margin-top:32px"><p class="muted">Videos are embedded with YouTube's privacy-enhanced mode and load only when you press play. All rights belong to the respective creators. Want your video featured or to sponsor a video series? <a href="/advertise.html">Get in touch</a>.</p></div></div></section>
"""
    return page("/videos.html", "Number Videos: Why 7 Is Weird, the Rule of 72, Binary Explained | 017777",
                "Curated videos on number theory, the Rule of 72, compounding and binary computing, with context from the 017777 team.", body)


PAGES = {"index.html": home, "meaning-of-017777.html": meaning, "tools.html": tools, "commerce.html": commerce,
         "ai-economy.html": ai_economy, "culture.html": culture, "videos.html": videos}
