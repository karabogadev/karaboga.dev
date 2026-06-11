# Lamatia QR Menü + Oyun (lamatia.karaboga.dev/menu)

## Plan
- [x] lamatia.com/menu crawl (16 kategori, 172 ürün, fiyat + görsel URL'leri → JSON)
- [ ] `lamatia/menu/index.html` — mobil öncelikli QR menü sayfası
  - Kategori sekmeleri (yatay scroll), arama, ürün kartları (görsel, ad, açıklama, fiyat)
  - "Pilavüstü Lezzetler" bölümü (görselden: Sade 100₺, Nohutlu 130₺, Tavuklu 150₺, Köri Soslu 225₺, Acı Soslu 225₺)
  - Oyuna geçiş CTA'sı
- [ ] `lamatia/oyun/index.html` — "Pilav Ustası" mobil web oyunu (canvas, dokunmatik)
  - Düşen malzemeleri (pilav, nohut, tavuk, köri sos, acı sos) kaseyle yakala
  - Sipariş = menüdeki gerçek ürünler; doğru tarif → puan/combo
  - Skor eşiklerinde rozet/kupon ekranı → kullanıcıyı tutma
- [ ] nginx.conf: `lamatia.karaboga.dev` server bloğu; Dockerfile'a lamatia/ kopyala
- [ ] Lokal doğrulama (docker/nginx veya python http.server + mobil viewport test)

## Review
(doldurulacak)
