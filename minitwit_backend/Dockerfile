FROM python:3
ENV PYTHONUNBUFFERED 1


RUN mkdir /minitwit_backend
WORKDIR /minitwit_backend
COPY requirements.txt /minitwit_backend/
EXPOSE 8080
RUN pip install -r requirements.txt
COPY . /minitwit_backend/
COPY ./scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
# RUN python manage.py makemigrations
# RUN python manage.py migrate