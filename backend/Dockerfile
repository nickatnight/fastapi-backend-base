FROM alpine:3.14

LABEL maintainer Nick <nick@night.com>

WORKDIR /code/

 # Install base packages
RUN apk add --no-cache \
    bash \
    curl \
    python3-dev \
    py3-pip \
    postgresql-dev \
    gcc \
    libffi-dev \
    g++ \
    musl-dev &&\
    pip3 install --upgrade pip &&\
    rm -rf /tmp/*

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python3 && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create true

# Copy poetry.lock* in case it doesn't exist in the repo
COPY . /code/

# Allow installing dev dependencies to run tests
# ARG INSTALL_DEV=false
# RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"
RUN poetry install --no-root

ENV PYTHONPATH "${PYTHONPATH}:/code"

EXPOSE 8000
