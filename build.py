# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_engine"))
from sitegen import *

EMAIL = "ficonvention@gmail.com"
SITE = dict(
    name="Vista", domain="www.vistapub.co.kr",
    brand_main="VISTA", brand_sub="세빛섬 3F · Cafe & Restaurant",
    desc="비스타 — 반포 한강 세빛섬 플로팅아일랜드 3층 캐주얼 펍 다이닝. 전면 통창 파노라믹 한강 야경, 이탈리안 푸드와 세계 맥주, 기업연회·가족연회·돌잔치·프로포즈. 11:00–23:00, 예약 02-537-2405.",
    og="2649b2_76dd4914a0474381bdbbcf7d4c7fd72f~mv2_d_5923_3949_s_4_2.jpg",
    address="서울 서초구 반포동 650 세빛섬 플로팅아일랜드 3층 비스타",
    tel="(02) 537-2405", tel_raw="025372405", fax="", email=EMAIL,
    footer_extra='<p>Tel 2: <a href="tel:025372440">(02) 537-2440</a> &nbsp;|&nbsp; 3F 11:00–23:00 · 4F Rooftop 16:00–24:00</p>',
    legal="Floating Island Vista",
    social=[("Instagram", "https://instagram.com/floatingisland_marinapark", IG_SVG), ("Facebook", "https://www.facebook.com/floatingi2440", FB_SVG)],
    favicon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#14110f"/><text x="32" y="43" text-anchor="middle" font-family="Georgia,serif" font-size="30" fill="#d4a24c">V</text></svg>',
    nav=[
        ("index.html", "Home", []),
        ("about.html", "About us", [("press.html", "보도자료 · Reviews")]),
        ("menu.html", "메뉴", [("menu.html#food", "Food"), ("menu.html#beverage", "Beverage"), ("course.html", "코스 요리")]),
        ("banquet.html", "연회 · 파티", [("banquet.html#corporate", "기업연회"), ("banquet.html#family", "가족연회 · 돌잔치"), ("banquet.html#wedding", "웨딩"), ("banquet.html#proposal", "프로포즈")]),
        ("directions.html", "찾아오시는 길", []),
    ],
)

THEME = """:root{
  --ink:#1b1714; --ink-soft:#6a625b; --line:#e8e2da; --paper:#fffdfa; --cream:#f6f1ea;
  --gold:#d4a24c; --gold-deep:#a67a2a; --sky:#daeef3;
  --serif:"Cormorant Garamond",Georgia,serif; --sans:"Noto Sans KR","Apple SD Gothic Neo",sans-serif;
  --wrap:1180px; --header-h:76px;
}
.site-footer{background:#14110f}.cta-band{background:#1b1714}
"""

HERO = "2649b2_76dd4914a0474381bdbbcf7d4c7fd72f~mv2_d_5923_3949_s_4_2.jpg"
HERO2 = "2649b2_233487760b8145498d54aafda3d6d50b~mv2_d_2845_1745_s_2.jpg"
J = lambda ids, o="L": [(f"2649b2_{i}", o) for i in ids]

