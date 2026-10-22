from layout import *


def strategy():
    faqs = [
        ("What does a strategy call cost?", "The first assessment is free. If you want ongoing help — brokerage, a pricing test plan or a naming project — we quote a fixed fee or a success fee before any work starts."),
        ("How fast will you reply?", "Within two business days, usually sooner. Urgent deals (an auction closing, a launch date) — say so in the form."),
        ("Do you buy domains or numbers yourself?", "Sometimes, for the right asset. Tell us whether you want to sell, and we will be clear about whether we are a buyer or acting for you."),
        ("Is my information private?", "Yes. We use it only to answer your request. We never sell lead data. See the privacy policy."),
    ]
    body = page_head("Turn a number into revenue",
                     "Free first assessment for numeric domains, memorable phone numbers, pricing and number-based brands. Reply within two business days.",
                     [("/number-strategy.html", "Strategy call")]) + f"""
<section class="block"><div class="wrap layout-side">
<div>
  <div class="panel big">
    <form class="lead" data-relay="Strategy call" data-steps>
      <div class="steps-bar" aria-hidden="true"><span></span><span></span><span></span></div>
      {honeypot()}
      <div class="step">
        <h2 style="font-size:1.5rem">What can we help with?</h2>
        <div class="choice-grid">
          <label class="choice"><input type="radio" name="goal" value="Buy a numeric domain" required> Buy a numeric domain</label>
          <label class="choice"><input type="radio" name="goal" value="Sell a numeric domain"> Sell a numeric domain</label>
          <label class="choice"><input type="radio" name="goal" value="Build a website on my domain"> Build a site on my domain</label>
          <label class="choice"><input type="radio" name="goal" value="Find a memorable phone number"> Find a memorable phone number</label>
          <label class="choice"><input type="radio" name="goal" value="Pricing strategy / price endings"> Set or test my prices</label>
          <label class="choice"><input type="radio" name="goal" value="Name a brand or product with numbers"> Name a brand with numbers</label>
          <label class="choice"><input type="radio" name="goal" value="Sponsorship / partnership"> Sponsor or partner</label>
          <label class="choice"><input type="radio" name="goal" value="Acquire 017777.com"> Acquire this domain</label>
        </div>
        <div class="btn-row"><button class="btn" type="button" data-next>Continue</button></div>
      </div>
      <div class="step">
        <h2 style="font-size:1.5rem">Tell us about it</h2>
        <label for="s-asset">The number, domain or product</label><input id="s-asset" name="asset" placeholder="e.g. 8686.com, 0800 777 777, my $47 course">
        <div class="row">
          <div><label for="s-budget">Budget or expected value</label><select id="s-budget" name="budget" required><option value="">Choose a range</option><option>Under $1,000</option><option>$1,000–$10,000</option><option>$10,000–$50,000</option><option>$50,000–$250,000</option><option>$250,000+</option><option>Not sure yet</option></select></div>
          <div><label for="s-time">Timeline</label><select id="s-time" name="timeline" required><option value="">Choose one</option><option>This week</option><option>This month</option><option>This quarter</option><option>Just exploring</option></select></div>
        </div>
        <label for="s-msg">Anything else we should know?</label><textarea id="s-msg" name="message" rows="4"></textarea>
        <div class="btn-row"><button class="btn ghost" type="button" data-prev>Back</button><button class="btn" type="button" data-next>Continue</button></div>
      </div>
      <div class="step">
        <h2 style="font-size:1.5rem">Where should we send your assessment?</h2>
        <div class="row">
          <div><label for="s-name">Name</label><input id="s-name" name="name" required autocomplete="name"></div>
          <div><label for="s-email">Email</label><input id="s-email" type="email" name="email" required autocomplete="email"></div>
        </div>
        <div class="row">
          <div><label for="s-company">Company (optional)</label><input id="s-company" name="company" autocomplete="organization"></div>
          <div><label for="s-country">Country</label><input id="s-country" name="country" autocomplete="country-name"></div>
        </div>
        <label for="s-phone">Phone or WhatsApp (optional)</label><input id="s-phone" name="phone" type="tel" autocomplete="tel">
        {consent()}
        <div class="btn-row"><button class="btn ghost" type="button" data-prev>Back</button><button class="btn gold" type="submit">Send my request</button></div>
        <p class="form-status" role="status"></p>
        <p class="form-note">Free first assessment. No obligation. We never sell your details.</p>
      </div>
    </form>
  </div>
  <div class="prose" style="margin-top:36px">
    <h2>What you get</h2>
    <div class="grid g3">
      <div class="panel"><h3>Numeric domains</h3><p>Comparable sales context, buyer-market fit (Western vs East Asian), acquisition or outbound sale plan.</p></div>
      <div class="panel"><h3>Phone numbers</h3><p>Shortlist of memorable or vanity numbers and the trade-offs of toll-free vs local.</p></div>
      <div class="panel"><h3>Pricing</h3><p>An A/B test plan for price endings and anchors, sized to your traffic.</p></div>
    </div>
    <h2>How it works</h2>
    <ol><li>Send the three-step form (about two minutes).</li><li>We review the asset and reply within two business days.</li><li>You decide whether to go further. The first assessment is free.</li></ol>
    <h2>Questions</h2>{faq_html(faqs)}
  </div>
</div>
<aside><div class="panel">
  <h3>Why work with us</h3>
  <ul><li>Focused only on numbers: domains, phone numbers, prices and names.</li><li>Plain-language advice with the reasoning shown.</li><li>No fee unless you choose paid work.</li></ul>
  <p>Prefer to write directly? <a href="#" data-mail="Strategy call request">Email us</a>.</p>
</div></aside>
</div></section>
"""
    return page("/number-strategy.html", "Number Strategy Call: Numeric Domains, Phone Numbers & Pricing | 017777",
                "Get a free assessment for buying or selling a numeric domain, finding a memorable phone number, testing price endings or naming a brand with numbers.", body, [faq_ld(faqs)])


