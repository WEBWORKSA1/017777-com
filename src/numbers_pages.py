"""Generates /numbers/*.html — one page per notable number, maths first, tradition labelled."""
from layout import *
import math

DIGIT = {
    "0": dict(name="zero", theme="potential, blank slates and the whole cycle", culture="Zero as a written number with its own value is credited to Indian mathematicians; in binary it is the 'off' state that half of all computing rests on.",
              commerce="Zeros make prices look round and premium (100, 1,000). Strings of zeros in phone numbers are easy to say but easy to mis-dial.", clock="00:00 (midnight)"),
    "1": dict(name="one", theme="new beginnings, initiative and focus", culture="One means first and unique in most cultures; in Indian gift-giving an extra 1 (101, 501, 1001) turns a round sum into a fresh start.",
              commerce="Ones read as 'first' and 'number one' — common in rankings, hotlines and brand names.", clock="11:11 and 1:11"),
    "2": dict(name="two", theme="partnership, balance and patience", culture="In Chinese tradition good things come in pairs, so doubled digits (22, 88) are favoured for weddings and openings.",
              commerce="Pairs suggest bundles and two-for-one offers.", clock="2:22 and 22:22"),
    "3": dict(name="three", theme="creativity, expression and growth", culture="Three signals completeness in Western storytelling and is considered lucky in Korean tradition; in Hinduism it echoes the trimurti.",
              commerce="The 'rule of three' drives good-better-best pricing tiers.", clock="3:33"),
    "4": dict(name="four", theme="structure, hard work and stability", culture="In Chinese, Japanese and Korean, four sounds like the word for death, so many buildings skip fourth floors and buyers avoid 4s in phone numbers and plates.",
              commerce="Remove 4s from prices, plates, room numbers and phone numbers aimed at East Asian buyers — it is one of the strongest number effects in commerce.", clock="4:44"),
    "5": dict(name="five", theme="change, freedom and movement", culture="Five links to the five elements in Chinese philosophy and the five senses in the West.",
              commerce="Five-star ratings made 5 the universal symbol of quality.", clock="5:55"),
    "6": dict(name="six", theme="care, home and responsibility", culture="In Chinese, six sounds like 'smooth, flowing', and '666' is online slang for 'awesome'; in parts of the West, 666 carries negative religious associations.",
              commerce="Six-heavy numbers sell well to Chinese-speaking buyers; test before using 666 with Western audiences.", clock="6:06 and 16:16"),
    "7": dict(name="seven", theme="reflection, study and inner wisdom", culture="Seven is the West's classic lucky number — seven days, seven wonders, the 777 jackpot — and Japan has its Seven Lucky Gods. In Chinese it is mixed: the romantic Qixi festival, but also the seventh-month Ghost Month.",
              commerce="Seven-endings (27, 47, 97) are an internet-marketing habit; research favours 9-endings in general retail. Repeating sevens make memorable phone numbers and domains in Western markets.", clock="7:07 and 17:17"),
    "8": dict(name="eight", theme="ambition, abundance and achievement", culture="In Chinese, eight (bā) sounds like 'prosper' (fā). The Beijing Olympics opened at 8 pm on 8/8/2008, and phone numbers and plates full of 8s sell at large premiums.",
              commerce="The single most valuable digit for Chinese-speaking buyers of prices, plates, phone numbers and numeric domains.", clock="8:08 and 18:18"),
    "9": dict(name="nine", theme="completion, compassion and endings", culture="In Chinese, nine sounds like 'long-lasting', which makes it popular for weddings; in Japanese, ku can sound like 'suffering'.",
              commerce="Nine is the default retail price ending because of the left-digit effect (19.99 reads as 19).", clock="9:09 and 19:19"),
}

