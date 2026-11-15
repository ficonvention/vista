# -*- coding: utf-8 -*-
"""Generate reservation.html / reservation-en.html from the directions page shell.
Run: python3 make_reservation.py
Set ENDPOINT to a Google Apps Script web-app URL to store requests in a Google Sheet;
leave empty to fall back to a pre-filled e-mail."""
import re, json, pathlib

# Google Form "VISTA 예약 신청" (ficonvention account) — responses land in the
# "VISTA 예약" sheet (Form_Responses tab) and trigger an e-mail notification.
ENDPOINT = "https://docs.google.com/forms/d/e/1FAIpQLSdktSOkwg7fOscvPEvKpctkQXlCo-ni3QlqDl5hQl3kdUWX6w/formResponse"
ENTRY = {  # field -> Google Form entry id
    "date": "2031532063", "time": "1987687121", "guests": "714648507", "purpose": "866529829",
    "requests": "353836667", "name": "1757368300", "phone": "1887180724", "email": "1201334208",
    "contact": "1731595164", "memo": "803127697", "lang": "1238120040",
}
ROOT = pathlib.Path(__file__).parent

STYLE = """
<style>
/* Reservation page — sans-serif only */
.page-reservation .page-hero h1,.page-reservation .page-hero .lead,.page-reservation .eyebrow,.page-reservation h2,.page-reservation h3{font-style:normal;font-family:"Noto Sans KR","Open Sans",sans-serif;font-weight:700;letter-spacing:-.01em}
.rsv-wrap{display:grid;grid-template-columns:1.35fr .85fr;gap:2.5rem;align-items:start}
.rsv-form{display:grid;grid-template-columns:1fr 1fr;gap:1.1rem 1.2rem}
.rsv-form .full{grid-column:1/-1}
.rsv-form fieldset{border:0;margin:0;padding:0}
.rsv-form legend,.rsv-form label>span{display:block;font-size:.82rem;font-weight:600;letter-spacing:.04em;color:#eaeaea;margin-bottom:.45rem}
.rsv-form legend em,.rsv-form label>span em{color:var(--gold-deep);font-style:normal}
.rsv-form input[type=text],.rsv-form input[type=tel],.rsv-form input[type=email],.rsv-form input[type=date],.rsv-form select,.rsv-form textarea{width:100%;padding:.8rem .9rem;background:#111;border:1px solid #333;color:#eaeaea;font:inherit;font-size:.95rem;border-radius:4px;box-sizing:border-box}
.rsv-form input:focus,.rsv-form select:focus,.rsv-form textarea:focus{outline:none;border-color:var(--gold)}
.rsv-form input[type=date]{color-scheme:dark}
.chips{display:flex;flex-wrap:wrap;gap:.5rem}
.chip{position:relative}
.chip input{position:absolute;opacity:0;inset:0;margin:0;cursor:pointer}
.chip span{display:inline-block;padding:.55rem .95rem;border:1px solid #444;border-radius:999px;font-size:.88rem;color:#d6d6d6;transition:.15s}
.chip input:checked+span{background:var(--gold);border-color:var(--gold);color:#fff}
.chip input:focus-visible+span{outline:2px solid #fff;outline-offset:2px}
.times{display:grid;grid-template-columns:repeat(auto-fill,minmax(78px,1fr));gap:.45rem}
.times .chip span{display:block;text-align:center;padding:.55rem 0}
.times-label{font-size:.75rem;color:#9a9a9a;margin:.6rem 0 .35rem}
.stepper{display:flex;align-items:center;gap:.6rem}
.stepper button{width:42px;height:42px;border:1px solid #444;background:#111;color:#eaeaea;font-size:1.2rem;border-radius:4px;cursor:pointer}
.stepper input{width:70px!important;text-align:center}
.note{font-size:.8rem;color:#a8a8a8;margin:.4rem 0 0}
.note a{color:var(--gold-deep)}
.consent{display:flex;gap:.6rem;align-items:flex-start;font-size:.82rem;color:#bdbdbd}
.consent input{margin-top:.2rem}
.rsv-submit{background:var(--gold);border:1px solid var(--gold);color:#fff;padding:1rem;font-size:1rem;font-weight:700;letter-spacing:.06em;cursor:pointer;border-radius:4px}
.rsv-submit:hover{background:#c50b2e}
.rsv-side .contact-card{margin-bottom:1rem}
.rsv-side .contact-card p{margin:.3rem 0}
.rsv-done{display:none;border:1px solid var(--gold);padding:1.6rem;border-radius:6px;background:#111}
.rsv-done h3{margin-top:0}
.rsv-err{color:#ff6b81;font-size:.85rem;min-height:1em}
@media (max-width:820px){.rsv-wrap{grid-template-columns:1fr}.rsv-form{grid-template-columns:1fr}}
</style>
"""

