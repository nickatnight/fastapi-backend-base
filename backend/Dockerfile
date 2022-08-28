FROM alpine:3.14

LABEL maintainer Nick <nick@night.com>

ARG env
ENV REQUIREMENTS_FILE ${env:-dev}.txt
ENV PYTHONPATH "${PYTHONPATH}:/code"

 # Install base packages
RUN apk add --no-cache \
    bash \
    python3-dev \
    py3-pip \
    postgresql-dev \
    gcc \
    libffi-dev \
    g++ \
    musl-dev &&\
    pip3 install --upgrade pip &&\
    rm -rf /tmp/*


ADD /requirements/base.txt /requirements/$REQUIREMENTS_FILE /tmp/
RUN pip3 install --no-cache-dir -r /tmp/$REQUIREMENTS_FILE

ADD . /code/
WORKDIR /code/

EXPOSE 8000
