from django.shortcuts import render
from django.utils import simplejson

# Create your views here.
from django.http import HttpResponse
import pandas as pd
import numpy as np

def index(request):
	html = "<html>\
	<head><title>Top N</title></head>\
	<body>\
	Welcome to Amadeus Data Processing Unit.<br> <br> \
	2013 was great year for airport transport, but what do you think,  which airport had the highest number of passengers?.<br> \
	Well, we have sorted the airports by the number of arriving passengers.<br> \
	This list is huge, so please giveus a number of the top arriving airports you whish to see:<br> \
	<form action=\"/top_airports_json/\" method=\"get\">\
  	Airports number: <input type=\"text\" name=\"n\"><br>\
  	<input type=\"submit\" value=\"Submit\">\
	</form>	\
	<br> <br> <br> <br> \
	The output will be given in JSON format<br> \
	You can validate the output at: <a href=\"http://jsonformatter.curiousconcept.com\" > http://jsonformatter.curiousconcept.com </a> \
	</body></html>"
	return HttpResponse(html)
	


