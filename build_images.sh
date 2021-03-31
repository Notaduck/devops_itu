#!/bin/bash

set -e

echo "Building Minitwit Images"
docker build -t "$DOCKER_USERNAME"/minitwit_web -f Dockerfile-web .
docker build -t "$DOCKER_USERNAME"/minitwit_api -f Dockerfile-api .
docker build -t "$DOCKER_USERNAME"/minitwit_proxy -f Dockerfile-proxy .

echo "Login to Dockerhub, provide your password below..."
read -s DOCKER_PASSWORD
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

echo "Pushing Minitwit Images to Dockerhub..."
docker push "$DOCKER_USERNAME"/minitwit_web:latest
docker push "$DOCKER_USERNAME"/minitwit_api:latest
docker push "$DOCKER_USERNAME"/minitwit_proxy:latest
