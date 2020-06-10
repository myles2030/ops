#!/usr/bin/python3

from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def send():
    return render_template('web.html', address=0)

@app.route('/urladdress', methods=['GET'])
def urladdress():
    if request.method == 'GET':
        temp = request.args.get('address')

    return render_template('web.html', address=temp)



