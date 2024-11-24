FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
RUN mv nginx.conf /etc/nginx/conf.d
RUN ln -s /etc/nginx/conf.d/nginx.conf /etc/nginx/sites-enabled/