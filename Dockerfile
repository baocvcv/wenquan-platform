FROM node:10.16.1

RUN npm config set registry https://registry.npm.taobao.org

ENV HOME=/opt/app

WORKDIR $HOME

COPY . $HOME

WORKDIR $HOME/frontend

RUN npm install

RUN npm run build

EXPOSE 8080

CMD npm run serve

