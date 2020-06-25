#!/usr/bin/python3

from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route('/')
def send():
    return render_template('web.html', results=0)

@app.route('/urladdress', methods=['GET', 'POST'])
def urladdress():
        temp = request.args.get('results')
        #f = request.files['file']
        #f.save(secure_filename(f.filename))
        
        webpage = urlopen(temp)
        bs = BeautifulSoup(webpage,'html.parser')
        tags = str(bs.findAll("div",{"class":"section"}))

        tags = re.sub('<.+?>',"",tags,0).strip()

        b = tags.replace('(',' ').replace(')',' ').replace(',',' ').replace('.',' ')replace(';',' ').replace('"',' ').replace("'"," ").split()

        count = len(b)
        
        return render_template('web.html', results = count)

if __name__ == "__main__":
    app.run()




