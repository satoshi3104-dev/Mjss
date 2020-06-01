from django.shortcuts import render
from django.http import HttpResponse
from .models import MJhouse,station1,regionInfo1 
#from bs4 import BeautifulSoup
#import requests

def index(request):
    
     #麻雀王国より店舗情報を取得
     load_url = "https://mj-king.net/tempos/view/8431"
