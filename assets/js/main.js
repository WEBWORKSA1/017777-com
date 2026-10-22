/* 017777.com — site behaviour */
(function(){
  "use strict";
  var S = window.SITE || {};
  function addr(){ try{ return atob(S._k[0]).split("").reverse().join("") + "@" + atob(S._k[1]).split("").reverse().join(""); }catch(e){ return ""; } }
  function $(s,c){ return (c||document).querySelector(s); }
  function $$(s,c){ return Array.prototype.slice.call((c||document).querySelectorAll(s)); }

  document.addEventListener("DOMContentLoaded", function(){
    // Mobile nav
    var btn = $(".menu-btn"), nav = $(".nav");
    if(btn && nav) btn.addEventListener("click", function(){ var o = nav.classList.toggle("open"); btn.setAttribute("aria-expanded", o); });

    // Theme toggle
    var tt = $(".theme-toggle");
    try{ var saved = localStorage.getItem("theme"); if(saved) document.documentElement.setAttribute("data-theme", saved); }catch(e){}
    if(tt) tt.addEventListener("click", function(){
      var cur = document.documentElement.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark":"light");
      var next = cur==="dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      try{ localStorage.setItem("theme", next); }catch(e){}
    });

    // Year
    $$(".year").forEach(function(el){ el.textContent = new Date().getFullYear(); });

    // Email links: address assembled only on click, never written into the page
    $$("[data-mail]").forEach(function(a){
      a.addEventListener("click", function(e){
        e.preventDefault();
        var subj = encodeURIComponent(a.getAttribute("data-mail") || "Inquiry from 017777.com");
        window.location.href = "mai" + "lto:" + addr() + "?subject=" + subj;
      });
    });

    // Cookie notice
    var ck = $(".cookie");
    try{ if(ck && !localStorage.getItem("cookie-ok")) ck.classList.add("show"); }catch(e){ if(ck) ck.classList.add("show"); }
    $$(".cookie [data-ck]").forEach(function(b){ b.addEventListener("click", function(){ try{ localStorage.setItem("cookie-ok", b.getAttribute("data-ck")); }catch(e){} ck.classList.remove("show"); }); });

    // YouTube facades (load iframe only on click — faster pages, better Core Web Vitals)
    $$(".video[data-id]").forEach(function(v){
      var id = v.getAttribute("data-id"), title = v.getAttribute("data-title") || "Video";
      v.innerHTML = '<button type="button" aria-label="Play: '+title.replace(/"/g,"")+'"><img loading="lazy" alt="" src="https://i.ytimg.com/vi/'+id+'/hqdefault.jpg"><span class="play"></span></button>';
      v.querySelector("button").addEventListener("click", function(){
        v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0" title="'+title.replace(/"/g,"")+'" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
      });
    });

    // Split-flap hero
    var flaps = $("#flaps");
    function drawFlaps(str, animate){
      if(!flaps) return;
      var s = str.slice(0,12), html = "";
      for(var i=0;i<s.length;i++){ html += (i===2 && s.length===6 && str==="017777") ? '<span class="flap gap" aria-hidden="true"></span>' : ""; html += '<span class="flap'+(animate?" flip":"")+'" style="animation-delay:'+(i*70)+'ms">'+s[i]+'</span>'; }
      flaps.innerHTML = html; flaps.setAttribute("aria-label", s);
    }
    function heroFacts(v){
      if(!window.NUM) return; var a = NUM.analyze(v); if(!a) return;
      var box = $("#hero-facts"); if(!box) return;
      box.innerHTML = '<div><small>Digit sum</small><strong>'+a.sum+'</strong></div><div><small>Prime factors</small><strong>'+a.factors+'</strong></div><div><small>Binary</small><strong>'+a.bin+'</strong></div>';
    }
    if(flaps){
      drawFlaps("017777", true); heroFacts("017777");
      var hf = $("#hero-form");
      if(hf) hf.addEventListener("submit", function(e){
        e.preventDefault(); var v = (window.NUM ? NUM.clean(hf.n.value) : hf.n.value) || "017777";
        drawFlaps(v, true); heroFacts(v);
        var link = $("#hero-more"); if(link) link.href = "/tools.html#n=" + v;
      });
    }

    // Multi-step forms
    $$("form[data-steps]").forEach(function(f){
      var steps = $$(".step", f), bar = $$(".steps-bar span", f), i = 0;
      function show(n){ steps.forEach(function(s,k){ s.classList.toggle("active", k===n); }); bar.forEach(function(b,k){ b.classList.toggle("on", k<=n); }); i=n; var first = steps[n].querySelector("input,select,textarea"); if(first) first.focus({preventScroll:true}); }
      $$("[data-next]", f).forEach(function(b){ b.addEventListener("click", function(){
        var bad = $$("input,select,textarea", steps[i]).filter(function(el){ return !el.checkValidity(); });
        if(bad.length){ bad[0].reportValidity(); return; } show(Math.min(i+1, steps.length-1)); }); });
      $$("[data-prev]", f).forEach(function(b){ b.addEventListener("click", function(){ show(Math.max(i-1,0)); }); });
      show(0);
    });

    // Form relay (FormSubmit AJAX). Address decoded at send time only.
    $$("form[data-relay]").forEach(function(f){
      f.addEventListener("submit", function(e){
        e.preventDefault();
        var hp = f.querySelector(".hp input"); if(hp && hp.value) return;
        var status = f.querySelector(".form-status"), sb = f.querySelector("[type=submit]");
        var data = {}; new FormData(f).forEach(function(v,k){ if(k!=="_hp") data[k] = data[k] ? data[k]+", "+v : v; });
        data._subject = "[017777.com] " + (f.getAttribute("data-relay") || "Form") + " — " + (data.name || data.email || "new submission");
        data._template = "table"; data._captcha = "false"; data.page = location.pathname;
        if(sb){ sb.disabled = true; sb.dataset.label = sb.textContent; sb.textContent = "Sending…"; }
        fetch("https://formsubmit.co/ajax/" + addr(), { method:"POST", headers:{"Content-Type":"application/json","Accept":"application/json"}, body: JSON.stringify(data) })
          .then(function(r){ if(!r.ok) throw new Error("bad"); return r.json(); })
          .then(function(){ location.href = "/thank-you.html?form=" + encodeURIComponent(f.getAttribute("data-relay")||"form"); })
          .catch(function(){
            if(status){ status.className = "form-status err"; status.innerHTML = 'Your message did not send. Check your connection and try again, or <a href="#" data-fallback>email us instead</a>.'; 
              var fb = status.querySelector("[data-fallback]"); if(fb) fb.addEventListener("click", function(ev){ ev.preventDefault();
                var body = Object.keys(data).map(function(k){return k+": "+data[k];}).join("\n");
                location.href = "mai"+"lto:"+addr()+"?subject="+encodeURIComponent(data._subject)+"&body="+encodeURIComponent(body); }); }
            if(sb){ sb.disabled = false; sb.textContent = sb.dataset.label; }
          });
      });
    });

    // Support page: switch pledge buttons to live checkout links when configured
    var pay = S.payments || {};
    $$("[data-pay]").forEach(function(a){
      var url = pay[a.getAttribute("data-pay")];
      if(url){ a.href = url; a.target = "_blank"; a.rel = "noopener"; a.hidden = false; } else { a.hidden = true; }
    });
    var anyPay = Object.keys(pay).some(function(k){ return pay[k]; });
    $$("[data-if-nopay]").forEach(function(el){ el.hidden = anyPay; });

    // Tier buttons prefill pledge amount
    $$("[data-amount]").forEach(function(b){ b.addEventListener("click", function(){
      var sel = $("#pledge-amount"); if(sel){ sel.value = b.getAttribute("data-amount"); }
      var t = $("#pledge"); if(t) t.scrollIntoView({behavior:"smooth"}); }); });

    // Thank-you page message
    var ty = $("#ty-form"); if(ty){ var m = location.search.match(/form=([^&]+)/); if(m) ty.textContent = decodeURIComponent(m[1]); }
  });
})();
