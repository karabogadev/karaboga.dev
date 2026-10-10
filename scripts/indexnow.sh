#!/bin/sh
# Tell IndexNow engines (Bing, Yandex, Seznam, Naver) that URLs changed.
# Bing's index also feeds ChatGPT search and Copilot. Google doesn't use IndexNow;
# it reads sitemap.xml.
#
#   scripts/indexnow.sh                         every URL in sitemap.xml
#   scripts/indexnow.sh https://karaboga.dev/notes/x [...]
#
# Run after the deploy is live: engines fetch the key file to verify ownership.
set -eu

cd "$(dirname "$0")/.."
host=karaboga.dev
key=$(basename "$(ls [0-9a-f]*.txt | head -n 1)" .txt)

if [ "$#" -eq 0 ]; then
  set -- $(sed -n 's:.*<loc>\(.*\)</loc>.*:\1:p' sitemap.xml)
fi

urls=$(printf '"%s",' "$@")
curl -sS -o /dev/null -w 'IndexNow: HTTP %{http_code} for '"$#"' URL(s)\n' \
  -H 'Content-Type: application/json; charset=utf-8' \
  --data "{\"host\":\"$host\",\"key\":\"$key\",\"keyLocation\":\"https://$host/$key.txt\",\"urlList\":[${urls%,}]}" \
  https://api.indexnow.org/indexnow
