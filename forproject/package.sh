#!/bin/bash

mkdir templates
mv web.html templates/

echo"download pachages..."

pip3 install flask
pip3 install werkzeug
pip3 install bs4
pip3 install sklearn
pip3 install re
pip3 install numpy
pip3 install sys

chmod +x ./app.py

./app.py
