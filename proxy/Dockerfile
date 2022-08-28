# this is a simplified version of tivix/docker-nginx:v6
# which supports Let's Encrypt
FROM alpine:3.14

RUN apk add --no-cache\
    nginx~=1.20 \
    py3-pip \
    gcc \
    g++ \
    libffi-dev \
    python3-dev \
    musl-dev \
    curl &&\
    pip3 install --upgrade pip &&\
    pip3 install --no-cache-dir \
    j2cli==0.3.10 \
    certbot-nginx==1.20.0 &&\
    curl -o /usr/local/bin/waitforit -sSL https://github.com/maxcnunes/waitforit/releases/download/v2.4.1/waitforit-linux_amd64 && \
    chmod +x /usr/local/bin/waitforit &&\
    rm -rf /etc/nginx/nginx.conf /etc/nginx/http.d/*

COPY ./ /code/
COPY docker-entrypoint.sh /usr/local/bin/

EXPOSE 80

ENTRYPOINT ["docker-entrypoint.sh"]
