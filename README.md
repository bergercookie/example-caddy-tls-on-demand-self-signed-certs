# Caddy on-demand self-signed certificates

This is a minimal Docker-based example of how one could set-up caddy to act as a
reverse proxy for issuing on-demand self-signed certificates regardless of the
IP or domain name the client is connecting to.

You should be able to run `docker compose up`, then navigate to any of the
following and get a message that looks like the following:

```
You reached me over https using {hostname|IP address the client is connecting to}!
```

Assumming you're making the request from the host machine you're also running
`docker compose up`, any of the following should work and cddy should generate a
self-signed certificate for said name/IP:

* `localhost`
* `127.0.0.1`
* `<local IP address of the host machine running caddy>`
* `<hostname of host machine>`


On top of this you should also be able to set an arbitrary name to point to
`127.0.0.1` in the host's `/etc/hosts` and, assumming you restart your browser
for the changes in `/etc/hosts` to take effect, navigate to that name and get a
self-signed certificate for it as well.
