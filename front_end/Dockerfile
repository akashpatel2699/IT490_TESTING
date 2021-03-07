FROM node:15.7.0-alpine3.10

MAINTAINER AKASH PATEL

WORKDIR /usr/src/app

COPY . .

RUN cd client && npm install && npm run build

WORKDIR /usr/src/app

RUN cd server && npm install

EXPOSE 3000

WORKDIR /usr/src/app

# CMD ["node","../server/server.js","&","npm","run","dev"]

#RUN apk add bash

CMD ["node","./server/server.js"]

# CMD ["./start.sh"]
