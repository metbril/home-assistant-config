# HASS.io

This file contains specific details about my HASS.io installation.

## Host hardware

The system is currently running on a Raspberry Pi 2B. It is equipped with an ? GB SD Card.

## Installed Add-ons

### Nginx Proxy

The Nginx Proxy enables me to service more than one application to the Internet with exposing only 1 port to the outside world. Next to that, it's able to service LE certificate renewal.

### Duckdns

Although it believe is has not changed for ages, my ISP officialy provides me with a dynamic IP address. To be able to always use a hostname, I let the addon ping the duckdns service.

Using the separate addon, enables me to service multiple domains at once.

A hostname is convenient for remembering, but, more importantly, required for using certificates from Let's Encrypt.

### Lets Encrypt

### SSH

### Samba

