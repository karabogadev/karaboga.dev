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

## "OKUT BENİ!" eş pankartı — A3 (2026-06-11)
- [x] `lamatia/poster/okut-beni.html` — sınav pankartının yanına asılacak, uzaktan bağıran ikinci A3
- [x] Ters palet: fosforlu sarı zemin + dev Fraunces 900 "OKUT BENİ!" (585px) + 1400px menü QR (baskıda ~17cm)
- [x] Sınav kampanyası dili korundu: siyah "FİNAL DÖNEMİ ★ KAHVE MOLASI" bantları, el yazısı kırmızı notlar/oklar, kraft Pilav Ustası yapışkanı, La'Matia damgası, kahve halkaları
- [x] Marka düzeltmesi: her iki pankartta "Coffee & More" → "Chocolate & Coffee" (lamatia.com gerçek alt yazı)
- [x] Render doğrulama (bölge bölge: alt bant/QR boşluğu, sağ not, damga) → `lamatia-okut-beni-a3.png`; sınav pankartı PNG'si de yenilendi

## Gerçek marka: logo + jenerik lamatia.com'dan (2026-06-11)
- [x] lamatia.com analizi: "logo" = Luxurious Script "La'matia" yazı markası + "Chocolate & Coffee"; jenerik = tam ekran düşen kahve çekirdekleri videosu (Wix, 27 sn 720p)
- [x] Jenerik indirildi + ffmpeg ile 960px / CRF33 / 811KB'a küçültüldü → `lamatia/menu/assets/jenerik.mp4` (+ 20KB poster)
- [x] Menü header'ı lamatia.com'daki gibi: jenerik video bandı üzerine Luxurious Script (Google Fonts) "La'matia" + "CHOCOLATE & COFFEE"; QR Menü rozeti köşede
- [x] Footer markası da Luxurious Script; meta açıklamada "Coffee & More" → "Chocolate & Coffee"
- [x] prefers-reduced-motion → video gizli, poster arka planı kalıyor
- [x] QA (Playwright 390×844 + 320×568): video oynuyor (paused=false), font yüklü, yatay taşma 0, sıfır konsol hatası

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

## Sipariş FAB: Betül Abla (2026-06-11)
- [x] Oyun tamamen kaldırıldı (lamatia/oyun/, qr-oyun.png, menü FAB'ı, poster blokları)
- [x] "Sipariş Ver" FAB — Betül'ün yüz avatarıyla, bob animasyonlu
- [x] Basınca Betül abla yaylanarak sahneye çıkıyor: konuşma balonu + "Hemen Ara" (tel:+905345740596) + WhatsApp CTA'sı, uçuşan ☕✨🥐 parçacıkları
- [x] 5 dile çevrildi (tr/en/ar/es/zh) — eski oyun i18n anahtarları sipariş anahtarlarıyla değiştirildi; RTL (Arapça) aynalama eklendi
- [x] QA (Playwright): TR/EN/AR ekran görüntüleri, ESC + backdrop kapatma, WhatsApp önyazısı dile göre, 320px ekran, sıfır JS hatası

## Sepet + WhatsApp Sipariş + Tatlı Animasyon (2026-06-11)
- [x] Varsayılan açık tema (prefers-color-scheme kaldırıldı) + varsayılan dil Türkçe
- [x] i18n: sepet anahtarları (5 dil); Betül overlay metinleri applyUI'da (eşzamanlı süreçle birlikte)
- [x] CSS: tatlı FAB animasyonu (osway salınım + oring nabız halkası + facetilt), fabpop/cbump, uçan 😋, sepet listesi
- [x] Markup: kart ➕ (item-side), FAB rozet (ocnt) + toplam (osum), overlay sepet kutusu (cartBox)
- [x] JS: CART (lm_cart localStorage), addToCart, ± stepper, updateFab, renderCart, waText — sipariş metni HER ZAMAN Türkçe (işletme okuyor)
- [x] Varyantlı ürünler: kartta ➕ → sheet açılır; vrow'lara .vadd, tek fiyatlıya "Siparişe Ekle"
- [x] Doğrulama: node --check + DOM-shim uçtan uca (2× bowl + varyant ekle → 900₺ WA metni, stepper, dil değişimi, temizle) — PASS
