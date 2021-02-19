FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /minitwit_frontend
WORKDIR /minitwit_frontend

COPY requirements.txt /minitwit_frontend/
EXPOSE 8000

RUN pip install -r requirements.txt

COPY . /minitwit_frontend/
COPY scripts/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["/entrypoint.sh"]