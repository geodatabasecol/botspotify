#!/bin/bash
sudo apt update
sudo apt -y upgrade
wget -P ~/Downloads/ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i ~/Downloads/google-chrome*.deb
wget https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip
unzip chromedriver_linux64

sudo mv chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

sudo pip3 install selenium
sudo pip3 install webdriver-manager
sudo pip3 install pymongo
sudo pip3 install "pymongo[srv]"

pip3 freeze
whereis chromedriver
whereis google-chrome
exit
