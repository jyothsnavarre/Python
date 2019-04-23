from bs4 import BeautifulSoup
import requests
import os
sym=[]
n=[]

r=requests.get("https://finance.yahoo.com/trending-tickers")
soup = BeautifulSoup(r.text,'html.parser')
symbol_list=soup.find_all('a',{"class":"Fw(b)"})
for symbol in symbol_list:
	if symbol.contents[0]!=" ":
		sym.append(symbol.contents[0])
		
name_list=soup.find_all('td',{"class":"data-col1 Ta(start) Pstart(10px) Miw(180px)"})
for name in name_list:
	if name.contents[0]!=" ":
		n.append(name.contents[0])
		
f=open("tickers.txt","x")
for x in range(len(sym)):
	f.write(sym[x]+"::"+n[x])
	f.write("\n")	
f.close()

for symbol in symbol_list:
	str1=symbol.contents[0]
	try:
		os.makedirs(os.path.join("Tickers",str1))
	except:
		print("Already Exists")
			
	page1=requests.get('https://finance.yahoo.com/quote/'+str1+'?p='+str1)
	soup1=BeautifulSoup(page1.text,'html.parser')
	f1=open("Tickers/"+str1+"/summary.html","w")
	f1.write(str(soup1.encode('utf-8')))
			
	page2=requests.get('https://finance.yahoo.com/quote/'+str1+'profile?p='+str1)
	soup2=BeautifulSoup(page2.text,'html.parser')
	f2=open("Tickers/"+str1+"/profile.html","w")
	f2.write(str(soup2.encode('utf-8')))
			
	page3=requests.get('https://finance.yahoo.com/quote/'+str1+'key-statistics?p='+str1)
	soup3=BeautifulSoup(page3.text,'html.parser')
	f3=open("Tickers/"+str1+"/statistics.html","w")
	f3.write(str(soup3.encode('utf-8')))
				
	page4=requests.get('https://finance.yahoo.com/quote/'+str1+'financials?p='+str1)
	soup4=BeautifulSoup(page4.text,'html.parser')
	f4=open("Tickers/"+str1+"/financials.html","w")
	f4.write(str(soup4.encode('utf-8')))
	
	