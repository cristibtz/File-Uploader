FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
RUN mv files.conf /etc/nginx/conf.d
RUN ln -s /etc/nginx/conf.d/files.conf /etc/nginx/sites-enabled/