from xml.dom.minidom import parse
import xml.dom.minidom
import mysql.connector
f=open('ti.txt','r')
for i in f:
     DOMTree = xml.dom.minidom.parse(r"C:\Users\MTS\PycharmProjects\projectStock\%s\%s.xml" % (i.strip(),i.strip()))
     collection = DOMTree.documentElement
     statistic = collection.getElementsByTagName('statistics')
     for to in statistic:
          ki=to.getElementsByTagName('srno')
          for gh in ki:
               sr=gh.childNodes[0].nodeValue
          sttick=to.getElementsByTagName('stat_tik')
          for a in sttick:
               stattick=a.childNodes[0].nodeValue
          marketc = to.getElementsByTagName('marketcap')
          for m in marketc:
               marketcap = m.childNodes[0].nodeValue
          Enter = to.getElementsByTagName('Enterprisevalue')
          for e in Enter:
               enterprise = e.childNodes[0].nodeValue
          Ret = to.getElementsByTagName('RetOnAss')
          for r in Ret:
               Return = r.childNodes[0].nodeValue
          Tot = to.getElementsByTagName('TotCash')
          for t in Tot:
               Total = t.childNodes[0].nodeValue
          promar= to.getElementsByTagName('proMar')
          for p in promar:
               promarg = p.childNodes[0].nodeValue
          grpro = to.getElementsByTagName('grossPro')
          for g in grpro:
               gross = g.childNodes[0].nodeValue
          ocash = to.getElementsByTagName('ooCash')
          for o in ocash:
               Ocash = o.childNodes[0].nodeValue
          todebt = to.getElementsByTagName('totdebt')
          for tl in todebt:
               debt = tl.childNodes[0].nodeValue
          curr = to.getElementsByTagName('currat')
          for c in curr:
               current = c.childNodes[0].nodeValue
          lever = to.getElementsByTagName('lever')
          for l in lever:
               levered = l.childNodes[0].nodeValue
          conn=mysql.connector.connect(host="127.0.0.1",port="4444",user="root",password="root",database="mohan")
          cursor1=conn.cursor()
          sql = """insert into statistics(Srno,TickerName,Marketcap,Enter_Value,Ret_Assets,Total_cash,Oper_cash_flow,Levered_free_cash_flow,TotalDebt,Curre_Ratio,Gross_Profit,profit_margin) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
          values = (str(sr),str(stattick),str(marketcap),str(enterprise),str(Return),str(Total),str(Ocash),str(levered),str(debt),str(current),str(gross),str(promarg))
          try:
           cursor1.execute(sql, values)
           conn.commit()
          except:
               financials = collection.getElementsByTagName('financials')
               for to in financials:
                    fintick = to.getElementsByTagName('fintick')
                    for a in fintick:
                         finntick = a.childNodes[0].nodeValue
                    TotRev = to.getElementsByTagName('TotRev')
                    for a in TotRev:
                         totrev = a.childNodes[0].nodeValue
                    costRev = to.getElementsByTagName('costRev')
                    for a in costRev:
                         Costrev = a.childNodes[0].nodeValue
                    incBTax = to.getElementsByTagName('incBefTax')
                    for a in incBTax:
                         incB = a.childNodes[0].nodeValue
                    Net = to.getElementsByTagName('Netinc')
                    for a in Net:
                         NetInc = a.childNodes[0].nodeValue
                    sql = """insert into financials(Fin_ticker,Total_revenue,Cost_revenue,Income_Before_Tax,NetIncome) values(%s,%s,%s,%s,%s)"""
                    values = (str(finntick),str(totrev),str(Costrev),str(incB),str(NetInc))
                    try:
                       cursor1.execute(sql, values)
                       conn.commit()
                    except:
                         profiles = collection.getElementsByTagName('profiles')
                         for to in profiles:
                              protick = to.getElementsByTagName('protick')
                              for a in protick:
                                   prtick = a.childNodes[0].nodeValue
                              name = to.getElementsByTagName('name')
                              for a in name:
                                   Name = a.childNodes[0].nodeValue
                              adress = to.getElementsByTagName('address')
                              for a in adress:
                                   adr = a.childNodes[0].nodeValue
                              phno = to.getElementsByTagName('phno')
                              for a in phno:
                                   ph = a.childNodes[0].nodeValue
                              web = to.getElementsByTagName('website')
                              for a in web:
                                   website = a.childNodes[0].nodeValue
                              sec = to.getElementsByTagName('sector')
                              for a in sec:
                                   sector = a.childNodes[0].nodeValue
                              industry = to.getElementsByTagName('industry')
                              for a in industry:
                                   indus = a.childNodes[0].nodeValue
                              full = to.getElementsByTagName('fulltime')
                              for a in full:
                                   fulltime = a.childNodes[0].nodeValue
                              bussum = to.getElementsByTagName('business')
                              for a in bussum:
                                   summary = a.childNodes[0].nodeValue
                              sql = """insert into profiles(prof_ticker,Name,Address,phonenum,website,sector,industry,Fulltime,summary) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                              values = (str(prtick),str(Name),str(adr),str(ph),str(website),str(sector),str(indus),str(fulltime),str(summary))
                              try:
                                cursor1.execute(sql, values)
                                conn.commit()
                              except:
                                   pass










