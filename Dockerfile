FROM node:24-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --omit=dev

COPY . .

# Birleşik dağıtım (Coolify): ödeme sayfaları API'yi aynı origin üzerinden kullanır.
# Hestia/rsync ile statik dağıtımda meta varsayılanı https://api.cihat.app kalır.
RUN sed -i 's|<meta name="api-base" content="https://api.cihat.app">|<meta name="api-base" content="">|' odeme/index.html odeme/sonuc.html

RUN chown -R node:node /app

ENV NODE_ENV=production
EXPOSE 3000

USER node

CMD ["node", "api/server.js"]
