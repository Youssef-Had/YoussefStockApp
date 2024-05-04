from django.shortcuts import render
from django.http import HttpResponse
import yfinance as yf
import pandas as pd
from .models import StockData

# Create your views here.

def index(request) :
    return render(request,'stockpages/index.html')

def getdata(request):
    stock = request.POST.get('stocksymbol')
    sdate = request.POST.get('startdate')
    edate = request.POST.get('enddate')
    print(stock)
    print(sdate)
    print(edate)
    stock_symbol = yf.Ticker(stock)
    data = stock_symbol.history(start=sdate, end=edate)
    df = pd.DataFrame(data[['Open', 'Close']])
    for i in df.itertuples():
        print(i)
        StockData.objects.create(tickersymbol = stock_symbol, date = i[0], openprice = i[1], closeprice = i[2])
    query_results = StockData.objects.all()
    query_date_list = list(StockData.objects.values_list('date'))
    print(query_date_list)
    context = { 
        'query_results' : query_results,
        'stockdata':stock,
        'startdata':sdate,
        'enddata':edate,
     }

    return render(request, 'stockpages/index.html',context)