T = {
 "ko": dict(
  title="예약하기 | Vista", eyebrow="Reservation", h1="예약하기",
  lead="한강뷰 디너 · 기념일 · 프러포즈 · 해외 손님 VIP 디너",
  date="방문 날짜", time="방문 시간", lunch="런치", dinner="디너", guests="인원",
  guests_note='30명 이상 단체·대관은 <a href="tel:025372440">02-537-2440</a>으로 문의해 주세요.',
  purpose="방문 목적", purposes=["일반 식사","기념일","생일","프러포즈","해외 손님 VIP 디너","비즈니스 미팅","단체 모임"],
  req="요청사항", reqs=["창가석","할랄","채식","알레르기","케이크","꽃 장식","샴페인·와인"],
  name="성함", phone="연락처", contact="선호 연락 방법", contacts=["전화","문자","WhatsApp","이메일"],
  email="이메일", memo="추가 요청 (선택)", memo_ph="알레르기, 이벤트 연출, 도착 시간 등",
  consent="예약 확인을 위한 개인정보(성함·연락처·이메일) 수집·이용에 동의합니다. 예약 처리 후 1년간 보관합니다.",
  submit="예약 신청하기", req_mark="필수",
  side_h="예약 안내",
  side=["신청 후 담당자가 확인하여 <strong>확정 연락</strong>을 드립니다. 확정 전까지는 예약이 완료되지 않습니다.",
        "창가석·이벤트 연출은 가능 여부를 확인 후 안내드립니다.",
        "할랄·채식 메뉴는 방문 3일 전까지 요청해 주세요."],
  side2_h="바로 문의",
  hours="영업시간 3층 11:00–23:00 · 4층 루프탑 16:00–24:00",
  done_h="예약 신청이 접수되었습니다", done_p="확인 후 남겨 주신 연락처로 확정 안내를 드리겠습니다. 감사합니다.",
  mail_h="메일 앱에서 전송을 눌러 주세요", mail_p="작성하신 내용이 담긴 메일이 열렸습니다. 메일 앱이 열리지 않으면 아래 번호로 연락 주세요.",
  err="필수 항목을 확인해 주세요.", subject="[VISTA 예약 신청]",
 ),
 "en": dict(
  title="Reservation | Vista", eyebrow="Reservation", h1="Book a Table",
  lead="Han River-view dinners · anniversaries · proposals · VIP dinners for overseas guests",
  date="Date", time="Time", lunch="Lunch", dinner="Dinner", guests="Guests",
  guests_note='For groups of 30+ or private hire, please contact <a href="tel:+82225372440">+82 2-537-2440</a>.',
  purpose="Occasion", purposes=["Dining","Anniversary","Birthday","Proposal","VIP dinner for overseas guests","Business meeting","Group gathering"],
  req="Requests", reqs=["Window seat","Halal","Vegetarian","Allergy","Cake","Flowers","Champagne / wine"],
  name="Name", phone="Phone (with country code)", contact="Preferred contact", contacts=["Phone","SMS","WhatsApp","E-mail"],
  email="E-mail", memo="Additional requests (optional)", memo_ph="Allergies, surprise set-up, arrival time, etc.",
  consent="I agree to the collection and use of my name, phone number and e-mail to confirm this reservation. Data is kept for one year.",
  submit="Request reservation", req_mark="required",
  side_h="How it works",
  side=["Our team will review your request and <strong>contact you to confirm</strong>. Your booking is not final until confirmed.",
        "Window seats and special set-ups are subject to availability.",
        "Please request halal or vegetarian menus at least 3 days in advance."],
  side2_h="Contact us directly",
  hours="Hours: 3F 11:00–23:00 · 4F Rooftop 16:00–24:00",
  done_h="Your request has been received", done_p="We will contact you shortly to confirm your reservation. Thank you.",
  mail_h="Please press Send in your mail app", mail_p="A pre-filled e-mail has opened. If it did not, please contact us below.",
  err="Please check the required fields.", subject="[VISTA Reservation Request]",
 ),
}

