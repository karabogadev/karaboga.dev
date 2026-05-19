# karaboga.dev

Statik, hızlı ve SEO uyumlu kişisel tanıtım sayfası. Framework yok; yalnızca HTML, CSS ve birkaç yardımcı dosya.

## Yerel önizleme

Repo kökünde bir HTTP sunucusu çalıştırın (kök yolları `/styles.css` için doğru çözülsün):

```bash
python3 -m http.server 8080
```

Ardından tarayıcıda `http://localhost:8080` adresine gidin.

## GitHub Pages

1. Bu repoyu GitHub’a gönderin.
2. **Settings → Pages** bölümünde **Source** olarak `main` (veya `master`) dalını ve **root** (`/`) klasörünü seçin.
3. Yayın URL’i `https://<kullanıcı>.github.io/<repo-adı>/` olur.

**Özel alan adı (karaboga.dev):**

1. Aynı ayar sayfasında **Custom domain** alanına `karaboga.dev` yazın.
2. DNS sağlayıcınızda GitHub’ın [Pages özel alan belgelerinde](https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site) anlatıldığı gibi **A**, **AAAA** veya **CNAME** kayıtlarını ekleyin (apex için A kayıtları, `www` için CNAME yaygındır).
3. İsteğe bağlı: **Enforce HTTPS** seçeneğini etkinleştirin (sertifika hazır olduktan sonra).

## Dosyalar

| Dosya | Açıklama |
|--------|-----------|
| `index.html` | Ana sayfa, meta/OG, JSON-LD |
| `styles.css` | Stiller |
| `robots.txt` | Tarayıcı robotları |
| `sitemap.xml` | Site haritası |
| `favicon.svg` | Sekme ikonu |
