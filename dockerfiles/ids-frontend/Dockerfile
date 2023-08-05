FROM node:20-alpine
WORKDIR /app

COPY build /app/
COPY package.json /app/

RUN npm install && \
    npm build