def support():
    body = page_head("Support 017777",
                     "Your support keeps every tool free, funds new research and pays real people — writers, developers and contest winners.",
                     [("/support.html", "Support")]) + f"""
<section class="block"><div class="wrap">
<div class="grid g4">
  <div class="panel tier"><h3>Supporter</h3><div class="price">$7</div><ul><li>Keeps the decoder online for a week</li><li>Name on the supporters page (optional)</li></ul><button class="btn" type="button" data-amount="7">Choose $7</button></div>
  <div class="panel tier"><h3>Builder</h3><div class="price">$77</div><ul><li>Funds one new tool or research page</li><li>Early access to new tools</li><li>Supporter badge in the newsletter</li></ul><button class="btn" type="button" data-amount="77">Choose $77</button></div>
  <div class="panel tier feature"><h3>Patron</h3><div class="price">$777</div><ul><li>Sponsors a month of contest prizes</li><li>Thank-you link on the homepage for 30 days</li><li>A private number-strategy session</li></ul><button class="btn gold" type="button" data-amount="777">Choose $777</button></div>
  <div class="panel tier"><h3>Founding partner</h3><div class="price">$7,777</div><ul><li>Named sponsor of a tool for 12 months</li><li>Co-branded research report</li><li>First conversation on partnerships</li></ul><button class="btn" type="button" data-amount="7777">Choose $7,777</button></div>
</div>

<div class="grid g2" style="margin-top:28px">
  <div class="panel big">
    <h2>Where the money goes</h2>
    <table><tr><th>Use</th><th>Share</th></tr>
    <tr><td>Operations — hosting, data, tools, security</td><td>25%</td></tr>
    <tr><td>Hiring talent — writers, researchers, developers, video creators</td><td>30%</td></tr>
    <tr><td>Contests and prizes</td><td>20%</td></tr>
    <tr><td>Promotion and marketing — reaching new readers</td><td>15%</td></tr>
    <tr><td>Reserve for new projects</td><td>10%</td></tr></table>
    <p class="muted">This is how we plan to allocate support; we publish a summary of actual spending each quarter on this page.</p>
    <h3>Current goal: fund the next three tools</h3>
    <div class="progress" aria-label="Goal progress"><i style="width:12%"></i></div>
    <p class="form-note">Next tools: number-plate pattern checker, birthday-number compatibility, and a monthly numeric-domain sales tracker.</p>
  </div>
  <div class="panel big" id="pledge">
    <h2>Give now</h2>
    <div class="btn-row">
      <a class="btn gold" data-pay="paypal" hidden>Give with PayPal</a>
      <a class="btn" data-pay="stripe" hidden>Pay by card</a>
      <a class="btn" data-pay="buymeacoffee" hidden>Buy us a coffee</a>
      <a class="btn" data-pay="kofi" hidden>Support on Ko-fi</a>
    </div>
    <div data-if-nopay>
      <p>Pledge below and we will send you a secure payment link by email within one business day. Choose one-time or monthly.</p>
    </div>
    <form class="lead" data-relay="Support pledge">
      {honeypot()}
      <div class="row">
        <div><label for="pledge-amount">Amount (USD)</label><select id="pledge-amount" name="amount" required><option value="7">$7</option><option value="17">$17</option><option value="77" selected>$77</option><option value="177">$177</option><option value="777">$777</option><option value="7777">$7,777</option><option value="other">Other amount</option></select></div>
        <div><label for="pledge-freq">Frequency</label><select id="pledge-freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div>
      </div>
      <label for="pledge-for">Put it toward</label>
      <select id="pledge-for" name="designation"><option>Wherever it's needed most</option><option>Operations</option><option>Hiring talent</option><option>Contests and prizes</option><option>Promotion and marketing</option></select>
      <div class="row">
        <div><label for="p-name">Name</label><input id="p-name" name="name" required autocomplete="name"></div>
        <div><label for="p-email">Email</label><input id="p-email" type="email" name="email" required autocomplete="email"></div>
      </div>
      <label class="check"><input type="checkbox" name="public_thanks" value="yes"> Thank me publicly on the supporters list</label>
      <label for="p-msg">Message (optional)</label><textarea id="p-msg" name="message" rows="3"></textarea>
      {consent("I understand support is a voluntary contribution, not a purchase, and is not tax-deductible.")}
      <div class="btn-row"><button class="btn gold" type="submit">Send my pledge</button></div>
      <p class="form-status" role="status"></p>
    </form>
  </div>
</div>
<div class="prose" style="margin-top:32px"><h2>Other ways to help</h2><ul><li>Share a tool with someone who will use it.</li><li>Send corrections and ideas through the <a href="/contact.html">contact form</a>.</li><li><a href="/careers.html">Contribute</a> research, writing, code or video.</li><li><a href="/advertise.html">Sponsor</a> a tool, a contest or the newsletter.</li></ul></div>
</div></section>
"""
    return page("/support.html", "Support 017777 — Keep the Number Tools Free",
                "Support 017777.com from $7. Contributions fund operations, new tools, contest prizes, marketing and paid contributors.", body)


