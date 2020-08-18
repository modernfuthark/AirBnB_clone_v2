#!/usr/bin/env bash
# Creates all the junk needed for Nginx on a server
# shellcheck disable=SC2016

# Install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo service restart nginx

# Create directories
sudo mkdir -p data/web_static/{releases/test,shared}

# Makes a file named index.html, adds filler into it
sudo echo "testing testing 123 " | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link between the test folder and file current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Change ownership of folder /data/
sudo chown -R ubuntu:ubuntu /data/

# i hate typing so use a shell variable for a string
str='server {
	listen 80 default_server;
	listen [::]:80 default_server;
	location /hbnb_static {
	alias /data/web_static/current/;
	index index.html;
	}
	location /tester {
        alias /var/www/html/;
        index tester.html;
        }
        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        add_header  X-Served-By $hostname;
	error_page 404 /not_found.html;
	location = /not_found.html {
		root /usr/share/nginx/html;
		internal;
	}
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	location / {
		try_files $uri $uri/ =404;
	}
}'

# Use string to edit default for nginx, then restart nginx
sudo echo "$str" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
