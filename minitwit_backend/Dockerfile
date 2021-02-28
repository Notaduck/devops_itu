FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"

RUN mkdir /minitwit_backend
WORKDIR /minitwit_backend
COPY requirements.txt /minitwit_backend/
EXPOSE 8080

RUN pip install -r requirements.txt

COPY . /minitwit_backend/
COPY scripts/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["/entrypoint.sh"]
# RUN python manage.py makemigrations
# RUN python manage.py migrate