def contests():
    faqs = [
        ("Do I need to buy anything to enter?", "No. Entry is free. Purchases or donations do not improve your chances."),
        ("Who can enter?", "Anyone 18 or older (or the age of majority where they live), except where prohibited by law. One entry per person per contest."),
        ("How are winners chosen?", "All correct entries received before the deadline go into a random draw. Winners are contacted by email and announced on this page with their permission."),
    ]
    body = page_head("Contests and prizes",
                     "Monthly number puzzles, a creator challenge and a tool-idea prize. Free to enter.",
                     [("/contests.html", "Contests")]) + f"""
<section class="block"><div class="wrap grid g2">
<div class="panel big">
  <span class="tag">Open now</span>
  <h2>The Lucky 7 Challenge</h2>
  <p><strong>This month's puzzle:</strong> 17,777 is divisible by its own digit sum (29). It uses only the digits 1 and 7 and contains four 7s. Find the <em>next</em> number after 17,777 that uses only 1s and 7s, contains at least four 7s, and is divisible by its own digit sum.</p>
  <p>Use any method — the <a href="/tools.html#decoder">decoder</a> is allowed. Prize: a $77 gift card for one randomly drawn correct entry; runners-up get a feature in the newsletter.</p>
  <form class="lead" data-relay="Contest entry">
    {honeypot()}
    <input type="hidden" name="contest" value="Lucky 7 Challenge">
    <label for="c-answer">Your answer</label><input id="c-answer" name="answer" inputmode="numeric" required>
    <label for="c-work">How you found it (optional)</label><textarea id="c-work" name="method" rows="3"></textarea>
    <div class="row">
      <div><label for="c-name">Name</label><input id="c-name" name="name" required autocomplete="name"></div>
      <div><label for="c-email">Email</label><input id="c-email" type="email" name="email" required autocomplete="email"></div>
    </div>
    <label class="check"><input type="checkbox" name="age" value="18+" required> I am 18 or older (or the age of majority where I live).</label>
    <label class="check"><input type="checkbox" name="rules" value="accepted" required> I accept the <a href="#rules">official rules</a>.</label>
    <label class="check"><input type="checkbox" name="newsletter" value="yes"> Also send me the weekly newsletter.</label>
    <div class="btn-row"><button class="btn gold" type="submit">Submit my entry</button></div>
    <p class="form-status" role="status"></p>
  </form>
</div>
<div>
  <div class="panel"><span class="tag">Quarterly</span><h3>Number Story creator challenge</h3><p>Make a short video, post or graphic explaining a surprising fact about any number. Best entry wins $177 and is featured on our videos page. Send your link through the form with “creator challenge” in the answer box.</p></div>
  <div class="panel" style="margin-top:20px"><span class="tag">Always open</span><h3>Tool idea prize</h3><p>Suggest a number tool. If we build it, you get credit on the tool and a $27 thank-you. <a href="/contact.html">Send an idea</a>.</p></div>
  <div class="panel" style="margin-top:20px"><h3>Sponsor a prize</h3><p>Put your brand on a contest seen by number-curious readers. <a href="/advertise.html">See sponsorship options</a>.</p></div>
</div>
</div>
<div class="wrap prose" id="rules" style="margin-top:40px">
<h2>Official rules (summary)</h2>
<ol>
<li><strong>No purchase necessary.</strong> A purchase or donation does not increase your chances of winning.</li>
<li><strong>Eligibility.</strong> Open to individuals 18+ (or the age of majority in their jurisdiction). Void where prohibited. Employees and contractors of 017777.com and their households may not win.</li>
<li><strong>Entry period.</strong> Each monthly contest opens on the 1st and closes at 23:59 UTC on the last day of the month. One entry per person.</li>
<li><strong>Selection.</strong> One winner is drawn at random from all correct entries within 7 days of the close. Odds depend on the number of correct entries.</li>
<li><strong>Prizes.</strong> Prizes are as described, non-transferable, and may be substituted with a prize of equal or greater value. Winners are responsible for any taxes.</li>
<li><strong>Notification.</strong> Winners are emailed and must reply within 14 days or a new winner is drawn.</li>
<li><strong>Privacy.</strong> Entry data is used only to run the contest and, if you opt in, the newsletter. See the <a href="/privacy.html">privacy policy</a>.</li>
<li><strong>General.</strong> We may cancel or modify a contest if fraud or technical failure affects it. Contests are not sponsored, endorsed or administered by Google, YouTube or any social platform.</li>
</ol>
<h2>Questions</h2>{faq_html(faqs)}
</div></section>
"""
    return page("/contests.html", "Lucky 7 Challenge & Number Contests with Prizes | 017777",
                "Free monthly number puzzle contests with prizes, a quarterly creator challenge and a tool-idea prize. No purchase necessary.", body, [faq_ld(faqs)])


