#!/bin/ash -e

mkdir -p /run/nginx/
rm -rf /run/nginx/nginx.pid

if [ ${#} -eq 0 ]; then
  echo "Configuring nginx..."
  ls -la /etc/nginx
  j2 --undefined /code/templates/nginx.conf.j2 > /etc/nginx/nginx.conf
  j2 --undefined /code/templates/site.conf.j2 > /etc/nginx/conf.d/site.conf

  if [[ "${ENABLE_SSL}" == "true" ]]; then
    echo "Installing Certbot"
    apk add --no-cache certbot \
    && certbot certonly --standalone --agree-tos -m "${CERTBOT_EMAIL}" -n -d ${DOMAIN_LIST} \
    && echo -e "#!/bin/sh\n\ncertbot renew --nginx" >/etc/periodic/daily/certbot-renew \
    && chmod +x /etc/periodic/daily/certbot-renew

    # run crond in the background with a log level of 8
    crond -b -L /var/log/cron.log
  fi
  echo "Starting nginx..."
  exec nginx -g 'daemon off;'
else
  exec "${@}"
fi
