#!/bin/sh

docker-compose -f  docker-compose-deploy.yml down 
# docker-compose -f  docker-compose-deploy.yml build 
docker-compose -f  docker-compose-deploy.yml up --build