def careers():
    body = page_head("Careers and contributors",
                     "We pay people who make numbers clear. Remote, flexible, project-based.",
                     [("/careers.html", "Careers")]) + f"""
<section class="block"><div class="wrap layout-side"><div>
<div class="grid g2">
  <div class="panel"><h3>Research writer</h3><p>Turn studies and data on pricing, culture and economics into clear, sourced articles. Paid per article.</p></div>
  <div class="panel"><h3>Front-end developer</h3><p>Build fast, accessible, dependency-free JavaScript tools. Paid per tool.</p></div>
  <div class="panel"><h3>Video creator</h3><p>Short explainers on number facts for YouTube and social. Paid per video plus revenue share on sponsored series.</p></div>
  <div class="panel"><h3>Translator</h3><p>Spanish, Hindi, Chinese, Korean and Japanese editions of our most popular pages.</p></div>
  <div class="panel"><h3>Numeric domain analyst</h3><p>Track monthly numeric domain sales and write the market summary.</p></div>
  <div class="panel"><h3>Community and contest manager</h3><p>Run monthly contests, verify entries and grow the newsletter.</p></div>
</div>
<div class="panel big" style="margin-top:24px">
  <h2>Apply</h2>
  <form class="lead" data-relay="Job application">
    {honeypot()}
    <div class="row">
      <div><label for="j-name">Name</label><input id="j-name" name="name" required autocomplete="name"></div>
      <div><label for="j-email">Email</label><input id="j-email" type="email" name="email" required autocomplete="email"></div>
    </div>
    <div class="row">
      <div><label for="j-role">Role</label><select id="j-role" name="role" required><option value="">Choose a role</option><option>Research writer</option><option>Front-end developer</option><option>Video creator</option><option>Translator</option><option>Numeric domain analyst</option><option>Community and contest manager</option><option>Other</option></select></div>
      <div><label for="j-loc">Location / time zone</label><input id="j-loc" name="location"></div>
    </div>
    <label for="j-port">Portfolio, LinkedIn or samples (links)</label><input id="j-port" name="portfolio" type="url" placeholder="https://" required>
    <label for="j-rate">Rate expectation</label><input id="j-rate" name="rate" placeholder="e.g. $150 per article">
    <label for="j-why">Why this role, in a few lines</label><textarea id="j-why" name="message" rows="4" required></textarea>
    {consent("I agree that 017777.com may keep my application for 12 months to consider me for roles.")}
    <div class="btn-row"><button class="btn gold" type="submit">Send my application</button></div>
    <p class="form-status" role="status"></p>
  </form>
</div></div>
<aside><div class="panel"><h3>How we work</h3><ul><li>Paid test task before ongoing work</li><li>Clear briefs and fixed rates</li><li>Credit on everything you publish</li><li>Payment within 14 days of approval</li></ul></div></aside>
</div></section>
"""
    return page("/careers.html", "Careers at 017777: Writers, Developers, Video Creators & Analysts",
                "Remote, paid contributor roles: research writers, JavaScript tool developers, video creators, translators, numeric domain analysts and community managers.", body)


