from bs4 import BeautifulSoup
import requests
import csv
import lxml
import os
lis=[]
tick=""
Name=""
LastPrice=""
MarketTime=""
Change=""
csvw=open('tickers.txt','w',newline='')
csv_writer=csv.writer(csvw)
csv_writer.writerow(['Symbol      Name'])
source=requests.get( 'https://finance.yahoo.com/trending-tickers').text
soup=BeautifulSoup(source,'lxml')
containers=soup.findAll('tr')
for container in containers:
      for i in container.findAll("td",{"class":"data-col0 Ta(start) Pstart(6px) Pend(15px)"}):
        tick=i.text
      for j in container.findAll("td",{"class":"data-col1 Ta(start) Pstart(10px) Miw(180px)"}):
          Name=j.text
      print(tick.strip()+" "+Name)
      if(tick!="" and Name!=""):
       csv_writer.writerow([tick+"::"+Name.strip('"')])
      newpath = r'C:\Users\MTS\PycharmProjects\projectStock\%s' % (tick)
      if not os.path.exists(newpath):
          os.makedirs(newpath)
      if (tick != ""):
        url0='https://finance.yahoo.com/quote/%s/financials?p=%s' % (tick,tick)
        respo = requests.get(url0)


        f = open(r'C:\Users\MTS\PycharmProjects\projectStock\%s\financials.html' %(tick), 'wb')
        f.write(respo.content)
        f.close
        url1 = 'https://finance.yahoo.com/quote/%s/key-statistics?p=%s' % (tick, tick)
        respo = requests.get(url1)

        f = open(r'C:\Users\MTS\PycharmProjects\projectStock\%s\statistics.html' % (tick), 'wb')
        f.write(respo.content)
        f.close
        url2 = 'https://finance.yahoo.com/quote/%s/profile?p=%s' % (tick, tick)
        respo = requests.get(url2)

        f = open(r'C:\Users\MTS\PycharmProjects\projectStock\%s\profile.html' % (tick), 'wb')
        f.write(respo.content)
        f.close

      fil=open('ti.txt','a')
      fil.write(tick+"\n")







