from django.shortcuts import render
from django.utils import simplejson

# Create your views here.
from django.http import HttpResponse
import pandas as pd
import numpy as np

def index(request):
	html = "<html><body>\
	Welcome to Amadeus Data Processing Unit.<br> <br> \
	We have access to the total number of passengers for every airport (year 2013).<br> \
	The airports are sorted by the number of arriving passengers.<br> \
	This list is huge, so please giveus a number of the top arriving airports you whish to see:<br> \
	<br> <br> <br> <br> \
	The output will be given in JSON format<br> \
	You can validate the output at: http://jsonformatter.curiousconcept.com/<br> \
	</body></html>"
	return HttpResponse(html)
	


