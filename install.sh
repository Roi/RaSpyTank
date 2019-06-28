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

# install requirments for pi video 
sudo apt-get -y install ffmpeg python3-picamera python3-ws4py

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
        DocumentRoot /var/www/html/

        ErrorLog /var/www/html/tank/error.log
        CustomLog /var/www/html/tank/access.log combined

        Alias /static /var/www/html/tank/static


        <Directory /var/www/html/tank>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        <Directory /var/www/html/tank/robot>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        <Directory /var/www/html/tank/camera>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>


WSGIDaemonProcess example.com  python-path=/var/www/html/tank
WSGIProcessGroup example.com
WSGIScriptAlias  /  /var/www/html/tank/wsgi.py process-group=example.com
WSGIScriptAlias  /robot  /var/www/html/tank/robot/wsgi.py process-group=example.com
WSGIScriptAlias  /camera  /var/www/html/tank/camera/wsgi.py process-group=example.com

LogLevel error
 </VirtualHost>
" > 000-default.conf

# allow GPIO from apache 
sudo adduser www-data gpio
sudo usermod -a -G video www-data

echo "change owner of /var/www/html to www-data"
sudo chown -R www-data:www-data /var/www/html

echo "set permision to 777 to /var/www/html"
sudo chmod -R 777 /var/www/html

echo "set a+x to stream.sh"
sudo chmod a+x /var/www/html/tank/camera/stream.sh

sudo service apache2 restart
