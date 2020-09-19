# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:03:13 2020

@author: DELL-PC
"""

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    

    

if __name__ == '__main__':
    app.run()
    
    
   
