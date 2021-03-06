FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /minitwit_backend
WORKDIR /minitwit_backend
RUN mkdir ./scripts
COPY ./minitwit_backend/requirements.txt /minitwit_backend/
EXPOSE 8080

RUN pip install -r requirements.txt

COPY ./minitwit_backend /minitwit_backend/

COPY ./minitwit_frontend/scripts/entrypoint.sh /scripts/entrypoint.sh

RUN chmod +x /scripts/entrypoint.sh

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["/entrypoint.sh"]