# this is a simplified version of tivix/docker-nginx:v6
# which supports Let's Encrypt
FROM alpine:3.12

RUN apk add --no-cache\
    nginx~=1.18 \
    py3-pip \
    curl &&\
    pip3 install --no-cache-dir \
    j2cli==0.3.10 \
    boto3==1.12.26 &&\
    curl -o /usr/local/bin/waitforit -sSL https://github.com/maxcnunes/waitforit/releases/download/v2.4.1/waitforit-linux_amd64 && \
    chmod +x /usr/local/bin/waitforit &&\
    rm -rf /etc/nginx/nginx.conf /etc/nginx/conf.d/*

COPY ./ /code/
COPY docker-entrypoint.sh /usr/local/bin/

EXPOSE 80

ENTRYPOINT ["docker-entrypoint.sh"]