def advertise():
    body = page_head("Advertise, sponsor or partner",
                     "Reach readers who are actively thinking about prices, phone numbers, domains and data.",
                     [("/advertise.html", "Advertise")]) + f"""
<section class="block"><div class="wrap">
<div class="grid g3">
  <div class="panel tier"><h3>Tool sponsorship</h3><p>Your brand on one tool page (for example the charm-price calculator) with a short description and link.</p><ul><li>Monthly or yearly</li><li>Clearly labelled “Sponsored”</li></ul></div>
  <div class="panel tier"><h3>Newsletter sponsorship</h3><p>One sponsor slot per weekly issue, written in our voice with your link.</p><ul><li>Single issue or a 4-issue pack</li></ul></div>
  <div class="panel tier"><h3>Contest prizes</h3><p>Supply or fund a prize and be named as the contest sponsor.</p><ul><li>Monthly puzzle or creator challenge</li></ul></div>
  <div class="panel tier"><h3>Sponsored research</h3><p>A co-branded report on a numbers topic in your industry. Our editorial standards apply; findings are not for sale.</p></div>
  <div class="panel tier"><h3>Video series</h3><p>Sponsor a series of short explainers produced for YouTube and social.</p></div>
  <div class="panel tier feature"><h3>Domain & site partnership</h3><p>Interested in acquiring, licensing or partnering on 017777.com itself?</p><a class="btn gold" href="{OWNER_URL}" target="_blank" rel="noopener">Contact the owner</a></div>
</div>
<div class="panel big" style="margin-top:28px">
  <h2>Request the media kit</h2>
  <form class="lead" data-relay="Advertising inquiry">
    {honeypot()}
    <div class="row">
      <div><label for="a-name">Name</label><input id="a-name" name="name" required autocomplete="name"></div>
      <div><label for="a-email">Work email</label><input id="a-email" type="email" name="email" required autocomplete="email"></div>
    </div>
    <div class="row">
      <div><label for="a-co">Company</label><input id="a-co" name="company" required autocomplete="organization"></div>
      <div><label for="a-web">Website</label><input id="a-web" name="website" type="url" placeholder="https://"></div>
    </div>
    <div class="row">
      <div><label for="a-type">Interested in</label><select id="a-type" name="interest" required><option value="">Choose one</option><option>Tool sponsorship</option><option>Newsletter sponsorship</option><option>Contest prizes</option><option>Sponsored research</option><option>Video series</option><option>Domain / site partnership</option></select></div>
      <div><label for="a-bud">Monthly budget</label><select id="a-bud" name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div>
    </div>
    <label for="a-msg">Goals and timing</label><textarea id="a-msg" name="message" rows="4"></textarea>
    {consent()}
    <div class="btn-row"><button class="btn gold" type="submit">Request the media kit</button></div>
    <p class="form-status" role="status"></p>
  </form>
</div>
<div class="prose" style="margin-top:28px"><h2>Our standards</h2><ul><li>All paid placements are labelled.</li><li>We do not accept ads for gambling, get-rich-quick schemes, or anything claiming numbers predict outcomes.</li><li>Display advertising on this site is served by Google AdSense under Google's policies.</li></ul></div>
</div></section>
"""
    return page("/advertise.html", "Advertise & Sponsor on 017777 — Tools, Newsletter, Contests, Partnerships",
                "Sponsorship options on 017777.com: tool sponsorships, newsletter slots, contest prizes, sponsored research, video series and domain partnerships.", body)