FOOD_IMGS = J(["9e9a48cc39da472dac3fd17202ec03bb~mv2_d_6000_4000_s_4_2.jpg","683d3c2313a94a6799cd89c8d0d0a999~mv2_d_5922_3948_s_4_2.jpg","a8c48c1cd2c94c6f976a3b0002264c76~mv2_d_6000_4000_s_4_2.jpg","76dd4914a0474381bdbbcf7d4c7fd72f~mv2_d_5923_3949_s_4_2.jpg","4c84284962f64cb8baa68d857f191a3a~mv2_d_4240_2832_s_4_2.jpg","b0aba844c8b74bb789a33fface2fceab~mv2.jpg"])
CORP = J(["d000c4d62c704915ab45a732b32928df~mv2_d_3276_2448_s_4_2.jpg","4c84284962f64cb8baa68d857f191a3a~mv2_d_4240_2832_s_4_2.jpg","c31d1b867eb64294833e664d479292a4~mv2.jpg","9c38131c71a74a07aed3062a4746b596~mv2.png"]) + [("2649b2_4be3966e788a43c4b63f29d0d21261f1~mv2.png","P")]
FAMILY = J(["dddc35318db44927b70b3e9bbf361027~mv2_d_4080_2720_s_4_2.jpg","1e9f8cdda90b46aab2ea75285213baca~mv2.jpg","f9cd84aef91548da8ad202e13754b9db~mv2.jpg","43bd7859e71d48a7bb7824057a652408~mv2.jpg","54a3a975e8ce4ad19727de96767e4355~mv2.jpg","3c8bfbd1804f404bbe2cd7d08d5fd19f~mv2_d_4080_2720_s_4_2.jpg","3c9fb2a79bd943cb88acfeb332d7fe36~mv2.jpg"]) + [("2649b2_41ec4fd4291a42aa99f8322441d5cfa4~mv2.png","P")]
WED = J(["008128c8ff8e465cb0ea4beb19708ab8~mv2.png","a17b409f7dd643f1a6e296b9576ddbd6~mv2.png","51438498e0264c92afaf313ff05036ca~mv2.png","158901237763482cad700e8f2788bc03~mv2.jpg","ac4cbd77d2164c08bc91393f7417f404~mv2_d_3739_2482_s_4_2.jpg"]) + [("2649b2_196f010abcbc40c2a2e794bfa4ee97e4~mv2.png","P"),("2649b2_4d4ad3ea74e14ec3ae098e80aa1cb928~mv2.jpg","P")]
PROP = [("2649b2_e940c72f75f24637933044d7ed3d5d49~mv2_d_1242_1848_s_2.jpg","P")] + J(["9e25c8bb46ce4862adc11baa4fab72fb~mv2_d_3255_2449_s_4_2.jpg","683d3c2313a94a6799cd89c8d0d0a999~mv2_d_5922_3948_s_4_2.jpg","d000c4d62c704915ab45a732b32928df~mv2_d_3276_2448_s_4_2.jpg"])
COURSE = [("2649b2_a2e23ea8bcb0414f866db64ef59209df~mv2.png","P"),("2649b2_cf22f9d71cb944be84f34dea4b1a03e7~mv2.jpg","P"),("2649b2_b66f3af4b8c846f295340734e0d1b2be~mv2.jpg","P"),("2649b2_874d667afa3c4aeea8d24e8c6d7e8340~mv2.jpg","P"),("2649b2_0e5502c788224ce5b626c8811255fad9~mv2.jpg","P"),("2649b2_18f01a1bdbe1439fa660ce588cf2ddcd~mv2.jpg","P")]
PRESS = ["56292f_72bc9130c3e14602b782579ca6f8ac1f.jpg","56292f_6615156f4be14c7e860377991563dea5.jpg","56292f_370dbfec312b402e96fa3d27ac9b5543.jpg","56292f_25bd67b988ee428cbf7eb64f9fe5e934.jpg","56292f_4f5a07e50eb0415d97e7a76d3303ee9f.jpg","56292f_626a92ce3176432ca063cdf1899b4927.jpg","56292f_39fe050cfa4d47e790ae0c2684bb2209.jpg","56292f_9b2c1d49ce184bbdb184528817c705eb.jpg","56292f_5da3deab1922472495c9d820bdf3b7a1.jpg"]

ROOMS = [
    ("비스타 홀", "Vista Hall", "~250명", "파노라믹 한강 뷰의 메인 홀. 스크린·음향 시스템 완비. 기업 연회, 런칭 행사, 공식 만찬."),
    ("리브고시", "Rive Gauche", "60–100명", "단독 홀. 소규모 예식, 돌잔치, 세미나."),
    ("오키드 룸", "Orchid Room", "30–60명", "반포대교 달빛무지개분수 쇼가 보이는 룸."),
    ("테라스 룸", "Terrace Room", "15–30명", "비즈니스 디너, 돌잔치, 상견례."),
    ("메디치", "Medici", "10–18명", "앤틱 스타일 룸. 다양한 소규모 연회."),
    ("프러포즈 룸", "Proposal Room", "4–10명", "야외 테라스가 있는 프라이빗 룸."),
    ("세이지 룸", "Sage Room", "4–8명", "야외 테라스가 있는 룸."),
    ("코지 룸", "Cozy Room", "5–8명", "안락한 소파와 테이블이 준비된 룸."),
]
def rooms_html():
    return '<div class="rooms">' + "".join(f'<div class="room"><span class="eyebrow">{en} · {cap}</span><h3>{kr}</h3><p>{d}</p></div>' for kr, en, cap, d in ROOMS) + '</div>'

