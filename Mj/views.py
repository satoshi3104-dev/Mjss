from django.shortcuts import render
from django.http import HttpResponse
from .models import MJhouse,station1,regionInfo1 
from bs4 import BeautifulSoup
import requests

def index(request):
    
     #麻雀王国より店舗情報を取得
     load_url = "https://mj-king.net/tempos/view/8431"
     html = requests.get(load_url)
     soup = BeautifulSoup(html.content,  "html.parser")

     #shoptableクラスをすべて取得
     table = soup.find_all(class_="shopTable")

     #お店の詳細情報を取得
     tags = table[0]
     td = tags.findAll("td")

     #店名,セット料金,フリー料金,最寄り駅を取得
     #店名
     title = td[0].text.strip() #空白を削除
     #セット料金
     setFee = td[8].text.strip()
     sFee = setFee[1:4] #セット料金を抽出
     #フリー料金
     freeFee = td[7].text.strip()
     fFee = freeFee[1:4] #セット料金を抽出
     #最寄り駅
     #nearestStation = "横浜駅"#td[3].text.strip()

     #お店のサービス情報を取得
     tags = table[1]
     tds = tags.findAll("td")

     #卓数を取得
     Mjtable = tds[0].text
     Mt = Mjtable[:-1]
     
     #destanceToStation=100
     #usertOfStation=100
     #eventTimes=10
     #annualINcome=100
     
     #Mjhouseオブジェクトを作成    
     house = MJhouse(name=title,setFee=sFee,FreeFee=fFee,mjTables=Mt)
     house.save() 
     mjHouseData = MJhouse.objects.all()
     #Stationオブジェクトを作成
     stationData = station1.objects.all()          
     #Regioninfoオブジェクトを作成
     regionData = regionInfo1.objects.all()
              
     params = {
             'MjData': mjHouseData,
             'staData': stationData,
             'regData': regionData,
         }
    
     return render(request, 'Mj/index.html', params)
