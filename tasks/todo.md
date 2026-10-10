# karaboga.dev — AI SEO motoru

**Kaynak:** Julian Goldie'nin "everywhere engine" özeti — 5 hamle.
**Hedef:** ChatGPT / AI Overviews "Flutter geliştirici" konularında Cihat'ın adını anar hâle gelsin.
**Kısıt:** Tek repo, build adımı yok, statik nginx. Uydurma deneyim yok.
**Kararlar (Cihat):** Yazılar İngilizce · ilk taslakları Claude yazar, Cihat onaylar · GSC CSV export'u Cihat verecek.

## Hamle → karaboga.dev karşılığı

| # | Makaledeki hamle | Burada | Durum |
|---|---|---|---|
| 1 | Flywheel: 1 keyword + 1 gerçek örnek → yayın → ping | `/notes/` + `scripts/indexnow.sh` | yapıldı |
| 1 | Birden çok site ağı | **Yapılmadı** — scaled content abuse / link scheme riski; marka tek alan adında | red |
| 2 | Search Console gap/leak avı | `scripts/gsc.py` | yapıldı, gerçek veri bekliyor |
| 3 | Yazım kuralları AI'dan önce | `WRITING.md` | yapıldı |
| 4 | Başkalarının seni anması | `WRITING.md` → "Beyond the site" — paylaşımı Cihat yapar | checklist |
| 5 | Kalan tıklamanın kalitesi | Her not tek net "next step" ile biter | yapıldı |

## Yapılacaklar

### Altyapı
- [x] `sitemap.xml` — ana sayfa `lastmod` güncel, notlar eklendi
- [x] IndexNow anahtar dosyası + `scripts/indexnow.sh`
- [x] Dockerfile — `notes/` ve anahtar kopyalanıyor
- [x] nginx `absolute_redirect off` (yol boyunca bulunan hata, aşağıda)

### /notes/
- [x] `notes/index.html` + ortak `notes/notes.css`
- [x] `BlogPosting` JSON-LD, `author` → `#person`; `Blog` JSON-LD index'te
- [x] Ana sayfada Notes bölümü (TR etiketli, notlar `lang="en"`) + sitemap
- [x] Not 1: `flutter-offline-sync-queue-hive-ce` (boilerplate @ `47bfb7b`)
- [x] Not 2: `headless-chrome-500px-minimum-width` (bu makinede yeniden ölçüldü)
- [ ] **Cihat iki notu satır satır okur** → sonra deploy

### Kurallar & veri
- [x] `WRITING.md` — 11 kural + brief şablonu + yayın checklist'i
- [x] `scripts/gsc.py` — EN/TR export, zip veya CSV
- [ ] Gerçek GSC export'u ile ilk çalıştırma

### Deploy sonrası (Cihat)
- [ ] Push → deploy, sonra `scripts/indexnow.sh`
- [ ] Search Console'da sitemap'i yeniden gönder
- [ ] Boilerplate README'sinden not 1'e link; dev.to'ya canonical'lı cross-post

## Review

**Doğrulama (hepsi çalıştırıldı):**
- Docker imajı (nginx) üzerinde: `/`, `/notes/`, iki not, `/privacy`, anahtar
  dosyası 200; `/notes/nope`, `/WRITING.md`, `/scripts/gsc.py` 404 (sızmıyor).
- Playwright + Chrome for Testing 151: 4 sayfa × 320/360/768/1440 × açık/koyu —
  hepsinde `scrollWidth == clientWidth`, konsol hatası yok; TR'de bölüm başlığı
  "Notlar".
- html-validate (repo stil kuralları hariç) 6 sayfada temiz; JSON-LD'ler geçerli;
  notlardaki tüm iç linkler ve commit'e sabitlenmiş GitHub linkleri 200.
- `gsc.py` sentetik EN zip, TR zip (virgüllü ondalık), düz CSV ve yanlış dosya
  ile denendi.

**Yol boyunca çıkan gerçek düzeltmeler:**
1. nginx `/notes` → `/notes/` yönlendirmesini `http://host:3000/notes/` olarak
   veriyordu; proxy arkasında kırık link olurdu. `absolute_redirect off`.
2. Boilerplate'te `queueOperation` hiç çağrılmıyor — not 1 "offline-first
   uygulamam" değil, "altyapı ve eksikleri" olarak yazıldı.
3. `lessons.md`'deki headless Chrome iddialarından biri (`--dump-dom` ve
   transition) yeniden ölçünce yanlış, biri (500px tabanı) eksik çıktı;
   ders düzeltildi, not 2 ölçülen hâliyle yazıldı.

**Cihat'ın bilmesi gerekenler:**
- Not 1 boilerplate'teki gerçek eksikleri herkese açık yazıyor (8s yorumu,
  idempotency yok, testler ince). İstersen önce repoda düzelt, not "ne
  düzelttim" diye güncellenir — bu da flywheel'in bir sonraki turu.
- Notların tarihi 10 Ekim 2026; deploy günü farklıysa tarihleri güncelle.

---

# karaboga.dev — Tasarım elden geçirme

**Yön:** Rafine minimal (mevcut ember + Geist çizgisinin ustalaşmış hâli)
**Kapsam:** Görsel yenileme + yeni bölümler · İki dilli (TR/EN) · Tek dosya, build yok

