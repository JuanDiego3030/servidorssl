# Certbot Instructions for SSL Certificate Management

This directory contains instructions for using Certbot to obtain and manage SSL certificates from Let's Encrypt for the secure web server project.

## Prerequisites

1. Ensure that you have Nginx installed and configured to serve your Django application.
2. Your domain name should be pointed to the server's IP address.
3. Make sure that ports 80 (HTTP) and 443 (HTTPS) are open on your firewall.

## Installing Certbot

To install Certbot, you can use the following commands depending on your operating system:

### For Ubuntu

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx
```

### For CentOS

```bash
sudo yum install epel-release
sudo yum install certbot python2-certbot-nginx
```

## Obtaining an SSL Certificate

To obtain an SSL certificate, run the following command:

```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

Replace `yourdomain.com` with your actual domain name.

## Automatic Renewal

Certbot automatically sets up a cron job to renew your certificates. You can test the renewal process with:

```bash
sudo certbot renew --dry-run
```

## Troubleshooting

If you encounter issues, check the Certbot logs located at `/var/log/letsencrypt/letsencrypt.log` for more information.

## Further Information

For more detailed instructions and options, refer to the [Certbot documentation](https://certbot.eff.org/docs/).