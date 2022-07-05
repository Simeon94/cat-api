#script to scrape cat categories from catapi
import requests
from fastapi import FastAPI
import json
import os
import urllib.request
import lxml
import webencodings
import html5lib
import pandas as pd
from json2html import *
from flask import Flask, Blueprint, redirect, url_for, render_template

# link for the index.html file
template_dir = os.path.abspath('./')

# app variable for Flask: method was useful, research and deployed it
app = Flask(__name__, template_folder=template_dir)


"""
    This app is used to scrape data in a json format. Data extracted is then transformed
    to a dataframe, then  to an html file which is then rendered to webpage at the address http://127.0.0.1:5000/
    app attributes:
    url (str): this specifies where the data is being extracted from.
    
   data schema:  
    id: int
    index: int
    name: str
"""     


@app.route("/")
def index():
    url = "https://api.thecatapi.com/v1/categories"
    
    #key for connection
    headers = {'x-api-key': '5baba247-1b72-4049-bd44-53cea33b8b97'}

    response = requests.request("GET", url, headers=headers)
    
    #called response at json
    cats = response.json()
    print(cats)

    #write cats to df
    df = pd.DataFrame.from_dict(cats)
    df_html = df.to_html()
    print(df_html)
    
    #write html to file
    text_file = open("index.html", "w")
    text_file.write(df_html)
    text_file.close()
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