def about():
    body = page_head("About 017777", "A number-intelligence hub that treats numbers seriously and belief respectfully.", [("/about.html", "About")]) + f"""
<section class="block"><div class="wrap prose">
<h2>What we do</h2>
<p>017777.com publishes free, private number tools and plain-language research on how numbers shape commerce, technology, the economy and culture. The site grew out of a simple observation: people search for what numbers mean every day — prices, phone codes, repeating digits on clocks — and most answers online either drown the maths or oversell the mysticism. We separate the two.</p>
<h2>Our principles</h2>
<ul><li><strong>Maths first.</strong> Every number page starts with verifiable properties.</li>
<li><strong>Tradition labelled.</strong> Numerology and angel-number content is presented as culture and entertainment, never as prediction.</li>
<li><strong>Sources shown.</strong> Research claims link to their source. See our <a href="/editorial-policy.html">editorial policy</a>.</li>
<li><strong>Privacy by design.</strong> Tools run in your browser; we do not store what you type into them.</li></ul>
<h2>Why “017777”?</h2>
<p>Read as “01 7777,” the name pairs the binary digits of computing with the West's favourite lucky number, repeated. <a href="/meaning-of-017777.html">Read the full story</a>.</p>
<h2>How we are funded</h2>
<p>Advertising through Google AdSense, reader <a href="/support.html">support</a>, <a href="/advertise.html">sponsorships</a> and paid <a href="/number-strategy.html">strategy calls</a>. Sponsors never buy editorial conclusions.</p>
<h2>Contact</h2>
<p>Use the <a href="/contact.html">contact page</a>. For domain, sponsorship, advertising or partnership interest, <a href="{OWNER_URL}" target="_blank" rel="noopener">contact the owner</a>.</p>
</div></section>"""
    return page("/about.html", "About 017777 — Number Intelligence Hub", "Who we are, what we publish, how we keep maths and belief separate, and how 017777.com is funded.", body)


def contact():
    body = page_head("Contact us", "Questions, corrections, tool ideas or partnerships. We reply within two business days.", [("/contact.html", "Contact")]) + f"""
<section class="block"><div class="wrap layout-side"><div class="panel big">
  <form class="lead" data-relay="Contact">
    {honeypot()}
    <div class="row">
      <div><label for="ct-name">Name</label><input id="ct-name" name="name" required autocomplete="name"></div>
      <div><label for="ct-email">Email</label><input id="ct-email" type="email" name="email" required autocomplete="email"></div>
    </div>
    <label for="ct-topic">Topic</label>
    <select id="ct-topic" name="topic" required><option value="">Choose a topic</option><option>General question</option><option>Correction</option><option>Tool idea</option><option>Strategy call</option><option>Advertising / sponsorship</option><option>Partnership</option><option>Domain purchase inquiry</option><option>Press</option></select>
    <label for="ct-msg">Message</label><textarea id="ct-msg" name="message" rows="6" required></textarea>
    {consent()}
    <div class="btn-row"><button class="btn gold" type="submit">Send message</button></div>
    <p class="form-status" role="status"></p>
  </form>
</div>
<aside><div class="panel"><h3>Other ways to reach us</h3>
<p><a href="#" data-mail="Message from 017777.com">Email the team</a></p>
<p><a href="{OWNER_URL}" target="_blank" rel="noopener">Domain, sponsorship, advertising or partnership interest</a></p>
<p><a href="/number-strategy.html">Request a strategy call</a></p></div></aside>
</div></section>"""
    return page("/contact.html", "Contact 017777", "Contact the 017777.com team with questions, corrections, tool ideas, advertising or partnership inquiries.", body)


def legal(path, title, intro, html, desc):
    return page(path, title + " | 017777", desc, page_head(title, intro, [(path, title)]) +
                f'<section class="block"><div class="wrap prose"><p class="muted">Last updated {UPDATED}</p>{html}</div></section>')


