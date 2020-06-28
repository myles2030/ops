#!/usr/bin/python3

from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import time
import numpy as np

app = Flask(__name__)

def cos_similarity(v1,v2):
    doc_product = np.dot(v1,v2)
    norm = (np.sqrt(sum(np.square(v1)))*np.sqrt(sum(np.square(v2))))
    similarity = doc_product / norm

    return similarity

@app.route('/')
def send():
    return render_template('web.html', results=0,wordcount = 0,timecount = 0)

@app.route('/urladdress', methods=['GET', 'POST'])
def urladdress():
    urlre = list()
    wordre = list()
    timere = list()


    temp = request.args.get('results')
    
    webpage = urlopen(temp)
    bs = BeautifulSoup(webpage,'html.parser')
    tags = str(bs.findAll("div",{"class":"section"}))

    tags = re.sub('<.+?>',"",tags,0).strip()

    start = time.time()

    b = tags.replace('(',' ').replace(')',' ').replace(',',' ').replace('.',' ').replace(';',' ').replace('"',' ').replace("'"," ").split()
        
    count = len(b)

    endtime = time.time()-start

    urlre.append(temp)
    wordre.append(count)
    timere.append(endtime)

    return render_template('web.html', results = urlre,wordcount = wordre,timecount = timere)

@app.route('/textfile', methods = ['GET','POST'])
def textfile():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    
    tf = open("url_list.txt", "r")

    urldata = list()
    urlvalue = list()
    countingline = 0

    while True:
        line = tf.readline()
        if not line: break
        urldata.append(line[:-1])
        countingline = countingline + 1

    datacount = list()
    timecounted = list()
    doc_list = list()

    for urllist in urldata:
        twebpage = urlopen(urllist)
        ash = BeautifulSoup(twebpage,'html.parser')
        buck = str(ash.findAll("div",{"class":"section"}))


        urlvalue.append("success")

        #fail: no url, and url that can't crawling.

        buck = re.sub('<.+?>',"",buck,0).strip()

        doc_list.append(buck)
        
        txstart=time.time()

        glaz = buck.replace('(',' ').replace(')',' ').replace(',',' ').replace('.',' ').replace(";"," ").replace('"',' ').replace("'"," ").split()
    
        datacount.append(len(glaz))

        txendtime = time.time() - txstart

        timecounted.append(txendtime)


    tfidf_vect_simple = TfidfVectorizer()
    feature_vect_simple = tfidf_vect_simple.fit_transform(doc_list)

    feature_vect_dense = feature_vect_simple.todense()

    vect1 = np.array(feature_vect_dense[0]).reshape(-1,)
    vect2 = np.array(feature_vect_dense[1]).reshape(-1,)
    
    indices = np.argsort(tfidf_vect_simple.idf_)[::-1]
    features = tfidf_vect_simple.get_feature_names()
    top_n = 10

    top_features = [features[i] for i in indices[:top_n]]

    return render_template('web.html',results = urldata,wordcount = datacount,timecount = top_features)



if __name__ == "__main__":
    app.run()