home = f"""
<section class="hero" style="background-image:url('{wix(HERO, 1920, 1280)}')">
  <div class="hero-inner">
    <p class="eyebrow">Floating Island · Han River · Banpo</p>
    <h1>Vista</h1>
    <p class="lead">3F Cafe &amp; Restaurant · 4F Rooftop — 전면 통창으로 만나는 한강 파노라믹 야경</p>
    <div class="hero-cta">
      <a class="btn btn-light" href="tel:025372405">예약 02-537-2405</a>
      <a class="btn btn-outline" href="menu.html">Menu</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="split-img"><img src="{wix(HERO2, 1100, 733)}" loading="lazy" alt="Vista"></div>
    <div class="split-text">
      <p class="eyebrow">캐주얼 펍 다이닝 · Italian Food</p>
      <h2>세계가 인정한 그 맛,<br>한강 위의 비스타</h2>
      <p>반포지구 세빛섬 플로팅아일랜드 3층에 위치한 비스타는 전면이 통창으로 되어 있어 한강 야경과 서울 스카이라인이 한눈에 들어오는 캐주얼 펍 레스토랑입니다. 신선한 식재료의 이탈리안 스타일 메뉴와 세계 맥주, 간단한 차와 커피부터 코스 디너와 공식 만찬까지 — 총 250석의 여유로운 공간에서 즐기실 수 있습니다.</p>
      <a class="btn" href="about.html">About Vista</a>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <p class="eyebrow center">Business · Party</p>
    <h2 class="center">기업연회 · 파티대관 · 루프탑 파티 · 돌잔치 · 가족연회</h2>
    <div class="service-grid">
      <a class="service" href="banquet.html#corporate"><img src="{wix('2649b2_4c84284962f64cb8baa68d857f191a3a~mv2_d_4240_2832_s_4_2.jpg', 900, 640)}" loading="lazy" alt=""><h3>기업연회</h3><p>250석 홀 · 스크린 · 음향</p></a>
      <a class="service" href="banquet.html#family"><img src="{wix('2649b2_dddc35318db44927b70b3e9bbf361027~mv2_d_4080_2720_s_4_2.jpg', 900, 640)}" loading="lazy" alt=""><h3>가족연회 · 돌잔치</h3><p>소규모 룸 4~5개 · 독립 연회장</p></a>
      <a class="service" href="banquet.html#wedding"><img src="{wix('2649b2_ac4cbd77d2164c08bc91393f7417f404~mv2_d_3739_2482_s_4_2.jpg', 900, 640)}" loading="lazy" alt=""><h3>웨딩</h3><p>소규모 예식 · 리셉션</p></a>
      <a class="service" href="banquet.html#proposal"><img src="{wix('2649b2_e940c72f75f24637933044d7ed3d5d49~mv2_d_1242_1848_s_2.jpg', 900, 640)}" loading="lazy" alt=""><h3>프로포즈</h3><p>야외 테라스 프라이빗 룸</p></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow center">Gallery</p>
    {gallery(FOOD_IMGS, "gallery cols-3")}
  </div>
</section>

<section class="section alt">
  <div class="wrap hours-grid">
    <div><p class="eyebrow">영업시간</p><h3>3F 비스타</h3><p>11:00 – 23:00</p><h3>4F 루프탑</h3><p>16:00 – 24:00</p></div>
    <div><p class="eyebrow">예약 문의</p><h3><a href="tel:025372405">(02) 537-2405</a></h3><p><a href="tel:025372440">(02) 537-2440</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p><p>전 좌석 예약제로 운영됩니다.</p></div>
    <div><p class="eyebrow">위치</p><h3>세빛섬 3층</h3><p>서울 서초구 반포동 650 세빛섬 플로팅아일랜드 3F</p><a class="btn" href="directions.html">찾아오시는 길</a></div>
  </div>
</section>
"""

