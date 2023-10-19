#!/bin/bash

rm -rf frontend_quasar_vue/node_modules
rm -rf frontend_quasar_vue/dist

cd frontend_quasar_vue
npm install
npm run build
cd ..

docker build -t ${1:-chatbot-confidential-app} .
