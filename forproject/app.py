#!/usr/bin/python3

from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import time

app = Flask(__name__)

@app.route('/')
def send():
    return render_template('web.html', results=0)

@app.route('/urladdress', methods=['GET', 'POST'])
def urladdress():
    temp = request.args.get('results')
    
    webpage = urlopen(temp)
    bs = BeautifulSoup(webpage,'html.parser')
    tags = str(bs.findAll("div",{"class":"section"}))

    tags = re.sub('<.+?>',"",tags,0).strip()

    start = time.time()

    b = tags.replace('(',' ').replace(')',' ').replace(',',' ').replace('.',' ').replace(';',' ').replace('"',' ').replace("'"," ").split()
        
    count = len(b)

    endtime = time.time()-start

    return render_template('web.html', results = count)

@app.route('/textfile', methods = ['GET','POST'])
def textfile():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    
    tf = open("text.txt", "r")

    urldata = list()
    urlvalue = list()
    countingline = 0

    while True:
        line = tf.readline()
        if not line: break
        urldata.append(line[:-1])
        countingline = countingline + 1

    datacount = list()

    for urllist in urldata:
        twebpage = urlopen(urllist)
        ash = BeautifulSoup(twebpage,'html.parser')
        buck = str(ash.findAll("div",{"class":"section"}))

        urlvalue.append("success")

        #fail: no url, and url that can't crawling.

        buck = re.sub('<.+?>',"",buck,0).strip()



        glaz = buck.replace('(',' ').replace(')',' ').replace(',',' ').replace('.',' ').replace(";"," ").replace('"',' ').replace("'"," ").split()
    
        datacount.append(len(glaz))

    return render_template('web.html',results = datacount)

if __name__ == "__main__":
    app.run()



