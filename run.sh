#! /bin/sh 

set -e 

./build_images.sh
docker-compose pull
docker-comose up --build
