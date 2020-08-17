#!/usr/bin/env bash
# Sets up directories, ownerships, and links for web static deployment

sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

if [ ! -d "/data/" ]
then
    sudo mkdir /data
fi

if [ ! -d "/data/web_static/" ]
then
    sudo mkdir /data/web_static
fi

if [ ! -d "/data/web_static/releases" ]
then
    sudo mkdir /data/web_static/releases
fi

if [ ! -d "/data/web_static/shared" ]
then
    sudo mkdir /data/web_static/shared
fi

if [ ! -d "/data/web_static/releases/test/" ]
then
    sudo mkdir /data/web_static/releases/test/
fi

htmltext="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

sudo bash -c 'echo "$htmltext" > /data/web_static/releases/test/index.html'

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

insertline="location /hbnb_static {\n\t\troot /data/web_static/current;\n\t}"
sudo sed -i "s@# pass the PHP@$insertline\n\n\t# pass the PHP@" /etc/nginx/sites-available/default
sudo service nginx restart
