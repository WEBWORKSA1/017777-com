/* 017777.com — number analysis engine + interactive tools. No external dependencies. */
(function(){
  "use strict";
  var NUM = {};

  NUM.clean = function(s){ return String(s||"").replace(/[^0-9]/g,"").slice(0,30); };

  NUM.isPrime = function(n){
    if(n < 2n) return false;
    if(n % 2n === 0n) return n === 2n;
    if(n % 3n === 0n) return n === 3n;
    if(n > 1000000000000n) return null; // too large for quick trial division
    for(var i=5n; i*i<=n; i+=6n){ if(n%i===0n || n%(i+2n)===0n) return false; }
    return true;
  };
  NUM.factor = function(n){
    if(n < 2n || n > 1000000000000n) return null;
    var f=[], d=2n;
    while(d*d<=n){ while(n%d===0n){ f.push(d); n/=d; } d += (d===2n?1n:2n); }
    if(n>1n) f.push(n);
    return f;
  };
  NUM.roman = function(n){
    n = Number(n); if(!n || n>3999) return null;
    var m=[[1000,"M"],[900,"CM"],[500,"D"],[400,"CD"],[100,"C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]], r="";
    m.forEach(function(p){ while(n>=p[0]){ r+=p[1]; n-=p[0]; } }); return r;
  };
  NUM.digitalRoot = function(sum){ while(sum>9 && sum!==11 && sum!==22 && sum!==33){ sum = String(sum).split("").reduce(function(a,b){return a+ +b;},0);} return sum; };
  NUM.pattern = function(s){
    var p=[];
    if(/^(\d)\1+$/.test(s) && s.length>1) p.push("repdigit (one digit repeated)");
    if(s.length>1 && s === s.split("").reverse().join("")) p.push("palindrome");
    var run = s.match(/(\d)\1{2,}/g); if(run) p.push("contains a run of " + run.map(function(r){return r.length+"× "+r[0];}).join(", "));
    if(/^(?:0?1?2?3?4?5?6?7?8?9?)$/.test(s) && s.length>2) p.push("ascending sequence");
    if(/^(?:9?8?7?6?5?4?3?2?1?0?)$/.test(s) && s.length>2) p.push("descending sequence");
    if(s.length%2===0 && s.slice(0,s.length/2)===s.slice(s.length/2) && s.length>2) p.push("doubled half (e.g. 4242)");
    if(/^0/.test(s)) p.push("leading zero (reads like a dialling or trunk prefix)");
    return p;
  };
  NUM.keypad = {"2":"ABC","3":"DEF","4":"GHI","5":"JKL","6":"MNO","7":"PQRS","8":"TUV","9":"WXYZ","0":"(none)","1":"(none)"};

  /* Cultural notes per digit — tradition, not prediction. */
  NUM.culture = {
    "0":"Western: emptiness, a fresh start. Binary: the 'off' state. Chinese: líng, neutral; in phone numbers often read as 'you' in slang.",
    "1":"Western: firsts and leadership. Binary: the 'on' state. Chinese: yī/yāo, 'one/the only'. Japanese: ichi, the top rank.",
    "2":"Chinese: pairs are auspicious ('good things come in pairs'). Japanese: ni. Western: balance, partnership.",
    "3":"Chinese: sān sounds like 'birth/life' in some dialects. Western: completeness (beginning, middle, end).",
    "4":"Chinese/Japanese/Korean: sì / shi sounds like 'death' — buildings often skip floor 4 (tetraphobia).",
    "5":"Chinese: wǔ, linked to the five elements. Western: the human senses, change.",
    "6":"Chinese: liù sounds like 'flowing / smooth' — '666' means things are going great online.",
    "7":"Western: the most-chosen 'favourite number' and classic luck (777 jackpot). Chinese: qī — mixed: Qixi lovers' festival, but the 7th lunar month is Ghost Month. Japan: Seven Lucky Gods.",
    "8":"Chinese: bā sounds like fā ('prosper') — the most valued digit in prices, plates and phone numbers.",
    "9":"Chinese: jiǔ sounds like 'long-lasting'. Japanese: ku can sound like 'suffering'. Western retail: the default price ending."
  };
  NUM.prefixes = [
    ["01777","UK geographic dialling code for Retford, Nottinghamshire (Ofcom allocation; changed from 0777 in 1995)."],
    ["017","Legacy South Korean mobile prefix (Shinsegi Telecom, later SK Telecom). Retired in the 010 unification; SK's 2G network closed in 2020."],
    ["011","Legacy South Korean SK Telecom mobile prefix, retired with 2G. Also the international exit code from the US/Canada."],
    ["010","South Korea's unified mobile prefix since 2004."],
    ["00","International exit code used across most of Europe, India and much of the world."],
    ["0","Trunk prefix in the UK, India, Australia and many other countries (dropped when dialling from abroad)."],
    ["1","Country code shared by the US, Canada and the Caribbean (NANP)."],
    ["7","Country code for Russia and Kazakhstan."]
  ];
  NUM.prefixNote = function(s){
    for(var i=0;i<NUM.prefixes.length;i++){ if(s.indexOf(NUM.prefixes[i][0])===0) return NUM.prefixes[i]; }
    return null;
  };
  NUM.reflect = function(s){
    var uniq = Array.from(new Set(s.replace(/^0+/,"").split("")));
    if(!uniq.length) return "Zero-only sequences are read as 'potential' or a blank slate in most number-symbolism traditions.";
    var themes = {"1":"beginnings","2":"partnership","3":"expression","4":"structure","5":"change","6":"care","7":"reflection and study","8":"ambition and money","9":"completion","0":"potential"};
    return "Readers of 'angel number' traditions would frame this sequence around " + uniq.map(function(d){return themes[d];}).join(", ") +
      ". This is a belief tradition, not evidence — psychologists explain repeated sightings through the frequency illusion (you notice what is already on your mind).";
  };

  NUM.analyze = function(raw){
    var s = NUM.clean(raw); if(!s) return null;
    var n = BigInt(s), sum = s.split("").reduce(function(a,b){return a + +b;},0);
    var freq = {}; s.split("").forEach(function(d){ freq[d]=(freq[d]||0)+1; });
    var prime = NUM.isPrime(n), factors = NUM.factor(n);
    return {
      raw:s, value:n.toString(), digits:s.length, sum:sum, root:NUM.digitalRoot(sum),
      parity: n%2n===0n ? "even":"odd", prime: prime,
      factors: factors ? factors.map(String).join(" × ") : (n<2n ? "—" : "too large for quick factoring"),
      sumDivides: sum>0 && n % BigInt(sum) === 0n,
      bin:n.toString(2), hex:n.toString(16).toUpperCase(), oct:n.toString(8), roman:NUM.roman(n),
      pattern:NUM.pattern(s), freq:freq, prefix:NUM.prefixNote(s),
      keypad: s.split("").map(function(d){return NUM.keypad[d];}).join(" · "),
      reflect: NUM.reflect(s)
    };
  };

  function esc(t){ return String(t).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];}); }

  NUM.render = function(a){
    if(!a) return '<p class="muted">Type at least one digit.</p>';
    var primeTxt = a.prime===null ? "too large to test quickly" : (a.prime ? "yes — prime" : "no");
    var rows = [
      ["Number", a.raw + (a.raw!==a.value ? " (value " + a.value + ")" : "")],
      ["Digits", a.digits], ["Digit sum", a.sum + (a.sumDivides ? " — and it divides the number exactly (Harshad number)" : "")],
      ["Digital root", a.root + ([11,22,33].indexOf(a.root)>-1 ? " (a 'master number' in numerology)" : "")],
      ["Even / odd", a.parity], ["Prime?", primeTxt], ["Prime factors", a.factors],
      ["Binary", a.bin], ["Hexadecimal", "0x"+a.hex], ["Octal", a.oct]
    ];
    if(a.roman) rows.push(["Roman numerals", a.roman]);
    rows.push(["Phone keypad letters", a.keypad]);
    if(a.pattern.length) rows.push(["Patterns", a.pattern.join("; ")]);
    if(a.prefix) rows.push(["Prefix note", "Starts with " + a.prefix[0] + ": " + a.prefix[1]]);
    var html = "<dl>" + rows.map(function(r){return "<dt>"+esc(r[0])+"</dt><dd>"+esc(r[1])+"</dd>";}).join("") + "</dl>";
    var cultures = Object.keys(a.freq).sort().map(function(d){ return "<li><strong>"+d+"</strong> (×"+a.freq[d]+"): "+esc(NUM.culture[d])+"</li>"; }).join("");
    html += '<h4 style="margin-top:16px">What each digit means across cultures</h4><ul>'+cultures+'</ul>';
    html += '<p class="callout" style="margin-bottom:0"><strong>Belief lens:</strong> '+esc(a.reflect)+'</p>';
    return html;
  };

  /* Pythagorean numerology */
  NUM.letterVal = function(ch){ var c = ch.toUpperCase().charCodeAt(0)-64; return (c>=1 && c<=26) ? ((c-1)%9)+1 : 0; };
  NUM.nameNumbers = function(name){
    var letters = name.replace(/[^a-z]/gi,"").split(""); if(!letters.length) return null;
    var vowels = "AEIOU", all=0, v=0, c=0;
    letters.forEach(function(l){ var x = NUM.letterVal(l); all+=x; if(vowels.indexOf(l.toUpperCase())>-1) v+=x; else c+=x; });
    return { expression:NUM.digitalRoot(all), soul:NUM.digitalRoot(v), personality:NUM.digitalRoot(c), letters:letters.length };
  };
  NUM.lifePath = function(dateStr){
    var d = dateStr.replace(/[^0-9]/g,""); if(d.length<8) return null;
    return NUM.digitalRoot(d.split("").reduce(function(a,b){return a+ +b;},0));
  };
  NUM.meaning = {1:"initiator, independent",2:"mediator, cooperative",3:"communicator, creative",4:"builder, methodical",5:"explorer, adaptable",6:"caretaker, responsible",7:"analyst, seeker of knowledge",8:"executive, results-driven",9:"humanitarian, big-picture",11:"intuitive visionary (master 11)",22:"master builder (master 22)",33:"master teacher (master 33)"};

  /* Charm pricing */
  NUM.charm = function(price){
    var p = parseFloat(price); if(!(p>0)) return null;
    var whole = Math.floor(p);
    return {
      ".99": (whole - (p===whole ? 1 : 0)) + 0.99,
      ".97": (whole - (p===whole ? 1 : 0)) + 0.97,
      ".95": (whole - (p===whole ? 1 : 0)) + 0.95,
      "round": Math.round(p),
      "lucky 8": Math.floor(p/10)*10 + 8,
      "lucky 7": Math.floor(p/10)*10 + 7
    };
  };

  /* Seeded lucky numbers — deterministic for fun, clearly not predictive */
  NUM.seeded = function(seedStr, count, max){
    var h = 2166136261;
    for(var i=0;i<seedStr.length;i++){ h ^= seedStr.charCodeAt(i); h = Math.imul(h, 16777619); }
    var out = [], guard=0;
    while(out.length<count && guard<500){ guard++; h ^= h<<13; h ^= h>>>17; h ^= h<<5; var v = (Math.abs(h) % max) + 1; if(out.indexOf(v)<0) out.push(v); }
    return out.sort(function(a,b){return a-b;});
  };

  /* Letters to keypad digits */
  NUM.wordToDigits = function(w){
    var map={}; Object.keys(NUM.keypad).forEach(function(k){ NUM.keypad[k].replace(/[^A-Z]/g,"").split("").forEach(function(l){map[l]=k;}); });
    return w.toUpperCase().split("").map(function(ch){ return map[ch] || (/[0-9]/.test(ch)?ch:""); }).join("");
  };

  /* Memorability score for a numeric string (domain, phone, plate). Heuristic, not an appraisal. */
  NUM.memorability = function(s){
    s = NUM.clean(s); if(!s) return null;
    var score = 100, notes=[];
    score -= Math.max(0, s.length-4)*9; if(s.length<=4) notes.push("short — the strongest single factor");
    var uniq = new Set(s.split("")).size; score += (s.length-uniq)*6; if(uniq<=2) notes.push("only "+uniq+" distinct digits");
    if(/(\d)\1{2,}/.test(s)) { score+=8; notes.push("contains a repeated run"); }
    if(s.indexOf("4")>-1){ score-=8; notes.push("contains 4 (avoided by East Asian buyers)"); }
    var eights = (s.match(/8/g)||[]).length; if(eights){ score+=eights*5; notes.push(eights+"× 8 (valued by Chinese-speaking buyers)"); }
    var sevens = (s.match(/7/g)||[]).length; if(sevens){ score+=sevens*3; notes.push(sevens+"× 7 (Western luck)"); }
    if(s===s.split("").reverse().join("") && s.length>2){ score+=6; notes.push("palindrome"); }
    score = Math.max(1, Math.min(100, score));
    var tier = score>=85?"Exceptional":score>=70?"Strong":score>=50?"Solid":score>=30?"Average":"Low";
    return {score:score, tier:tier, notes:notes};
  };

  window.NUM = NUM;

  /* ---------- Wire up tools present on the page ---------- */
  function $(id){ return document.getElementById(id); }
  function onSubmit(id, fn){ var f=$(id); if(f) f.addEventListener("submit", function(e){ e.preventDefault(); fn(f); }); }

  document.addEventListener("DOMContentLoaded", function(){
    // Full decoder
    onSubmit("decoder-form", function(f){
      var v = f.querySelector("input").value; $("decoder-out").innerHTML = NUM.render(NUM.analyze(v));
      try{ history.replaceState(null,"","#n="+NUM.clean(v)); }catch(e){}
    });
    if($("decoder-form")){
      var m = location.hash.match(/n=(\d+)/); var start = m ? m[1] : ($("decoder-form").dataset.start || "017777");
      $("decoder-form").querySelector("input").value = start;
      $("decoder-out").innerHTML = NUM.render(NUM.analyze(start));
    }
    onSubmit("name-form", function(f){
      var r = NUM.nameNumbers(f.name_input.value), lp = NUM.lifePath(f.dob.value||"");
      if(!r){ $("name-out").innerHTML = '<p class="form-status err">Enter a name using letters A–Z.</p>'; return; }
      var html = "<dl><dt>Expression</dt><dd>"+r.expression+" — "+NUM.meaning[r.expression]+"</dd><dt>Soul urge (vowels)</dt><dd>"+r.soul+" — "+NUM.meaning[r.soul]+"</dd><dt>Personality (consonants)</dt><dd>"+r.personality+" — "+NUM.meaning[r.personality]+"</dd>";
      if(lp) html += "<dt>Life path</dt><dd>"+lp+" — "+NUM.meaning[lp]+"</dd>";
      $("name-out").innerHTML = html + '</dl><p class="form-note">Pythagorean system. For reflection and entertainment — not a personality test.</p>';
    });
    onSubmit("charm-form", function(f){
      var r = NUM.charm(f.price.value), cost = parseFloat(f.cost.value)||0;
      if(!r){ $("charm-out").innerHTML = '<p class="form-status err">Enter a price above zero.</p>'; return; }
      var html = "<table><tr><th>Ending</th><th>Price</th><th>Margin</th></tr>";
      Object.keys(r).forEach(function(k){ var p=r[k], mg = cost ? ((p-cost)/p*100).toFixed(1)+"%" : "—"; html += "<tr><td>"+k+"</td><td>"+p.toFixed(2)+"</td><td>"+mg+"</td></tr>"; });
      $("charm-out").innerHTML = html + '</table><p class="form-note">Left-digit effect: dropping 20.00 to 19.99 changes the first digit buyers read. Test endings on your own traffic before committing.</p>';
    });
    onSubmit("rule72-form", function(f){
      var r = parseFloat(f.rate.value); if(!(r>0)){ $("rule72-out").innerHTML='<p class="form-status err">Enter a rate above 0.</p>'; return; }
      var est = 72/r, exact = Math.log(2)/Math.log(1+r/100);
      $("rule72-out").innerHTML = "<dl><dt>Rule of 72 estimate</dt><dd>"+est.toFixed(2)+" years</dd><dt>Exact (compound)</dt><dd>"+exact.toFixed(2)+" years</dd><dt>Error</dt><dd>"+Math.abs(est-exact).toFixed(2)+" years</dd></dl><p class='form-note'>Works for growth, inflation (how fast prices double) and user growth. Not financial advice.</p>";
    });
    onSubmit("lucky-form", function(f){
      var seed = (f.seed.value||"") + "|" + (f.date.value||new Date().toISOString().slice(0,10));
      var nums = NUM.seeded(seed, parseInt(f.count.value,10)||6, parseInt(f.max.value,10)||49);
      $("lucky-out").innerHTML = '<div class="kv">'+nums.map(function(n){return "<span>"+n+"</span>";}).join("")+'</div><p class="form-note">Same name and date always give the same set. Lottery draws are random — no number set has better odds than any other.</p>';
    });
    onSubmit("base-form", function(f){
      var v = f.val.value.trim(), from = parseInt(f.from.value,10), n;
      try{ n = from===10 ? BigInt(v) : BigInt((from===16?"0x":from===2?"0b":"0o")+v); }catch(e){ $("base-out").innerHTML='<p class="form-status err">That value is not valid in base '+from+'.</p>'; return; }
      $("base-out").innerHTML = "<dl><dt>Decimal</dt><dd>"+n.toString(10)+"</dd><dt>Binary</dt><dd>"+n.toString(2)+"</dd><dt>Octal</dt><dd>"+n.toString(8)+"</dd><dt>Hex</dt><dd>"+n.toString(16).toUpperCase()+"</dd></dl>";
    });
    onSubmit("word-form", function(f){
      var d = NUM.wordToDigits(f.word.value);
      $("word-out").innerHTML = d ? "<dl><dt>Dial</dt><dd>"+d+"</dd><dt>Digits</dt><dd>"+d.length+"</dd></dl>" : '<p class="form-status err">Type letters or digits.</p>';
    });
    onSubmit("memo-form", function(f){
      var r = NUM.memorability(f.num.value);
      if(!r){ $("memo-out").innerHTML='<p class="form-status err">Type a numeric string.</p>'; return; }
      $("memo-out").innerHTML = '<p><span class="stat">'+r.score+'</span> / 100 — <strong>'+r.tier+'</strong></p><div class="progress"><i style="width:'+r.score+'%"></i></div><ul>'+r.notes.map(function(n){return "<li>"+n+"</li>";}).join("")+'</ul><p class="form-note">A memorability heuristic, not a valuation. For a human review of a domain, phone number or brand number, <a href="/number-strategy.html">request a strategy call</a>.</p>';
    });
  });
})();