LUNCH = ["11:30","12:00","12:30","13:00","13:30","14:00"]
DINNER = ["17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00"]

def chips(name, items, kind="checkbox", required=False):
    return "".join(
        f'<label class="chip"><input type="{kind}" name="{name}" value="{v}"{" required" if required and i==0 else ""}><span>{v}</span></label>'
        for i, v in enumerate(items))

def body(t):
    r = f' <em>*</em>'
    times = (f'<p class="times-label">{t["lunch"]}</p><div class="times">{chips("time", LUNCH, "radio", True)}</div>'
             f'<p class="times-label">{t["dinner"]}</p><div class="times">{chips("time", DINNER, "radio")}</div>')
    side = "".join(f"<p>{s}</p>" for s in t["side"])
    return f"""
<section class="page-hero" style="background-image:url('images/56292f_280421eebe4f4b12b1744b67f2e10af7.jpg')">
  <div class="wrap"><p class="eyebrow">{t['eyebrow']}</p><h1>{t['h1']}</h1><p class="lead">{t['lead']}</p></div>
</section>
<section class="section"><div class="wrap rsv-wrap">
  <div>
  <form class="rsv-form" id="rsvForm" novalidate data-endpoint="{ENDPOINT}" data-subject="{t['subject']}">
    <label><span>{t['date']}{r}</span><input type="date" name="date" id="rsvDate" required></label>
    <div><span style="display:block;font-size:.82rem;font-weight:600;letter-spacing:.04em;color:#eaeaea;margin-bottom:.45rem">{t['guests']}{r}</span>
      <div class="stepper"><button type="button" data-step="-1" aria-label="-">−</button><input type="text" inputmode="numeric" name="guests" id="rsvGuests" value="2" required><button type="button" data-step="1" aria-label="+">+</button></div>
      <p class="note">{t['guests_note']}</p></div>
    <fieldset class="full"><legend>{t['time']}{r}</legend>{times}</fieldset>
    <fieldset class="full"><legend>{t['purpose']}</legend><div class="chips">{chips("purpose", t['purposes'], "radio")}</div></fieldset>
    <fieldset class="full"><legend>{t['req']}</legend><div class="chips">{chips("requests", t['reqs'])}</div></fieldset>
    <label><span>{t['name']}{r}</span><input type="text" name="name" autocomplete="name" required></label>
    <label><span>{t['phone']}{r}</span><input type="tel" name="phone" autocomplete="tel" required></label>
    <label><span>{t['email']}</span><input type="email" name="email" autocomplete="email"></label>
    <fieldset><legend>{t['contact']}</legend><div class="chips">{chips("contact", t['contacts'], "radio")}</div></fieldset>
    <label class="full"><span>{t['memo']}</span><textarea name="memo" rows="4" placeholder="{t['memo_ph']}"></textarea></label>
    <label class="consent full"><input type="checkbox" name="consent" required><span style="margin:0;font-weight:400;letter-spacing:0;color:#bdbdbd">{t['consent']}{r}</span></label>
    <p class="rsv-err full" id="rsvErr" data-msg="{t['err']}"></p>
    <button type="submit" class="rsv-submit full">{t['submit']}</button>
  </form>
  <div class="rsv-done" id="rsvDone"><h3 data-alt="{t['mail_h']}">{t['done_h']}</h3><p data-alt="{t['mail_p']}">{t['done_p']}</p></div>
  </div>
  <aside class="rsv-side">
    <div class="contact-card"><h3>{t['side_h']}</h3>{side}<p>{t['hours']}</p></div>
    <div class="contact-card"><h3>{t['side2_h']}</h3>
      <p>Tel <a href="tel:025372405">02-537-2405</a></p>
      <p>WhatsApp <a href="https://wa.me/821067153458" target="_blank" rel="noopener">+82 10-6715-3458</a></p>
      <p>E-mail <a href="mailto:ficonvention@gmail.com">ficonvention@gmail.com</a></p>
      <p style="color:#9a9a9a;font-size:.85rem">{t['guests_note']}</p></div>
  </aside>
</div></section>
"""

