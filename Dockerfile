FROM nginx:alpine

# Server config: gzip, long-cache headers for assets, custom 404 page
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Static site (explicit list — build sources are intentionally excluded)
COPY index.html 404.html manifest.webmanifest robots.txt sitemap.xml \
     favicon.svg favicon.ico apple-touch-icon.png \
     icon-192.png icon-512.png og.png \
     /usr/share/nginx/html/

EXPOSE 80
