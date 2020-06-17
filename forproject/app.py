#!/usr/bin/python3

from flask import Flask, render_template,request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def send():
    return render_template('web.html', address=0)

@app.route('/urladdress', methods=['GET', 'POST'])
def urladdress():
    if request.method == 'POST':
        temp = request.args.get('address')
        f = request.files['file']
        f.save(secure_filename(f.filename))

    return render_template('web.html', address= 'file uploaded successfully')

if __name__ == "__main__":
    app.run()