---

## Kararlar

- Tek dosya + inline CSS + build adımı yok kuralı korunur (README'nin kimliği).
- Server-rendered markup **İngilizce** kalır → mevcut SEO/JSON-LD/OG bozulmaz.
  TR, `data-i18n` sözlüğüyle istemci tarafında uygulanır. Paylaşılabilir link
  için `?lang=tr`. Ayrı URL olmadığı için hreflang eklenmez (anlamsız olurdu).
- Yıldız sayıları yazılmaz (bayatlar). Yıl + dil + teknoloji etiketi yeter.
- Marka işareti olarak `favicon.svg` içindeki mevcut amblem esas alınır;
  404'teki ayrık lama silüeti onunla değiştirilir.

## Yapılacaklar

### Temel sistem (index.html)
- [x] Tasarım token'ları: renk (+ `--surface`, `--ink-3`), tipografik ölçek,
      boşluk ölçeği, radius, hairline — hepsi tek yerde
- [x] Geist Mono eklenir (yıl, bölüm numarası, etiket, meta için); tabular-nums
- [x] Açık/koyu tema kontrast denetimi (WCAG AA, özellikle ember-on-light)
- [x] Rail düzeni: solda `01 / Work` etiketi, sağda içerik; mobilde tek kolon

### Bölümler
- [x] Header: marka · anchor nav · dil butonu (TR/EN) · tema butonu
- [x] Hero: eyebrow (rol · Istanbul), isim, bio, müsaitlik rozeti, 2 CTA
- [x] 01 Seçili işler — flutter_app_boilerplate, traffic_racer, karaboga.dev
      + "tümü GitHub'da" linki
- [x] 02 Deneyim — **içerik Cihat'tan gelecek**, şimdilik işaretli yer tutucu
- [x] 03 Stack — Mobile / Architecture / Data / Tooling grupları
- [x] 04 Hakkımda — 2 paragraf taslak
- [x] Footer: e-posta, sosyal, ©

### i18n
- [x] `data-i18n` / `data-i18n-label` altyapısı + TR/EN sözlük
- [x] Dil tespiti: localStorage → `?lang` → navigator.language → en
- [x] Dil değişince `<html lang>`, `<title>`, meta description güncellenir

### Hareket & erişilebilirlik
- [x] IntersectionObserver ile kademeli scroll-reveal
- [x] `prefers-reduced-motion` altında tüm hareket kapalı
- [x] Klavye odağı, skip link, aria etiketleri, kontrast

### Diğer dosyalar
- [x] `404.html` — yeni token'lar, açık/koyu tema desteği, marka işareti hizası
- [x] `og.html` — yeni tipografi/palet · `og.png` headless Chrome ile yeniden render
- [x] `manifest.webmanifest` + `theme-color` — palet güncellenirse
- [x] `README.md` — i18n notu, font listesi, dosya tablosu

### Doğrulama
- [x] Headless Chrome ile 4 ekran görüntüsü: masaüstü/mobil × açık/koyu
- [x] TR ve EN ayrı ayrı render kontrolü
- [x] HTML doğrulama + JSON-LD sağlamlığı

## Tamamlananlar
- [x] Boş `lamatia/` klasörü silindi (dangling referans yok — nginx/Dockerfile zaten temizdi)

## Review

**Doğrulama (hepsi çalıştırıldı):**
- Kontrast: her ink/accent token'ı kendi arka planına karşı WCAG AA'yı geçiyor.
  Eski açık tema accent'i (`#e0481f`) normal metin için 3.96:1 ile kalıyordu —
  metin için `--accent-ink` (`#c23d18`, 5.10:1) ayrıldı, `--accent` dekorasyonda kaldı.
- 360px'te `scrollWidth == clientWidth` → yatay taşma yok.
- Konsol hatası yok; TR/EN geçişi `lang` ve `<title>`'ı doğru güncelliyor.
- 38 `data-i18n` anahtarının tamamının TR karşılığı var, fazlalık yok.
- JSON-LD ve manifest geçerli JSON; 4 dış link 200 dönüyor.
- Piksel doğrulaması: masaüstü açık/koyu, 360px mobil TR, 404 açık/koyu, og.png.

**Yol boyunca çıkan iki gerçek düzeltme:**
1. Accent fazla yerdeydi (rail numaraları + 4 şirket adı + CTA + marka noktası).
   `.xp-org` `--ink-2`'ye indi; vurgu artık seyrek.
2. Reveal `rootMargin: -12%` fazla agresifti, uzun ekranlarda görünür alandaki
   içeriği ıskalıyordu → `-5%` / `threshold 0`. Ayrıca güvenlik ağı eklendi:
   observer hiç ateşlenmezse 2.5sn sonra her şey yine de gösteriliyor. Reveal
   dekorasyon; altında sakladığı içerik sayfanın asıl amacı.

**Cihat'ın onayını bekleyen iki içerik notu:**
- Yolcu360 (2022—2024) ile Bookcars.com (2023—2024) tarihleri CV'de çakışıyor.
  Siteye CV'deki hâliyle yazıldı; kasıtlı değilse düzeltilmeli.
- Deneyim bölümü CV'den geldi, LinkedIn'den değil (LinkedIn HTTP 999 ile
  otomatik erişimi engelliyor).
