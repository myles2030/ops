#!/usr/bin/python3

from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import time
import numpy as np

cos_vect = list()
counting = 0
top_features = list()
urldata = list()
timecounted = list()
datacount = list()
tfidftime = list()
cosinetime = list()
urldata = list()
cos_result = list()
countingline = 0
cos_check = list()

app = Flask(__name__)

def cos_similarity(v1,v2):
    doc_product = np.dot(v1,v2)
    norm = (np.sqrt(sum(np.square(v1)))*np.sqrt(sum(np.square(v2))))
    similarity = doc_product / norm

    return similarity

@app.route('/')
def send():
    return render_template('web.html', results=0,wordcount = 0,timecount = 0,topword=0,message=0)

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

    warning ="success, but you can't analyze"

    return render_template('web.html', results = urlre,wordcount = wordre,timecount = timere,topword = 0,message = warning)

@app.route('/textfile', methods = ['GET','POST'])
def textfile():

    f = request.files['file']
    f.save(secure_filename(f.filename))
    
    tf = open("url_list.txt", "r")
    
    urlvalue = list()

    global countingline

    while True:
        line = tf.readline()
        if not line: break
        urldata.append(line[:-1])
        countingline = countingline + 1

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

    warning = "success"

    for cuv in range(countingline - 1):
        l = cuv + 1
        for l in range(countingline):
            if urldata[cuv] == urldata[l]:
                warning = "same url"
    for z in range(20):
         cos_check.append(0)
         cos_result.append(0)

    for m in range(countingline):

        cosinestart = time.time()

        tfidf_vect_simple = TfidfVectorizer()
        feature_vect_simple = tfidf_vect_simple.fit_transform(doc_list)

        feature_vect_dense = feature_vect_simple.todense()
        

        for i in range(countingline):
            cos_vect.append(np.array(feature_vect_dense[i]).reshape(-1,))
        
        for i in range(countingline):
            if(i != m):
                cos_check[i] = cos_similarity(cos_vect[m],cos_vect[i])
                cos_result[i] = cos_similarity(cos_vect[m],cos_vect[i])

        cosinetime.append(time.time()-cosinestart)
    
    cos_sorted = sorted(cos_check)

    for k in range(3):
        for r in range(countingline):
            if cos_sorted[k] == cos_result[r]:
                cos_resulturl.append(urldata[r] + "\n")


    tfidfstart = time.time()

    indices = np.argsort(tfidf_vect_simple.idf_)[::-1]
    features = tfidf_vect_simple.get_feature_names()
    top_n = 10
    tfidftime.append(time.time() - tfidfstart)

    topping = [features[i] for i in indices[:top_n]]
    lineto = "\n"

    for i in range(len(topping)):
        top_features.append(topping[i].replace(",","") + lineto)


    return render_template('web.html',results = urldata,wordcount = datacount,timecount = timecounted,topword = top_features,message= warning)

@app.route('/resulting', methods=['GET','POST'])
def resulting():
    return render_template('web.html',results = urldata,wordcount = datacount, timecount = tfidftime, topword = top_features)

@app.route('/cosinere', methods = ['GET','POST'])
def cosinere():
    return render_template('web.html',results = urldata, wordcount = datacount, timecount = cosinetime, urls = cos_resulturl)

if __name__ == "__main__":
    app.run()



