FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev
# install dependencies

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade -r requirements.txt
EXPOSE 8000

COPY . .
RUN python manage.py migrate
ENTRYPOINT ["python","manage.py","runserver","0.0.0.0:8000"]