def privacy():
    return legal("/privacy.html", "Privacy policy", "What we collect, why, and your choices.", """
<h2>Who we are</h2><p>017777.com (“we”) operates this website. Contact us through the <a href="/contact.html">contact page</a>.</p>
<h2>Information you give us</h2><p>When you submit a form (contact, strategy call, newsletter, pledge, contest entry, job application) we receive the details you enter. Form submissions are relayed to our inbox by a third-party form-forwarding service (FormSubmit). We use this information only to respond to you, run contests you enter, process pledges and send newsletters you request. We do not sell personal information.</p>
<h2>Tools</h2><p>Our number tools run in your browser. The numbers, names and dates you type into them are not sent to our servers.</p>
<h2>Cookies and advertising</h2><p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this site and/or other sites on the internet. You may opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" rel="noopener" target="_blank">Google Ads Settings</a> or <a href="https://www.aboutads.info/choices/" rel="noopener" target="_blank">aboutads.info</a>. Learn more at <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">how Google uses information from sites that use its services</a>.</p>
<p>We also store small preferences in your browser (theme, cookie choice). Embedded YouTube videos use privacy-enhanced mode and load only when you press play; once played, YouTube's own policies apply.</p>
<h2>Your rights</h2><p>Depending on where you live (for example under the GDPR, UK GDPR, PIPEDA, or CCPA/CPRA), you may request access to, correction of, or deletion of your personal information, and object to certain processing. Contact us and we will respond within 30 days. California residents: we do not sell or share personal information for cross-context behavioural advertising except through the advertising cookies described above, which you can control.</p>
<h2>Retention</h2><p>We keep form messages for up to 24 months, job applications for 12 months and contest entries for 12 months after a contest closes, unless the law requires longer.</p>
<h2>Children</h2><p>This site is not directed at children under 13, and contests are limited to adults.</p>
<h2>Changes</h2><p>We will post any changes on this page with a new date.</p>""",
                 "How 017777.com collects and uses information, Google AdSense advertising cookies, form handling and your privacy rights.")


def terms():
    return legal("/terms.html", "Terms of use", "The rules for using this site.", """
<h2>Acceptance</h2><p>By using 017777.com you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>Information only</h2><p>Content and tools are provided for general information, education and entertainment. They are not financial, investment, legal, tax or professional advice. Numerology, lucky-number and angel-number content reflects cultural traditions and is not a prediction of any outcome.</p>
<h2>Tool accuracy</h2><p>We work to keep calculations correct but provide tools “as is,” without warranties. Check important results independently.</p>
<h2>Intellectual property</h2><p>Original text, design and code on this site are owned by 017777.com. You may quote short excerpts with a link back. Embedded videos and linked sources belong to their owners.</p>
<h2>User submissions</h2><p>By sending ideas, contest entries or content, you confirm you have the right to share them and grant us a non-exclusive licence to use them for running and promoting the site, with credit where practical.</p>
<h2>Support and pledges</h2><p>Voluntary support is a contribution, not a purchase of goods or services, and is not tax-deductible. Benefits listed on the support page are thank-you gestures and may change.</p>
<h2>Links</h2><p>We are not responsible for third-party websites we link to.</p>
<h2>Liability</h2><p>To the extent permitted by law, 017777.com is not liable for indirect or consequential losses arising from use of the site.</p>
<h2>Changes</h2><p>We may update these terms; the date above shows the latest version.</p>""",
                 "Terms of use for 017777.com, including tool accuracy, intellectual property, submissions and support.")


