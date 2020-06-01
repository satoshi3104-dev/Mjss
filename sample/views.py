from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import house,station1,regionInfo1
from .forms import FindForm,SelectForm
from beautifulsoup4 import BeautifulSoup
import requests

def index(request, num=1):
     #麻雀王国より店舗情報を取得
     load_url = "https://mj-king.net/tempos/view/10160"
     html = requests.get(load_url)
     soup = BeautifulSoup(html.content,  "html.parser")

     #shoptableクラスをすべて取得
     table = soup.find_all(class_="shopTable")

     #お店の詳細情報を取得
     tags = table[0]
     td = tags.findAll("td")

     #店名,セット料金,フリー料金,最寄り駅、市町村を取得
     #店名
     title = td[0].text.strip() #空白を削除
     #住所
     address = td[1].text.strip() #余分な文字を削除
     add = address.replace("\t", "")
     add = add.replace("\r", "")
     add = add.replace("\n", "")
     add = add.replace("[地図]", "")
     add = add.replace("\xa0", "")

     #セット料金
     setFee = td[8].text.strip()
     sFee = setFee[1:4] #セット料金を抽出
     if sFee.isdigit() != True:
        sFee = "11"

     #フリー料金
     freeFee = td[7].text.strip()
     fFee = freeFee[1:4] #セット料金を抽出
     if fFee.isdigit() != True:
        fFee = "11"
     
     #最寄り駅
     nstation = "蒲田駅"
     #市町村
     city = "大田"

     #お店のサービス情報を取得
     tags = table[1]
     tds = tags.findAll("td")

     #卓数を取得
     Mjtable = tds[0].text
     Mt = Mjtable[:-1]

     #stationテーブルより駅名を取得
     nstation = station1.objects.filter(stationName=nstation)
     sta = nstation[0]

     #regionInfoテーブルより駅名を取得
     city = regionInfo1.objects.filter(cityName=city)
     ci = city[0]

     #Mjhouseオブジェクトを作成    
     house1 = house(name=title,setFee=sFee,FreeFee=fFee,mjTables=Mt,address=add,station=sta,city=ci)

     house1.save() 
     mjHouseData = house.objects.all()
     page = Paginator(mjHouseData, 10)     

     params = {
             'MjData': page.get_page(num),
             'form': SelectForm(),
         }
    
     return render(request, 'sample/index.html', params)
 
def find(request):
    form = SelectForm(request.POST)
    str = request.POST['select']
    data = house.objects.filter(station=str)
    
    params = {
             'MjData': data,
             'form': form,
          }
    
    return render(request, 'sample/index.html', params)
