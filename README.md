[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/dashboard?id=notaduck_devops_itu)

[![BCH compliance](https://bettercodehub.com/edge/badge/notaduck/devops_itu?branch=main)](https://bettercodehub.com/)

[![Maintainability](https://api.codeclimate.com/v1/badges/18e22cb76095ee4d843d/maintainability)](https://codeclimate.com/github/notaduck/devops_itu/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/18e22cb76095ee4d843d/test_coverage)](https://codeclimate.com/github/notaduck/devops_itu/test_coverage)

# Minitwit project

## How to get started

```sh
sudo apt-get install docker-ce  && docker-compose
```

Next thing is to get the database running. You will have to be in the root direcotry of the root project.

```sh
sudo docker-compose up -d
```
The database should be up and running algonside with pgadminer on port `localhost:5050`. Please create a database named `minitwit`.

### Last step

In order to run the project locally you would simply have to run `docker-compose up -d`, and override your `host` file and point `api.minitwititu.xyz` and `minitwititu.xyz` to either `localhost` or `127.0.0.1`.



