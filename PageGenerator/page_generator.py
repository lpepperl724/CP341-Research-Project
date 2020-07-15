#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:17:37 2020

@author: wydanielle
"""

from flask import Flask, redirect, url_for, render_template
import random
from functions import *


#%% Generating basic data for the person

# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask, render_template, url_for
  
# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__) 
  
# The route() function of the Flask class is a decorator,  
# which tells the application which URL should call  
# the associated function.

@app.route('/') 
# ‘/’ URL is bound with hello_world() function. 
def WikiPage(): 
    birth_date = dateGenerator()
    birth_place = placeGenerator()
    live_place = placeGenerator()
    
    return render_template('index.html', image = getImage(), name = nameGenerator(), birthdate = birth_date, birthplace = birth_place,liveplace = live_place)
 
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run(host='0.0.0.0',port=4478,debug=True) 
