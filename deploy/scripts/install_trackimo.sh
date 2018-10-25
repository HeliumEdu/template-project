#!/usr/bin/env bash

sudo apt-get install -y nodejs npm
sudo npm -g install yuglify
sudo ln -s /usr/bin/nodejs /usr/bin/node

sudo mkdir -p /usr/local/venvs
sudo chown ubuntu:ubuntu /usr/local/venvs

sudo chown -R ubuntu:ubuntu /srv/{%PROJECT_ID%}
cd /srv/{%PROJECT_ID%}

make install build migrate