about = f"""
{page_hero(HERO2, 'Vista', 'About us', '세계가 인정한 그 맛! VISTA를 소개합니다')}
<section class="section"><div class="wrap split">
  <div class="split-img"><img src="{wix('56292f_5bbb63cfc67f434ea072b6e6107ecc02.jpg', 950, 760)}" loading="lazy" alt=""></div>
  <div class="split-text prose">
    <p class="eyebrow">반포지구 세빛섬 플로팅아일랜드 3층</p>
    <p>전면이 통창으로 되어 있는 비스타는 파노라믹 뷰를 가진 아름다운 야경이 돋보이는 캐주얼 펍 레스토랑입니다.</p>
    <p>신선한 식재료를 사용한 이탈리안 스타일 캐주얼 펍 다이닝의 다양한 메뉴와 세계 맥주를 만나볼 수 있는 비스타는 총 250석 규모의 여유 있는 공간을 갖추고 있으며, 간단한 차나 커피만 즐기실 수도 있고 런칭 행사, 파티, 또는 코스 요리로 격조 있는 디너나 공식 만찬도 즐기실 수 있습니다.</p>
    <p>서울을 대표하는 유니크 베뉴로서 해외 언론의 집중 스포트라이트를 받고 있는 비스타는 외국 손님 접대나 특별한 모임, 돌잔치·회갑연 등의 가족연회, 비즈니스 파티가 가능한 4~5개의 소규모 룸과 100명 규모의 독립된 연회장도 갖추고 있으며 전 좌석이 예약제로 운영되고 있습니다.</p>
  </div>
</div></section>
<section class="section alt"><div class="wrap"><img src="{wix('56292f_5da3deab1922472495c9d820bdf3b7a1.jpg', 1400, 790)}" loading="lazy" alt="" style="width:100%"></div></section>
{cta("Reservation", "예약문의 (02) 537-2405 · 11:00 – 23:00", "전화 예약", "tel:025372405", ("보도자료 · Reviews", "press.html"))}
"""

press = f"""
{page_hero(HERO, 'Vista', 'Reviews', '보도자료')}
<section class="section"><div class="wrap">
  <div class="quotes">
    <blockquote>푸드 스타일리스트들의 감각이 돋보이는 비스타의 카나페는 맛의 향연과 함께 즐거움을 함께 얻을 수 있는, 그런 요리라고나 할까요?</blockquote>
    <blockquote>다양한 식자재의 변화로 질리지 않는 타파스의 매력과 셰프들의 정성이 느껴지는 비스타!</blockquote>
    <blockquote>국내 캐주얼 펍 다이닝 업계의 지각변동이 예고된다…</blockquote>
    <blockquote>다시 찾고 싶게 만드는 한강의 아름다운 파노라믹 뷰. 외국인의 입맛도 사로잡다!</blockquote>
  </div>
  <div class="press-grid">{"".join(f'<a href="{wix(p, 1600, 900)}" data-lightbox><img src="{wix(p, 900, 500)}" loading="lazy" alt=""></a>' for p in PRESS)}</div>
  <ul class="plain">
    <li>다양한 세계 생맥주와 함께 바삭바삭한 포테이토 칩과 피자로 비스타에서 회식을</li>
    <li>한가로운 오후 따사로운 햇살 아래서 여유 있게 즐기는 비스타의 브런치</li>
    <li>외국 손님 접대에 손색이 없는 세련된 플레이팅과 할랄, 베지테리언 등 특이식단 메뉴</li>
    <li>신선한 식자재를 사용하여 상큼한 맛이 돋보이는 비스타의 샐러드</li>
  </ul>
</div></section>
{cta("Reservation", "", "예약문의 (02) 537-2405", "tel:025372405")}
"""

