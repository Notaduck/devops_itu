# minitwit project

## How to get started

This tutorial expects you to run some kind of debian os.

### Get your virtual enviroment running

```sh
python -m pip install virtualenv
```

### Get psycopg2 and Django

```sh
sudo apt-get install libpq-dev
```

In order tovalidate that you have `pg_config` please run the following in your terminal

```sh
pg_config
```

Next thing is to install the `psycopg2`

```sh
python -m pip install psycopg2
```

```sh
python -m pip install django 
```

### How to setup docker

```sh
sudo apt-get install docker-ce  && docker-compose
```

Next thing is to get the database running. You will have to be in the root direcotry of the root project.

```sh
sudo docker-compose up -d
```
The database should be up and running algonside with pgadminer on port `localhost:5050`. Please create a database named `minitwit`.

### Last step

:kissing_closed_eyes:

```sh
python manage.py runserver 127.0.0.1:8000
```

## Deploy the project

In order to deploy the project tree enviroment files has to be created with the following structure

`.postgres.env`
```
POSTGRES_USER=........
POSTGRES_PASSWORD=........
```

`.api.env`
```
SECRET_KEY=..................
DB_NAME=........
DB_USER=........
DB_PASSWORD=........
DB_HOST=..
ALLOWED_HOSTS=127.0.0.1,localhost,api.minitwititu.dk
```

```
SECRET_KEY=..................
DB_NAME=........
DB_USER=........
DB_PASSWORD=........
DB_HOST=..
ALLOWED_HOSTS=127.0.0.1,localhost,minitwititu.dk
```

Next step is simply to run the `deploy.sh` script which will tear down any existing containers, then build and run the new ones.

