#!/bin/sh

printf "$NGINX_USERNAME:$(openssl passwd -crypt $NGINS_PASSWORD)\n" > /etc/nignx.htpasswd
curl -L -O https://github.com/nginxinc/nginx-amplify-agent/raw/master/packages/install.sh
sh ./install.sh

# su - nginx