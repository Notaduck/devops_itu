FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./nginx/uwsgi_params /etc/nginx/uwsgi_params

USER root
# RUN apk --no-cache add curl
# RUN curl -L -O https://github.com/nginxinc/nginx-amplify-agent/raw/master/packages/install.sh
# RUN sh ./install.sh
RUN mkdir -p /vol/static
RUN chmod 755 /vol/static

USER nginx