menu = f"""
{page_hero(HERO2, 'Vista · Italian Food', '메뉴', '캐주얼 펍 다이닝 · Party & Dinner')}
<section class="section" id="food"><div class="wrap">
  <p class="eyebrow center">Food</p><h2 class="center">Vista Menu</h2>
  <div class="menu-imgs">
    <a href="{wix('2649b2_455b070eeb234eac9b6480e11b3d5023~mv2.jpg', 1400, 1980)}" data-lightbox><img src="{wix('2649b2_455b070eeb234eac9b6480e11b3d5023~mv2.jpg', 900, 1273)}" loading="lazy" alt="Vista Menu 1"></a>
    <a href="{wix('2649b2_2e8b3064564d48f9ae51216f2ba4ddfd~mv2.jpg', 1400, 1980)}" data-lightbox><img src="{wix('2649b2_2e8b3064564d48f9ae51216f2ba4ddfd~mv2.jpg', 900, 1273)}" loading="lazy" alt="Vista Menu 2"></a>
  </div>
  <p class="center note">메뉴와 가격은 사정에 따라 변경될 수 있습니다. 할랄·베지테리언 등 특이식단은 예약 시 말씀해 주세요.</p>
</div></section>
<section class="section alt" id="beverage"><div class="wrap">
  <p class="eyebrow center">Beverage</p><h2 class="center">세계 맥주 · 와인 · 커피</h2>
  <a href="{wix('2649b2_b0aba844c8b74bb789a33fface2fceab~mv2.jpg', 1800, 1264)}" data-lightbox><img src="{wix('2649b2_b0aba844c8b74bb789a33fface2fceab~mv2.jpg', 1400, 983)}" loading="lazy" alt="Beverage" style="width:100%"></a>
</div></section>
<section class="section"><div class="wrap">{gallery(FOOD_IMGS[:3], "gallery cols-3")}<p class="center"><a class="btn" href="course.html">코스 요리 보기</a></p></div></section>
{cta("Reservation", "", "예약문의 (02) 537-2405", "tel:025372405")}
"""

course = f"""
{page_hero('2649b2_0e5502c788224ce5b626c8811255fad9~mv2.jpg', 'Vista', '코스 요리', 'Western Set Menu')}
<section class="section"><div class="wrap">
  <p class="center sub">격조 있는 디너와 공식 만찬을 위한 웨스턴 세트 메뉴. 인원과 예산에 맞춰 구성해 드립니다.</p>
  {gallery(COURSE, "gallery cols-3")}
</div></section>
{cta("Course dinner inquiry", "단체·만찬 예약은 전화로 문의해 주세요.", "예약문의 (02) 537-2405", "tel:025372405", ("E-mail", f"mailto:{EMAIL}"))}
"""

banquet = f"""
{page_hero(HERO2, 'Vista', '연회 · 파티', '기업연회 · 파티대관 · 가족연회 · 웨딩 · 프로포즈')}
<section class="section"><div class="wrap">
  <p class="eyebrow center">Rooms</p><h2 class="center">공간 안내</h2>
  {rooms_html()}
  <p class="center note">전 좌석 예약제 · 예약문의 <a href="tel:025372405">(02) 537-2405</a></p>
</div></section>
<section class="section alt" id="corporate"><div class="wrap"><p class="eyebrow center">Corporate</p><h2 class="center">기업연회 · 파티대관</h2><p class="center sub">250명 규모 파노라믹 뷰 홀에 스크린과 음향 시스템을 갖추고 있어 런칭 행사, 송년회, 세미나, 공식 만찬에 적합합니다.</p>{gallery(CORP, "gallery cols-3")}</div></section>
<section class="section" id="family"><div class="wrap"><p class="eyebrow center">Family</p><h2 class="center">가족연회 · 돌잔치</h2><p class="center sub">돌잔치, 회갑연, 상견례 — 소규모 룸부터 독립 연회장까지 가족 모임의 규모에 맞게 준비합니다.</p>{gallery(FAMILY, "gallery cols-3")}</div></section>
<section class="section alt" id="wedding"><div class="wrap"><p class="eyebrow center">Wedding</p><h2 class="center">웨딩</h2><p class="center sub">한강이 보이는 리브고시 홀에서 진행되는 소규모 예식과 리셉션. 대규모 웨딩은 2층 컨벤션홀과 연계됩니다.</p>{gallery(WED, "gallery cols-3")}</div></section>
<section class="section" id="proposal"><div class="wrap"><p class="eyebrow center">Proposal</p><h2 class="center">프로포즈</h2><p class="center sub">야외 테라스가 있는 프라이빗 프러포즈 룸. 플라워·케이크·음악 연출을 함께 준비해 드립니다.</p>{gallery(PROP, "gallery cols-3")}</div></section>
{cta("Reservation", "예약문의 (02) 537-2405", "전화 예약", "tel:025372405", ("E-mail", f"mailto:{EMAIL}"))}
"""

