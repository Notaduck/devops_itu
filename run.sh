#!/bin/bash 

set -e 

./build_images.sh
docker-compose pull
docker-compose up --build
