#!/bin/bash

# update raspbian
sudo apt-get -y update

# insall apache2
sudo apt-get -y install apache2

# install mod-wsgi-py3 for apache2
sudo apt-get install libapache2-mod-wsgi-py3

sudo service apache2 restart

# install pip3
sudo apt-get -y install python3-pip

# install django
sudo pip3 install django

# install Rpi.GPIO using Python 3.5 pip
pip3 install Rpi.GPIO

cd /etc/apache2/sites-available
# create backup for default virtual host
cp 000-default.conf 000-default.conf.bkp

echo "<VirtualHost *:80>

    #ServerName tankrobot
    ServerAdmin webmaster@localhost

    DocumentRoot /var/www/html

    ErrorLog /var/www/html/tank/error.log
    CustomLog /var/www/html/tank/access.log combined

    Alias /static /var/www/html/tank/static

    <Directory /var/www/html/tank/tank>
        <Files wsgi.py>
                Require all granted
        </Files>
    </Directory>

WSGIDaemonProcess example.com  python-path=/var/www/html/tank
WSGIProcessGroup example.com
WSGIScriptAlias  /tank  /var/www/html/tank/tank/wsgi.py process-group=example.com

 </VirtualHost>" > 000-default.conf

echo " add 'WSGIPythonPath /var/www/html/tank' at the end of the next file: "
nano /etc/apache2/apache2.conf

sudo service apache2 restart

# allow GPIO from apache 
sudo adduser www-data gpio