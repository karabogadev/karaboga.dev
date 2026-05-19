FROM nginx:alpine

# Server config: gzip, long-cache headers for assets, custom 404 page
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Static site (explicit list — build sources are intentionally excluded)
COPY index.html 404.html manifest.webmanifest robots.txt sitemap.xml styles.css \
     favicon.svg favicon.ico apple-touch-icon.png \
     icon-192.png icon-512.png avatar.jpg \
     /usr/share/nginx/html/

# If og.png is committed, COPY it alongside the other assets and delete this line.
RUN cp /usr/share/nginx/html/icon-512.png /usr/share/nginx/html/og.png

EXPOSE 80
