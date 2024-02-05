FROM nginx

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./certs/ /certs
COPY ./500.html ./502.html ./503.html ./504.html /usr/share/nginx/html/

EXPOSE 80

# Команда для создания сертификата openssl req -x509 -newkey rsa:4096 -keyout certs/nginx.key -out certs/nginx.crt -days 1825 -nodes -subj "/CN=localhost"