directions = f"""
{page_hero('56292f_280421eebe4f4b12b1744b67f2e10af7.jpg', 'Vista', '찾아오시는 길', 'Map · 영업시간 · 예약')}
<section class="section"><div class="wrap split contact-split">
  <div class="split-text">
    <h2>세빛섬 플로팅아일랜드 3층</h2>
    <p>서울특별시 서초구 반포동 650번지 세빛섬 (가빛섬) 3F 비스타</p>
    <div class="contact-card">
      <h3>영업시간</h3>
      <p>3층 비스타: 11:00 – 23:00<br>4층 루프탑: 16:00 – 24:00</p>
      <h3>예약 · 문의</h3>
      <p>Tel: <a href="tel:025372405">(02) 537-2405</a> · <a href="tel:025372440">(02) 537-2440</a><br>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>특별 예약 및 단체 주문은 위 번호를 이용해 주세요.</p>
    </div>
    <div class="contact-card">
      <h3>오시는 길</h3>
      <p><strong>지하철</strong> 3·7·9호선 고속버스터미널역 G2 출구 → 세빛섬 주차장으로 연결</p>
      <p><strong>버스</strong> 잠수교 405, 740 · 반포대교 남단 143, 401, 406, 8340</p>
      <p><strong>자가용</strong><br>잠실 방면: 반포대교 통과 → 150m 지점 주차장 진입<br>공항 방면: 국립현충원 방향 → 반포IC → 이수고가차도 → 잠수교 입구 원형교차로 9시 방향<br>강북 방향: 잠수교 이용 → 주차장 진입, 또는 한남대교 → 반포대교 통과 후 150m 지점 주차장<br>강남 방향: 성모병원 앞 교차로 고가도로 → 잠수교 입구 원형교차로 9시 방향</p>
      <p>* 반포대교가 아닌 잠수교를 이용하셔야 진입이 가능합니다.</p>
    </div>
  </div>
  {contact_form(EMAIL, ["테이블 예약", "기업연회 / 파티대관", "가족연회 / 돌잔치", "웨딩", "프로포즈", "코스 요리 / 단체 주문", "기타"])}
</div></section>
<section class="map-section"><iframe title="Vista 위치" src="https://www.google.com/maps?q=%EC%84%B8%EB%B9%9B%EC%84%AC&output=embed" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe></section>
"""

PAGES = {
    "index.html": ("Home", home, True),
    "about.html": ("About us", about, False),
    "press.html": ("보도자료", press, False),
    "menu.html": ("메뉴", menu, False),
    "course.html": ("코스 요리", course, False),
    "banquet.html": ("연회 · 파티", banquet, False),
    "directions.html": ("찾아오시는 길", directions, False),
}

EXTRA_CSS = """
.hours-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2.5rem}
.hours-grid h3{margin:.3em 0 .1em}.hours-grid p{color:var(--ink-soft)}
.rooms{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2rem;margin-top:2rem}
.room{background:var(--cream);padding:1.4rem 1.4rem 1.2rem;border-top:2px solid var(--gold)}
.room .eyebrow{margin-bottom:.3em;font-size:.68rem}.room h3{margin-bottom:.3em;font-size:1.35rem}.room p{font-size:.88rem;color:var(--ink-soft);margin:0}
.menu-imgs{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;max-width:960px;margin:2rem auto}
.menu-imgs img{width:100%;box-shadow:0 10px 30px rgba(0,0,0,.08)}
.quotes{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:3rem}
.quotes blockquote{margin:0;padding:1.5rem 1.8rem;background:var(--cream);border-left:3px solid var(--gold);font-family:var(--serif);font-size:1.25rem;line-height:1.5}
.press-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
.press-grid img{width:100%;aspect-ratio:16/9;object-fit:cover}
.plain{list-style:none;padding:0;margin:2.5rem auto 0;max-width:760px;color:var(--ink-soft)}
.plain li{padding:.5rem 0;border-bottom:1px dotted var(--line)}
.contact-card+.contact-card{margin-top:1rem}.contact-card h3+p{margin-top:.2em}.contact-card h3{margin-top:1rem}.contact-card h3:first-child{margin-top:0}
@media (max-width:820px){.hours-grid{grid-template-columns:1fr}.rooms{grid-template-columns:1fr 1fr}.menu-imgs,.quotes{grid-template-columns:1fr}.press-grid{grid-template-columns:1fr 1fr}}
"""

if __name__ == "__main__":
    build(SITE, PAGES, os.path.dirname(os.path.abspath(__file__)), THEME + EXTRA_CSS)