SCRIPT = r"""
<script>
(function(){
  var f=document.getElementById('rsvForm'); if(!f) return;
  var d=document.getElementById('rsvDate'), g=document.getElementById('rsvGuests');
  var t=new Date(); t.setMinutes(t.getMinutes()-t.getTimezoneOffset()); d.min=t.toISOString().slice(0,10);
  f.querySelectorAll('[data-step]').forEach(function(b){b.addEventListener('click',function(){
    var v=parseInt(g.value||'0',10)+parseInt(b.dataset.step,10); g.value=Math.min(29,Math.max(1,v));});});
  g.addEventListener('input',function(){g.value=g.value.replace(/\D/g,'').slice(0,2);});
  function vals(n){return Array.prototype.map.call(f.querySelectorAll('[name="'+n+'"]:checked'),function(i){return i.value;}).join(', ');}
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var err=document.getElementById('rsvErr'), ok=d.value&&vals('time')&&g.value&&f.name.value.trim()&&f.phone.value.trim()&&f.consent.checked;
    if(!ok){err.textContent=err.dataset.msg;return;} err.textContent='';
    var data={date:d.value,time:vals('time'),guests:g.value,purpose:vals('purpose'),requests:vals('requests'),
      name:f.name.value.trim(),phone:f.phone.value.trim(),email:f.email.value.trim(),contact:vals('contact'),
      memo:f.memo.value.trim(),lang:document.documentElement.lang,submitted:new Date().toISOString()};
    var done=document.getElementById('rsvDone');
    function show(alt){ if(alt){done.querySelectorAll('[data-alt]').forEach(function(el){el.textContent=el.dataset.alt;});}
      f.style.display='none'; done.style.display='block'; done.scrollIntoView({behavior:'smooth',block:'center'}); }
    var ep=f.dataset.endpoint, map={ENTRY_JSON};
    if(ep){
      var body=new URLSearchParams();
      Object.keys(map).forEach(function(k){body.append('entry.'+map[k],data[k]||'');});
      fetch(ep,{method:'POST',mode:'no-cors',body:body})
        .then(function(){show(false);}).catch(function(){mail();});
    } else { mail(); }
    function mail(){
      var lines=Object.keys(data).filter(function(k){return k!=='submitted';}).map(function(k){return k+': '+(data[k]||'-');});
      location.href='mailto:ficonvention@gmail.com?subject='+encodeURIComponent(f.dataset.subject+' '+data.date+' '+data.time+' '+data.name+' ('+data.guests+')')+'&body='+encodeURIComponent(lines.join('\n'));
      show(true);
    }
  });
})();
</script>
"""

def build(lang):
    src = (ROOT / ("directions.html" if lang == "ko" else "directions-en.html")).read_text(encoding="utf-8")
    t = T[lang]
    me, other = ("reservation.html", "reservation-en.html") if lang == "ko" else ("reservation-en.html", "reservation.html")
    head, rest = src.split("</header>", 1)
    _, foot = rest.split('<footer class="site-footer">', 1)
    head = re.sub(r"<title>.*?</title>", f"<title>{t['title']}</title>", head)
    head = re.sub(r'(og:title" content=")[^"]*', r"\g<1>" + t["title"], head)
    head = head.replace('class="page-directions"', 'class="page-reservation"')
    head = head.replace("directions-en.html", "reservation-en.html").replace("directions.html", "reservation.html")
    head = head.replace('<li class="active">', "<li>")
    # restore real nav link to directions page after the blanket replace
    head = head.replace('<a href="reservation.html">찾아오시는 길', '<a href="directions.html">찾아오시는 길')
    head = head.replace('<a href="reservation-en.html">Directions', '<a href="directions-en.html">Directions')
    head = head.replace('<a href="reservation.html">Directions', '<a href="directions-en.html">Directions')
    head = head.replace("</head>", STYLE + "</head>")
    out = head + "</header>\n" + body(t) + '\n<footer class="site-footer">' + foot
    out = out.replace("</body>", SCRIPT.replace("{ENTRY_JSON}", json.dumps(ENTRY)) + "</body>")
    (ROOT / me).write_text(out, encoding="utf-8")
    print("wrote", me)

for l in ("ko", "en"):
    build(l)
