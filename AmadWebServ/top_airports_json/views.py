from django.shortcuts import render
from django.utils import simplejson

# Create your views here.
from django.http import HttpResponse
import pandas as pd
import numpy as np

def top_airports_json(request):
	n=int(request.GET.get('n', '10'))
	if n<1 :
		n=1
	if n>2274 :
		n=2274
	
	#BookFile='../../Data/BookingsNoDuplicates.csv'
	#BookFile='../../Data/bookings.csv'
	#BookingsAll = pd.read_csv(BookFile, sep='^', nrows=100, usecols=['arr_port','pax'])
	#BookingsAll=BookingsAll.dropna()
	#TopAirport = BookingsAll.groupby(['arr_port']).sum()
	#TopAirport = TopAirport.sort('pax', ascending=0)
	#TopAirport=TopAirport.reset_index()
	#TopN=TopAirport[:n]
	#TopN.index=TopN.index+1
	#jsonTopN=TopN.to_json(orient='records')
	

	SortedFile='../../Data/TopAirport2013Sorted.csv'
	Sorted2013 = pd.read_csv(SortedFile, sep='^')
	TopN=Sorted2013[:n]
	jsonTopN=TopN.to_json(orient='records')
	
	print >> open('WebOutputCheck.txt', 'w'), TopN , jsonTopN
    	#return HttpResponse(TopN)
	#return HttpResponse("Hello, world. You're at the Airport index numero 2.")
	return HttpResponse(jsonTopN)

#http://jsonformatter.curiousconcept.com/