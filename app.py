#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import *
from feedparser import parse
import feedparser
from datetime import datetime as dt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

def parseDate(dateData):
    return dt(
        dateData.tm_year,
        dateData.tm_mon,
        dateData.tm_mday,
        dateData.tm_hour,
        dateData.tm_min,
        dateData.tm_sec
    )

d = datetime.datetime.now() + datetime.timedelta(-30)

urls = [ 
	'blog feed url',
	'blog feed url',
	'blog feed url',
	'blog feed url',
	'blog feed url'
]

@app.route('/', methods=["GET", "POST"])
def index():
	entries = [
	    {
	        'title': entry['title'],
	        'link': entry['link'],
	        'date': parseDate(entry['updated_parsed'])
	    }
		for url in urls
	    for entry in parse(url).entries
	]
	entries.sort(key=lambda x: x['date'], reverse=True)
	return render_template('index.html',  entries=entries, d=d)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
