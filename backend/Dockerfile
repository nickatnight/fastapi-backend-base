FROM python:3.8-slim-buster

ARG env
ARG requirements_file
ENV REQUIREMENTS_FILE ${requirements_file:-dev.txt}

RUN apt-get update &&\
    apt-get install --yes --no-install-recommends \
    gcc \
    musl-dev \
    postgresql-client \
    postgresql-contrib \
    python3-dev \
    python3-pip &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --upgrade pip

ADD /requirements/base.txt /requirements/$REQUIREMENTS_FILE /tmp/
RUN pip3 install --no-cache-dir -r /tmp/$REQUIREMENTS_FILE

ADD . /code/
WORKDIR /code/