def disclaimer():
    return legal("/disclaimer.html", "Disclaimer and trademark notice", "How we use the name 017777 and what our content is — and is not.", f"""
<h2>Trademark and name notice</h2>
<p>“017777” is used on this website solely as a domain name and descriptive site identifier. This site does not claim trademark rights in the numeric string “017777,” “01 7777,” “7777,” or any variation, and does not use them to identify the goods or services of any other party.</p>
<p>017777.com is <strong>not affiliated with, endorsed by, or connected to</strong> any telephone operator, telephone number holder, the 01777 (Retford, UK) dialling area, the former 017 South Korean mobile service, SK Telecom, any lottery or gaming operator, any government agency, or any company or product that uses the same or similar digits. References to such parties are factual and descriptive (nominative use) for education and commentary.</p>
<p>All other trademarks, product names and company names mentioned on this site are the property of their respective owners and are used for identification only.</p>
<h2>Copyright notice</h2>
<p>Original text, tools, code and design © {UPDATED[:4]} 017777.com. Numbers and mathematical facts are not subject to copyright. Quoted research is summarised in our own words with links to the original sources; embedded YouTube videos remain the property of their creators and are shown through YouTube's official embed player. If you believe any material infringes your rights, contact us via the <a href="/contact.html">contact page</a> and we will review and respond promptly.</p>
<h2>Content disclaimer</h2>
<p>Numerology, lucky-number and angel-number material is presented as cultural tradition and entertainment. It does not predict the future and should not be used for medical, financial, legal or safety decisions. Research summaries are educational, not professional advice. Contest participation is free, and lucky-number tools do not improve odds in any game of chance.</p>
<h2>Advertising disclosure</h2>
<p>This site displays ads served by Google AdSense and may carry clearly labelled sponsorships. Advertisers do not influence editorial content.</p>
<h2>Domain availability</h2>
<p>For inquiries about this website, the domain name, sponsorship, advertising or partnership, <a href="{OWNER_URL}" target="_blank" rel="noopener">contact the owner</a>.</p>""",
                 "Trademark notice for the name 017777, non-affiliation statement, copyright notice, numerology disclaimer and advertising disclosure.")


def editorial():
    return legal("/editorial-policy.html", "Editorial policy", "How we research, write and correct.", """
<h2>Sourcing</h2><p>Factual claims about research, history, telephony or markets link to a primary or reputable secondary source. We summarise in our own words.</p>
<h2>Maths is verified</h2><p>Every number property on the site is generated by the same open code that powers our decoder, and spot-checked by hand.</p>
<h2>Belief, clearly labelled</h2><p>Numerology and angel-number sections are marked as tradition and paired with the relevant psychology. We never claim numbers predict outcomes.</p>
<h2>Independence</h2><p>Advertisers and sponsors do not see or approve editorial content before publication. Sponsored items are labelled.</p>
<h2>Corrections</h2><p>Found an error? <a href="/contact.html">Tell us</a>. We correct factual errors promptly and update the “last reviewed” date.</p>
<h2>AI assistance</h2><p>We may use AI tools to help draft or check content. Every page is reviewed by a person, and facts are checked against sources before publication.</p>""",
                 "How 017777.com researches, sources, labels belief-based content, keeps sponsors independent and corrects errors.")


def thank_you():
    body = page_head("Thank you — we've got it", "Your <span id=\"ty-form\">form</span> was sent.", None) + """
<section class="block"><div class="wrap prose"><p>We reply within two business days. While you wait:</p>
<ul><li><a href="/tools.html">Decode another number</a></li><li><a href="/numbers/">Browse number meanings</a></li><li><a href="/contests.html">Enter this month's contest</a></li></ul>
<p class="form-note">First-time note: if you don't hear back, check your spam folder.</p></div></section>"""
    h = page("/thank-you.html", "Thank You | 017777", "Your submission was received.", body)
    return h.replace('content="index, follow, max-image-preview:large"', 'content="noindex, follow"')


def not_found():
    body = page_head("That page isn't here", "The link may be old or mistyped. Try the decoder or the links below.", None) + """
<section class="block"><div class="wrap prose"><form id="decoder-form" class="lead" data-start="404"><div class="row"><input name="n" inputmode="numeric" aria-label="Number"><button class="btn gold" type="submit">Decode</button></div></form><div class="tool-out" id="decoder-out"></div>
<p style="margin-top:20px"><a href="/">Home</a> · <a href="/tools.html">Tools</a> · <a href="/numbers/">Number meanings</a> · <a href="/sitemap.html">Sitemap</a></p></div></section>"""
    h = page("/404.html", "Page Not Found | 017777", "Page not found.", body)
    return h.replace('content="index, follow, max-image-preview:large"', 'content="noindex, follow"')


PAGES = {"number-strategy.html": strategy, "support.html": support, "contests.html": contests, "careers.html": careers,
         "advertise.html": advertise, "about.html": about, "contact.html": contact, "privacy.html": privacy, "terms.html": terms,
         "disclaimer.html": disclaimer, "editorial-policy.html": editorial, "thank-you.html": thank_you, "404.html": not_found}
