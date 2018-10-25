#!/usr/bin/env bash

sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:certbot/certbot
sudo apt-get update

sudo apt-get install -y vim apache2 libapache2-mod-wsgi-py3 python-certbot-apache

sudo a2enmod wsgi ssl

sudo mkdir -p /var/log/apache2
sudo mkdir -p /var/log/{%PROJECT_ID%}
sudo chown ubuntu:ubuntu /var/log/{%PROJECT_ID%}

sudo cp /srv/{%PROJECT_ID%}/deploy/conf/django.conf /etc/apache2/sites-available/{%PROJECT_ID%}.conf

sudo a2dissite 000-default default-ssl
sudo a2ensite {%PROJECT_ID%}

sudo certbot --apache --non-interactive --agree-tos --email ${{%PROJECT_ID_UPPER%}_ADMIN_EMAIL} --domains {%PROJECT_HOST%}
