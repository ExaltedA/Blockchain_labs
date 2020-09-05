from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests


# Create your views here.
def index(request):
    return render(request, 'index.html')


def EtherCurrent():
    source = requests.get('https://www.coingecko.com/en/coins/ethereum').text

    soup = BeautifulSoup(source, 'lxml')
    currency = soup.find('span', class_='no-wrap')

    return currency.text[1:]


def EtherClassicCurrent():
    source = requests.get('https://coinmarketcap.com/ru/currencies/ethereum-classic/').text

    soup = BeautifulSoup(source, 'lxml')
    currency = soup.find('span', class_='cmc-details-panel-price__price')

    return currency.text[1:]


def submitquery(request):
    q = request.GET['query']
    des = request.GET['dis']

    if des == 'e':
        cur = EtherCurrent()
        ans = float(q) * float(cur)

    else:
        cur = EtherClassicCurrent()
        ans = float(q) * float(cur)

    try:

        mydictionary = {
            "q": q,
            "ans": ans,
            "error": False,
            "result": True,
            "current": cur
        }
        return render(request, 'index.html', context=mydictionary)
    except:
        mydictionary = {
            "error": True,
            "result": False

        }
        return render(request, 'index.html', context=mydictionary)
