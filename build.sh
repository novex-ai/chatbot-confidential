#!/bin/bash

rm -rf frontend_quasar_vue/node_modules
rm -rf frontend_quasar_vue/dist

cd frontend_quasar_vue
npm install
npm run build
cd ..

docker buildx build --platform linux/amd64,linux/arm64 --push -t ${1:-chatbot-confidential-app} .
