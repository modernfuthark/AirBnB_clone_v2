#!/usr/bin/env bash
# Creates all the junk needed for Nginx on a server
# shellcheck disable=SC2016

# Install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create directories
sudo mkdir -p data/web_static/{releases/test,shared}

# Makes a file named index.html, adds filler into it
sudo echo "testing testing 123 " | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link between the test folder and file current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Change ownership of folder /data/
sudo chown -R ubuntu:ubuntu /data/

# Use string to edit default for nginx, then restart nginx
sudo sed -i '/pass the PHP/i\    location /hbnb_static {\n        alias /data/web_static/current;\n    }' /etc/nginx/sites-available/default
sudo service nginx restart
