FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY files.conf /etc/nginx/conf.d
RUN mkdir /etc/nginx/sites-enabled && ln -s /etc/nginx/conf.d/files.conf /etc/nginx/sites-enabled/