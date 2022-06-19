#script to scrape cat breeds from catapi
import requests
from pydantic import BaseModel
import os
import urllib.request
import pandas as pd
from flask import Flask, Blueprint, redirect, url_for, render_template

"""
    This app is used to scrape data in a json format. Data extracted is then transformed
    to a dataframe, then to an html file which is then rendered to webpage at the address http://127.0.0.1:5000/
    app attributes:
    url (str): this specifies where the data is being extracted from.
    
   data schema:  
    id: str
    name: str
    temperament: str
    life_span: str
    alt_names: str
    wikipedia_url: str
    origin: str
    weight_imperial: str
    experimental: int
    hairless: int
    natural: int
    rare: int
    rex: int
    suppress_tail: int
    short_legs: int
    hypoallergenic: int
    adaptability: int
    affection_level: int
    country_code: str
    child_friendly: int
    dog_friendly: int
    energy_level: int
    grooming: int
    health_issues: int
    intelligence: int
    shedding_level: int
    stranger_friendly: int
    vocalisation: int
"""     

template_dir = os.path.abspath('./')
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def index1():
    url = "https://api.thecatapi.com/v1/breeds"

    headers = {'x-api-key': '5baba247-1b72-4049-bd44-53cea33b8b97'}

    response = requests.request("GET", url, headers=headers)

    cats_breed = response.json()
    #print(cats)
    
    #write cats to df
    df = pd.DataFrame.from_dict(cats_breed)
    df_html = df.to_html()
    print(df_html)
    
    #write html to file
    text_file = open("index.html1", "w")
    text_file.write(df_html)
    text_file.close()
    return render_template("index.html1")

if __name__ == '__main__':
    app.run(debug=True)
