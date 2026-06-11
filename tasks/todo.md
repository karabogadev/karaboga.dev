# Lamatia QR Menü + Oyun (lamatia.karaboga.dev/menu)

## Menü mobil uyumluluk turu (2026-06-11)
- [x] iOS odak zoom'u: arama input font-size 15px → 16px
- [x] Bottom sheet: max-height (100dvh−28px) + `.sheet-scroll` iç scroll; sürükle-kapat yalnız scrollTop=0 iken
- [x] iOS'ta sheet açıkken arka plan kayması: body.lock → position:fixed + top:-scrollY + kapatınca scroll restore
- [x] Dar ekran (≤380px) ince ayar: kart görseli 68px, hero tipografi, play-cta flex-wrap, clear butonu 34px, text-size-adjust (menü+oyun)
- [x] QA: Playwright 390×844 + 320×568 — 18/18 PASS (yatay taşma yok, arama, sheet aç/iç scroll/kapat, kilit, scroll restore), sıfır JS hatası

## Oyun mobil uyumluluk (2026-06-11)
- [x] Göreceli sürükleme kontrolü (DRAG_SENS 1.4): kase parmağa ışınlanmıyor, parmak kaseyi kapatmıyor; masaüstü için ok tuşları
- [x] `roundRect` polyfill — eski Safari (<16)/Android WebView'de HUD her karede patlıyordu
- [x] Panel taşması: `.veil` overflow-y:auto + `.panel` margin:auto; kısa ekran (≤620px) kompakt tipografi
- [x] Yatay mod: "Telefonu dik tut" katmanı (CSS media query) + oyun otomatik duraklıyor, dikeye dönünce devam
- [x] visualViewport/orientationchange resize + SAFE_TOP'un resize'da yenilenmesi (iOS adres çubuğu)
- [x] Düşüş hızı ekran boyuna ölçekli (H/720, 0.85–1.25) — kısa ekranda haksız zorlaşma yok
- [x] QA (Playwright): tap teleport yok, +100px drag → +137px hedef, polyfill'li 3s oyun hatasız, 320×568 panel sığıyor, landscape pause→resume doğrulandı, sıfır JS hatası

## Sınav dönemi pankartı (2026-06-11)
- [x] Konsept: "KHV 101 — Kahve Bilimine Giriş" final sınavı kağıdı parodisi (İstanbul Yüzyıl Üniv. öğrencilerine)
- [x] `lamatia/poster/sinav-pankart.html` — A3 300dpi (2480×3508), Courier Prime + Caveat + Fraunces
- [x] Menü QR = "Cevap Anahtarı", oyun QR = kraft mola kartı; AA damgası, kırmızı kalem, post-it, kahve lekeleri
- [x] Render doğrulama (headless Chromium, bölge bölge kontrol) → `lamatia-sinav-pankart-a3.png`

## Sınav pankartı v2 — La'Matia Üniversitesi + uzaktan okunabilirlik (2026-06-11)
- [x] Üniversite adı → "LA'MATIA ÜNİVERSİTESİ" (94px, nowrap; fakülte satırı kısaltıldı, barkodla çakışma giderildi)
- [x] Dev manşet: sarı fosforlu "FİNAL SINAVI" (212px) — sokaktan ilk okunan öğe
- [x] AA damgası 430→540px, kağıt kenarından taşan kolaj görünümü
- [x] Soru/cevap/keypanel sıkılaştırıldı (stem 53, opts 47, keypanel padding 46, QR 560)
- [x] Headless Chromium render, başlık/orta/alt bölge kontrolleri → `lamatia-sinav-pankart-a3.png` güncellendi

## Redesign v2 — "çok çok daha iyi" (2026-06-11)
- [ ] Tek sayfa akış: tüm kategoriler alt alta + scrollspy'lı yapışkan chip nav (sekme yerine)
- [ ] Ürün detay alt-sayfası (bottom sheet): büyük görsel (wix w_800), açıklama, varyantlar
- [ ] Görsel cila: başlık bandı, hero buhar animasyonu, kademeli kart reveal, arama vurgusu
- [ ] "Breakfast" (tek ürün) kategorisini render'da "Kahvaltı & Sandviç" ile birleştir
- [ ] Footer: "Fiyatlar www.lamatia.com..." satırını sil (kullanıcı isteği)
- [ ] Performans: content-visibility, lazy img; erişilebilirlik: aria, reduced-motion
- [ ] QA: Playwright 390×844 — scrollspy, arama, sheet aç/kapa, sıfır konsol hatası

## Plan
- [x] lamatia.com/menu crawl (16 kategori, 172 ürün, fiyat + görsel URL'leri → JSON)
- [x] `lamatia/menu/index.html` — mobil öncelikli QR menü sayfası
  - Kategori sekmeleri (yatay scroll), arama, ürün kartları (görsel, ad, açıklama, fiyat, boy varyantları)
  - "Pilavüstü Lezzetler" hero bölümü (görselden: Sade 100₺, Nohutlu 130₺, Tavuklu 150₺, Köri Soslu 225₺, Acı Soslu 225₺)
  - Oyuna geçiş CTA + yüzen buton
- [x] `lamatia/oyun/index.html` — "Pilav Ustası" mobil web oyunu (canvas, dokunmatik)
  - Düşen malzemeleri (pilav, nohut, tavuk, köri sos, acı sos) kaseyle yakala; bomba = -1 can, maydanoz = bonus
  - Sipariş = menüdeki 5 gerçek ürün; tamamla → fiyat × kombo kadar ₺ kazan
  - Rütbeler (Çaylak Komi → Efsane Şef), 1600₺+ rozet, rekor localStorage, paylaş butonu
- [x] nginx.conf: `lamatia.karaboga.dev` server bloğu; Dockerfile'a lamatia/ kopyala
- [x] Lokal doğrulama (http.server + Playwright/Chromium, 390×844)

## Review
- Crawl: Wix SSR HTML'den `data-hook` öznitelikleriyle parse edildi; 172 ürün, 16 kategori, 27 boy varyantı, görsel URL'leri (wixstatic, w_300 transform).
- Oyun QA (headless otomatik oyuncu): 3 sipariş/500₺/kombo ×3 sorunsuz; ölüm → oyun sonu ekranı, rütbe, rozet, rekor kaydı, tekrar oyna akışı doğrulandı; sıfır JS hatası.
- Denge: bomba oranı seviyeyle artıyor; gerekli malzemeyi kaçırmak komboyu bozuyor.
- Deploy: lamatia.karaboga.dev → nginx server bloğu (root: /usr/share/nginx/html/lamatia, / → /menu/). Coolify'da domain'in app'e ekli olması ve DNS kaydı gerekiyor.