SPECIAL = {
    "7": "Seven is the fourth prime number, and 1/7 = 0.142857142857… repeats with a six-digit cycle — the longest possible for a divisor of 7. Its real fame is cultural, though. Ask people for a random number between 1 and 10 and 7 comes up far more often than 1 in 10.",
    "11": "Eleven is the smallest two-digit prime and the first repdigit. In numerology it is the first 'master number' and is not reduced to 2. On clocks, 11:11 is the most-shared repeating time online.",
    "22": "Twenty-two = 2 × 11. Numerology calls it the 'master builder' number. 22/7 is the classic fraction approximation of π (3.142857…).",
    "33": "Thirty-three = 3 × 11, the third 'master number' in numerology. It is also the sum of the first four factorials: 1! + 2! + 3! + 4! = 33.",
    "77": "Seventy-seven = 7 × 11. It is the sum of the first eight prime numbers (2+3+5+7+11+13+17+19 = 77).",
    "88": "Eighty-eight = 8 × 11. A standard piano has 88 keys, and in Chinese 88 reads like 'bye-bye' in text slang as well as 'double prosperity'.",
    "777": "777 = 3 × 7 × 37 — and every three-digit repdigit is divisible by 37 (777 = 21 × 37). It is the classic slot-machine jackpot, and the name of Boeing's long-haul twin-jet.",
    "888": "888 = 2³ × 3 × 37 = 24 × 37. In Chinese culture it reads as triple prosperity and appears in shop names, prices and phone numbers.",
    "111": "111 = 3 × 37. Every three-digit repdigit ddd equals d × 111, which is why they all share the factor 37.",
    "444": "444 = 2² × 3 × 37. Because four sounds like 'death' in Chinese, Japanese and Korean, 444 is the most avoided triple in East Asian commerce — while Western angel-number writers read it as protection.",
    "666": "666 = 2 × 3² × 37, and it is also the sum of the first 36 positive integers (a triangular number). In Chinese internet slang it means 'awesome'.",
    "1111": "1111 = 11 × 101. 11:11 is the most widely shared 'make a wish' time.",
    "7777": "7777 = 7 × 11 × 101. Every four-digit repdigit dddd = d × 1111 = d × 11 × 101. As four repeated sevens it is one of the most memorable Western 'lucky' strings for phone numbers and domains.",
    "8888": "8888 = 2³ × 11 × 101. Phone numbers, plates and domains built on 8888 are among the most valuable numeric assets for Chinese-speaking buyers.",
    "1234": "1234 = 2 × 617. It is the most common four-digit PIN in leaked-password studies, which makes it a perfect example of a memorable number you should never use for security.",
    "1212": "1212 = 2² × 3 × 101. Its 12:12 clock sighting is a frequent angel-number search.",
    "1717": "1717 = 17 × 101. Any four-digit 'abab' number equals ab × 101.",
    "17777": "17777 = 29 × 613, and its digit sum is 29, so it is divisible by its own digit sum (a Harshad number). Written with a leading zero, 017777, it is the number this site is named after.",
}

NUMBERS = ["7", "11", "22", "33", "77", "88"] + [d * 3 for d in "0123456789"] + [d * 4 for d in "0123456789"] + ["1212", "1234", "1717", "17777"]


def factors(n):
    if n < 2:
        return "—"
    f, d = [], 2
    while d * d <= n:
        while n % d == 0:
            f.append(d); n //= d
        d += 1
    if n > 1:
        f.append(n)
    return " × ".join(map(str, f))


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(math.isqrt(n)) + 1))


def roman(n):
    if n <= 0 or n > 3999:
        return "—"
    m = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    r = ""
    for v, s in m:
        while n >= v:
            r += s; n -= v
    return r


def droot(s):
    while s > 9 and s not in (11, 22, 33):
        s = sum(map(int, str(s)))
    return s


def slug(s):
    return s


