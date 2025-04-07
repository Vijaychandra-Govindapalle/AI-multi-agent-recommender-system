# Dockerfile (inside frontend directory)
FROM node:20-slim


WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV NEXT_DISABLE_ESLINT=true

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
