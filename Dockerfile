FROM caddy:latest

RUN apk add --no-cache python3
ADD ./scripts /scripts

CMD ["/bin/sh", "-c", "/scripts/tls-host-checker.py & caddy run --config /etc/caddy/Caddyfile --adapter caddyfile"]
