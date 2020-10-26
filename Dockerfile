FROM python:3.6-alpine3.9

#Installing essential packages

WORKDIR /ayen_task/
RUN apk update \
    && apk add --no-cache --virtual .build-deps \
    && apk add linux-headers poppler-dev python3-dev libxslt-dev libxml2-dev mysql-dev gcc musl-dev jpeg-dev zlib-dev mysql-client g++ \
    && apk add ca-certificates wget

ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN apk del .build-deps

ADD . .

RUN python manage.py collectstatic --noinput

CMD gunicorn ayen_task.wsgi:application --bind 0.0.0.0:$PORT --log-level $LOG_LEVEL