FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /minitwit_frontend
WORKDIR /minitwit_frontend
RUN echo '-------------------'
RUN pwd
RUN ls

RUN echo '-------------------'
COPY ./minitwit_frontend/requirements.txt /minitwit_frontend/
EXPOSE 8000

RUN pwd
RUN ls -al 
# RUN ls -al ./minitwit_frontend
RUN pip install -r ./minitwit_frontend/requirements.txt

COPY ./minitwit_frontend /minitwit_frontend/
COPY ./minitwit_frontend/scripts/entrypoint.sh /entrypoint.sh

RUN chmod +x ./scripts/entrypoint.sh

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["/scripts/entrypoint.sh"]
