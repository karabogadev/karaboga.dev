# Dersler

## Headless Chrome ile görsel doğrulama

Bu repoda tasarım değişikliğini ekran görüntüsüyle doğrularken üç kez aynı
tuzağa düşüldü: **görüntüdeki kusur sayfada değil, ölçüm yönteminde çıktı.**
Bir sonraki seferde önce yöntemi doğrula, sonra kodu suçla.

- `--window-size` genişliği tam Chrome'da (`--headless` ve `--headless=new`)
  **500px'in altına inmiyor**: 390 istersen 500px layout alırsın, PNG 390'a
  kırpılır — bu "yatay taşma" gibi görünür ama değildir. `chrome-headless-shell`
  (ayrı binary) bu tabana sahip değil. Dar viewport için: shell, sabit genişlikli
  `<iframe>` ya da Playwright `viewport` (emülasyon; 320 gerçekten 320 verir).
  2026-10-10'da Chrome for Testing 151 ile yeniden ölçüldü.
- Taşmayı gözle değil ölçerek doğrula:
  `document.documentElement.scrollWidth` vs `clientWidth`. Iframe içindeki
  taşma ekran görüntüsünde kırpılır, hiç görünmez.
- `scroll-behavior: smooth` + fragment (`#about`) headless'ta yarım kalıyor;
  ekran görüntüsü boş kare yakalayabiliyor. Ölçüm için `scrollBehavior='auto'`.
- `--dump-dom` `load` anında DOM'u alır; load sonrası timer'lar hiç çalışmaz.
  `--virtual-time-budget` timer'ları çalıştırır ama CSS transition'ları
  güvenilir biçimde ilerletmez. Hesaplanan değere değil, sınıfın uygulanıp
  uygulanmadığına bak. Bütçesiz `--screenshot` da geçişi yarıda yakalayabilir.
- Bu makinede taze `--user-data-dir` ile Chrome for Testing `--dump-dom` ve
  `--screenshot`'ta sonsuza dek takılıyor. Bayrağı verme ya da Playwright kullan.

## Yazılara konan iddialar

Bir derse ya da hafızaya dayanan iddia yayınlanmadan önce yeniden üretilir.
`lessons.md`'deki dört headless Chrome iddiasından biri yeniden ölçünce yanlış,
biri eksik çıktı — not olarak yayınlansaydı yanlış bilgi yayılacaktı.

## Reveal animasyonları

Scroll-reveal dekorasyondur; altında sakladığı içerik sayfanın amacıdır.
`opacity: 0` varsayılanını asenkron bir observer'a bağlarken mutlaka zaman
aşımlı bir güvenlik ağı bırak — observer ateşlenmezse içerik kalıcı olarak
görünmez kalır ve bu sessiz bir hatadır.
