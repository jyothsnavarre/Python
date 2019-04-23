import mysql.connector
def stopword(value):
    file=open('stopwords.txt','r')
    list1=[]
    flag = 0
    for i in file:
        list1.append(i.strip())
    list2 = str(value).split(" ")
    print(list2)
    list3=[]
    for j in list2:
        flag = 0
        if (list1.__contains__(j)):
            flag = 1
        if (flag == 0):
            list3.append(j)
    return list3
def  attribute(list4):
    file=open('statistics.txt','r')
    file1=open('ti.txt','r')
    list1=[]
    for i in file:
        list1.append(i.strip())
    list3 = []
    for i in file1:
        list3.append(i.strip())
    for i in list4:
        if(list1.__contains__(i)):
            table="statistics"
            attribute=i
        if(list3.__contains__(i)):
            key=i
    return table,attribute,key

value="what is marketcap of ANDV"
list4=stopword(value)
print(list4)
x=attribute(list4)
conn=mysql.connector.connect(host="127.0.0.1",port="4444",user="root",password="root",database="mohan")
cursor1=conn.cursor()
sql="select %s from %s where TickerName='%s'"%(x[1],x[0],x[2])
cursor1.execute(sql)
value1=cursor1.fetchone()
for i in value1:
    v=i;
    break;
print(v)

