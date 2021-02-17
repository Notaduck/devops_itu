# FROM python:3.8-alpine
# ENV PATH="/scripts/${PATH}"

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# COPY ./requirements.txt /requirements.txt

# RUN apk add --update --no-cache --virtual .tmp gcc libc-dev postgresql-dev linux-headers


# RUN pip install -r /requirements.txt
# RUN apk del .tmp

# RUN mkdir minitwit/
# COPY ./ /app


# WORKDIR /app
# COPY ./scripts /scripts 

# RUN chmod +x /scripts/*
# RUN mkdir -p /vol/web/media
# RUN mkdir -p /vol/web/static

# RUN adduser -D app_user 
# RUN chown -R app_user:app_user /vol

# RUN chmod -R 755 /vol/web
# USER app_user

# CMD [ "entrypoint.sh" ]