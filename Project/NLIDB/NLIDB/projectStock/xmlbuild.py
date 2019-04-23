from xml.dom import minidom
from bs4 import BeautifulSoup

fio=open('ti.txt','r')
k=1

for i in fio:
    doc = minidom.Document()
    fp = open("%s\statistics.html" % (i.strip()), 'r')
    sou = fp.read()
    soup = BeautifulSoup(sou, 'lxml')
    root = doc.createElement('html')
    doc.appendChild(root)
    statistics=doc.createElement('statistics')
    srno = doc.createElement('srno')
    text = doc.createTextNode("%s" % str(k))
    srno.appendChild(text)
    statistics.appendChild(srno)
    root.appendChild(statistics)
    stat_tik=doc.createElement('stat_tik')
    tex=doc.createTextNode(str(i.strip()))
    stat_tik.appendChild(tex)
    statistics.appendChild(stat_tik)
    root.appendChild(statistics)
    marketcap = doc.createElement('marketcap')
    for g in soup.findAll("td", {"data-reactid": "19"}):
      tex2 = doc.createTextNode(g.text)
    marketcap.appendChild(tex2)
    statistics.appendChild(marketcap)
    root.appendChild(statistics)
    Enterprisevalue = doc.createElement('Enterprisevalue')
    for g in soup.findAll("td", {"data-reactid": "26"}):
        tex3 = doc.createTextNode(g.text)
    Enterprisevalue.appendChild(tex3)
    statistics.appendChild(Enterprisevalue)
    root.appendChild(statistics)
    RetOnAss = doc.createElement('RetOnAss')
    for g in soup.findAll("td", {"data-reactid": "133"}):
        tex4 = doc.createTextNode(g.text)
    RetOnAss.appendChild(tex4)
    statistics.appendChild(RetOnAss)
    root.appendChild(statistics)
    TotCash = doc.createElement('TotCash')
    for g in soup.findAll("td", {"data-reactid": "213"}):
        tex5 = doc.createTextNode(g.text)
    for g in soup.findAll("td", {"data-reactid": "214"}):
        tex5 = doc.createTextNode(g.text)
    TotCash.appendChild(tex5)
    statistics.appendChild(TotCash)
    root.appendChild(statistics)
    proMar = doc.createElement('proMar')
    for g in soup.findAll("td", {"data-reactid": "114"}):
        tex6 = doc.createTextNode(g.text)
    proMar.appendChild(tex6)
    statistics.appendChild(proMar)
    root.appendChild(statistics)
    grossPro = doc.createElement('grossPro')
    for g in soup.findAll("td", {"data-reactid": "173"}):
        tex7 = doc.createTextNode(g.text)
    grossPro.appendChild(tex7)
    statistics.appendChild(grossPro)
    root.appendChild(statistics)
    ooCash = doc.createElement('ooCash')
    for g in soup.findAll("td", {"data-reactid": "261"}):
        tex8 = doc.createTextNode(g.text)
    for g in soup.findAll("td", {"data-reactid": "260"}):
        tex8 = doc.createTextNode(g.text)
    ooCash.appendChild(tex8)
    statistics.appendChild(ooCash)
    root.appendChild(statistics)
    totdebt = doc.createElement('totdebt')
    for g in soup.findAll("td", {"data-reactid": "228"}):
        tex9 = doc.createTextNode(g.text)
    for g in soup.findAll("td", {"data-reactid": "227"}):
        tex9 = doc.createTextNode(g.text)
    totdebt.appendChild(tex9)
    statistics.appendChild(totdebt)
    root.appendChild(statistics)
    currat = doc.createElement('currat')
    for g in soup.findAll("td", {"data-reactid": "242"}):
        tex10 = doc.createTextNode(g.text)
    for g in soup.findAll("td", {"data-reactid": "241"}):
        tex10 = doc.createTextNode(g.text)
    currat.appendChild(tex10)
    statistics.appendChild(currat)
    root.appendChild(statistics)
    lever = doc.createElement('lever')
    for g in soup.findAll("td", {"data-reactid": "268"}):
        tex11 = doc.createTextNode(g.text)
    for g in soup.findAll("td", {"data-reactid": "267"}):
        tex11 = doc.createTextNode(g.text)
    lever.appendChild(tex11)
    statistics.appendChild(lever)
    root.appendChild(statistics)
    fp1 = open("%s\%s.html" % (i.strip(),"financials"), 'r')
    sou1 = fp1.read()
    soup1 = BeautifulSoup(sou1, 'lxml')
    financials = doc.createElement('financials')
    fintick = doc.createElement('fintick')
    tex12 = doc.createTextNode(i.strip())
    fintick.appendChild(tex12)
    financials.appendChild(fintick)
    root.appendChild(financials)
    TotRev= doc.createElement('TotRev')
    for g in soup1.findAll("span", {"data-reactid": "40"}):
        tex13 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "42"}):
        tex13 = doc.createTextNode(g.text)
    for g in soup1.findAll("td", {"data-reactid": "41"}):
        tex13 = doc.createTextNode(g.text)
    print(tex13)
    TotRev.appendChild(tex13)
    financials.appendChild(TotRev)
    root.appendChild(financials)
    costRev = doc.createElement('costRev')
    for g in soup1.findAll("span", {"data-reactid": "49"}):
        tex112 = doc.createTextNode(g.text)
    costRev.appendChild(tex112)
    financials.appendChild(costRev)
    root.appendChild(financials)
    incBefTax = doc.createElement('incBefTax')
    for g in soup1.findAll("span", {"data-reactid": "168"}):
        tex13 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "147"}):
        tex13 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "146"}):
        tex13 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "148"}):
        tex13 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "172"}):
        tex13 = doc.createTextNode(g.text)
    incBefTax.appendChild(tex13)
    financials.appendChild(incBefTax)
    root.appendChild(financials)
    Netinc = doc.createElement('Netinc')
    for g in soup1.findAll("span", {"data-reactid": "210"}):
        tex14 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "209"}):
        tex14 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "211"}):
        tex14 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "250"}):
        tex14 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "242"}):
        tex14 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "214"}):
        tex14 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "205"}):
        tex14 = doc.createTextNode(g.text)
    for g in soup1.findAll("span", {"data-reactid": "171"}):
        tex14 = doc.createTextNode(g.text)
    Netinc.appendChild(tex14)
    financials.appendChild(Netinc)
    root.appendChild(financials)
    fp2 = open("%s\profile.html" % (i.strip()), 'r')
    sou2 = fp2.read()
    soup2 = BeautifulSoup(sou2, 'lxml')
    profiles = doc.createElement('profiles')
    protick = doc.createElement('protick')
    tex12 = doc.createTextNode(i.strip())
    protick.appendChild(tex12)
    profiles.appendChild(protick)
    root.appendChild(profiles)
    name = doc.createElement('name')
    for g in soup2.findAll("h3", {"data-reactid": "6"}):
       tex12 = doc.createTextNode(g.text)
    name.appendChild(tex12)
    profiles.appendChild(name)
    root.appendChild(profiles)
    address = doc.createElement('address')
    for g in soup2.findAll("p", {"data-reactid": "8"}):
         tex13 = doc.createTextNode(g.text)
    address.appendChild(tex13)
    profiles.appendChild(address)
    root.appendChild(profiles)
    phno = doc.createElement('phno')
    for g in soup2.findAll("p", {"data-reactid": "8"}):
        xi = g.find("a", {"data-reactid": "15"}).text
        tex15 = doc.createTextNode(xi)
    phno.appendChild(tex15)
    profiles.appendChild(phno)
    root.appendChild(profiles)
    website = doc.createElement('website')
    for g in soup2.findAll("p", {"data-reactid": "8"}):
        xi = g.find("a", {"data-reactid": "17"}).text
        tex15 = doc.createTextNode(xi)
    website.appendChild(tex15)
    profiles.appendChild(website)
    root.appendChild(profiles)
    sector = doc.createElement('sector')
    for g in soup2.findAll("strong", {"data-reactid": "21"}):
        tex15 = doc.createTextNode(g.text)
    sector.appendChild(tex15)
    profiles.appendChild(sector)
    root.appendChild(profiles)
    industry = doc.createElement('industry')
    for g in soup2.findAll("strong", {"data-reactid": "25"}):
        tex15 = doc.createTextNode(g.text)
    industry.appendChild(tex15)
    profiles.appendChild(industry)
    root.appendChild(profiles)
    fulltime = doc.createElement('fulltime')
    for g in soup2.findAll("span", {"data-reactid": "30"}):
        tex15 = doc.createTextNode(g.text)
    fulltime.appendChild(tex15)
    profiles.appendChild(fulltime)
    root.appendChild(profiles)
    business = doc.createElement('business')
    for g in soup2.findAll("p", {"data-reactid": "101"}):
        tex16 = doc.createTextNode(g.text)
    for g in soup2.findAll("p", {"data-reactid": "98"}):
        tex16 = doc.createTextNode(g.text)
    for g in soup2.findAll("p", {"data-reactid": "102"}):
        tex16 = doc.createTextNode(g.text)
    for g in soup2.findAll("p", {"data-reactid": "99"}):
        tex16 = doc.createTextNode(g.text)
    for g in soup2.findAll("p", {"data-reactid": "100"}):
        tex16 = doc.createTextNode(g.text)
    for g in soup2.findAll("p", {"data-reactid": "103"}):
        tex16 = doc.createTextNode(g.text)
    business.appendChild(tex16)
    profiles.appendChild(business)
    root.appendChild(profiles)
    k=k+1
    xml_str = doc.toprettyxml(indent="  ")
    with open(r'C:\Users\MTS\PycharmProjects\projectStock\%s\%s.xml' %(i.strip(),i.strip()), "w") as f:
       f.write(xml_str)