def number_page(s):
    n = int(s)
    digits = sorted(set(s))
    dsum = sum(map(int, s))
    main = DIGIT[s[0]] if len(digits) == 1 else DIGIT["7"] if s == "17777" else DIGIT[digits[-1]]
    rows = [("Value", f"{n:,}"), ("Prime?", "Yes" if is_prime(n) else "No"), ("Prime factors", factors(n)),
            ("Digit sum", f"{dsum}" + (" (divides the number: Harshad)" if dsum and n % dsum == 0 else "")),
            ("Digital root", str(droot(dsum))), ("Binary", bin(n)[2:]), ("Hexadecimal", "0x" + format(n, "X")), ("Roman numerals", roman(n)),
            ("Square root", f"{math.sqrt(n):.4f}")]
    table = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    cult = "".join(f"<li><strong>{d} ({DIGIT[d]['name']}):</strong> {DIGIT[d]['culture']}</li>" for d in digits)
    comm = "".join(f"<li>{DIGIT[d]['commerce']}</li>" for d in digits)
    themes = ", ".join(DIGIT[d]["theme"] for d in digits)
    special = SPECIAL.get(s, f"{n:,} is a repdigit — one digit repeated — so it equals {s[0]} × {'1' * len(s)}, and it shares every factor of {'1' * len(s)} ({factors(int('1' * len(s)))}).")
    rel = [x for x in NUMBERS if x != s and (x[0] == s[0] or len(x) == len(s))][:8]
    rel_html = "".join(f'<a href="/numbers/{x}.html"><span>{x}</span></a>' for x in rel)
    clock = DIGIT[s[0]]["clock"] if len(digits) == 1 else "—"
    faqs = [
        (f"What does {s} mean?", f"Mathematically, {n:,} = {factors(n) if n > 1 else n}. In angel-number and numerology traditions, {s} is read around {themes}. Those readings are cultural beliefs, not predictions."),
        (f"Is {s} a lucky number?", f"It depends on culture. {main['culture']}"),
        (f"Why do I keep seeing {s}?", "Psychologists point to the frequency illusion (Baader–Meinhof phenomenon): once a pattern is on your mind, you notice it more, and each match feels significant. Clocks, receipts and plates show repeating digits more often than people expect."),
    ]
    body = page_head(f"{s}: meaning, maths and lucky-number lore",
                     f"The number {s} decoded — its mathematics first, then what cultures and belief traditions say about it, and how businesses use it.",
                     [("/numbers/", "Number meanings"), (None, s)]) + f"""
<section class="block"><div class="wrap layout-side"><article class="prose">
{byline()}
<h2>The maths of {s}</h2>
<p>{special}</p>
<table><tr><th>Property</th><th>Value</th></tr>{table}</table>

<h2>{s} across cultures</h2>
<ul>{cult}</ul>

<h2>{s} in business and commerce</h2>
<ul>{comm}</ul>

<h2>{s} as an “angel number” <span class="tag">Belief tradition</span></h2>
<p>Angel-number writers read {s} as a message about {themes}. Repeated digits are said to amplify the meaning of the base digit. Common moments people report seeing it: {clock}.</p>
<div class="callout"><strong>What the evidence says:</strong> there is no scientific evidence that numbers carry messages. The experience is real, though: the frequency illusion makes recently noticed patterns seem to appear everywhere. Use these readings as prompts for reflection, not as guidance for money, health or safety decisions.</div>

<h2>Questions</h2>
{faq_html(faqs)}
</article>
<aside><div class="panel">
<h3>Decode any number</h3>
<form id="decoder-form" data-start="{s}"><input style="width:100%;padding:10px;border-radius:6px;border:1px solid var(--line)" name="n" inputmode="numeric" aria-label="Number"><button class="btn" style="margin-top:8px;width:100%">Decode</button></form>
<div class="tool-out" id="decoder-out"></div>
<h3 style="margin-top:18px">Related numbers</h3><div class="kv">{rel_html}</div>
<p style="margin-top:14px"><a class="btn gold" href="/number-strategy.html">Own a {s} domain or phone number?</a></p>
</div></aside>
</div></section>
"""
    return page(f"/numbers/{s}.html", f"{s} Meaning: Maths, Angel Number, Luck & Business | 017777",
                f"What {s} means: {n:,} = {factors(n) if n > 1 else n}, its binary and Roman forms, what it means in Chinese, Japanese and Western culture, and the {s} angel number tradition explained.",
                body, [faq_ld(faqs)])


def index_page():
    groups = [("Single and double digits", ["7", "11", "22", "33", "77", "88"]),
              ("Triple repeating numbers", [d * 3 for d in "0123456789"]),
              ("Quadruple repeating numbers", [d * 4 for d in "0123456789"]),
              ("Patterns and notable numbers", ["1212", "1234", "1717", "17777"])]
    html = ""
    for title, nums in groups:
        html += f"<h2>{title}</h2><div class='grid g4'>" + "".join(
            f'<a class="panel" style="text-decoration:none;color:inherit" href="/numbers/{x}.html"><span class="stat">{x}</span><p class="muted" style="margin:.4em 0 0">{DIGIT[x[-1]]["theme"].split(",")[0].capitalize()}</p></a>' for x in nums) + "</div>"
    body = page_head("Number meanings library",
                     "Repeating numbers from 000 to 9999, master numbers and notable patterns. Every page leads with verifiable maths, then labels tradition as tradition.",
                     [("/numbers/", "Number meanings")]) + f"""
<section class="block"><div class="wrap">
<div class="prose"><p>Not finding your number? <a href="/tools.html">Decode any number</a> instantly, or <a href="/contact.html">request a page</a>. New pages are added every month based on reader requests.</p></div>
{html}
<div class="prose" style="margin-top:36px"><h2>How to read these pages</h2><p>Each page has three clearly separated layers: <strong>maths</strong> (factors, primes, bases — verifiable), <strong>culture</strong> (what the digits mean across Chinese, Japanese, Korean, Indian and Western traditions — documented belief), and <strong>angel-number tradition</strong> (a modern belief system, labelled as such, with the psychology that explains why repeating numbers feel meaningful).</p></div>
</div></section>"""
    return page("/numbers/", "Number Meanings: Angel Numbers 000–9999, Master Numbers & Lucky Numbers | 017777",
                "A library of number meanings — 111, 222, 777, 888, 1111, 7777 and more — with maths, cultural luck across five traditions, business uses and the angel-number tradition explained.", body)


def build_all():
    out = {"numbers/index.html": index_page()}
    for s in NUMBERS:
        out[f"numbers/{s}.html"] = number_page(s)
    return out
