#!C:\Users\MTS\PycharmProjects\projectStock\venv\Scripts\python.exe
import cgi,cgitb
import mysql.connector
x=cgi.FieldStorage()
cgitb.enable()
value=x.getvalue('field')
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
def stopword(value):
    file=open('stopwords.txt','r')
    list1=[]
    flag = 0
    for i in file:
        list1.append(i.strip())
    list2 = str(value).split(" ")
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
    attribute=[]
    table=[]
    avg=""
    key=[]
    for i in file:
        list1.append(i.strip())
    list3 = []
    for i in file1:
        list3.append(i.strip())
    for i in list4:
        #    print(i)
        if(i=='min'or i=='minimum'):
            avg="min"
        if (i == 'max' or i == 'maximum'):
            avg = "max"
        if (i == 'avg' or i == 'average'):
            avg = "max"
        if(list1.__contains__(i.lower())):

            table.append('statistics')
            attribute.append(i)
        if(list3.__contains__(i)):
            key.append(i)
    file = open('financials.txt', 'r')
    file1 = open('ti.txt', 'r')
    list1 = []
    for i in file:
        list1.append(i.strip())
    list3 = []

    for i in file1:
        list3.append(i.strip())
    for i in list4:
        if (i == 'min' or i == 'minimum'):
            avg = "min"
        if (i == 'max' or i == 'maximum'):
            avg = "max"
        if (i == 'avg' or i == 'average'):
            avg = "max"
        if (list1.__contains__(i.lower())):
            table.append('financials')
            attribute.append(i)
        if (list3.__contains__(i)):
            key.append(i)
    file = open('profiles.txt', 'r')
    file1 = open('ti.txt', 'r')
    list1 = []
    for i in file:
        list1.append(i.strip())
    list3 = []
    for i in file1:
        list3.append(i.strip())
    for i in list4:
        if (i == 'min' or i == 'minimum'):
            avg = "min"
        if (i == 'max' or i == 'maximum'):
            avg = "max"
        if (i == 'avg' or i == 'average'):
            avg = "max"
        if (list1.__contains__(i.lower())):
            table.append("profiles")
            attribute.append(i)
        if (list3.__contains__(i)):
            key.append(i)
    return table,attribute,key,avg

list4=stopword(value)
x=attribute(list4)
#print("<b>%s %s</b>" %(x[0],x[2]))
conn=mysql.connector.connect(host="127.0.0.1",port="4444",user="root",password="root",database="mohan")
cursor1=conn.cursor()
if(x[3]=='min' or x[3]=='max' or x[3]=='avg'):
 try:
    sql = "select %s(%s)  from %s" % (x[3],x[1][0], x[0][0])
    cursor1.execute(sql)
    value1 = cursor1.fetchone()
    v = ""
    for i in value1:
        v = i;
        break;
    print("<b>%s</b>" % (v))
    print("<br>")
 except:
     print("<b>Invalid Query</b>")
if(x[0].__len__()>=1 and x[2]!=""):
    for i in range(len(x[0])):
        try:
            sql = "select %s  from %s where TickerName='%s'" % (x[1][i], x[0][i], x[2][i])
            cursor1.execute(sql)
            value1 = cursor1.fetchone()
            v = ""
            for i in value1:
                v = i;
                break;
            print("<b>%s</b>" % (v))
            print("<br>")
        except:
            print("<b>Invalid Query</b>")
print("</form>")
print("</body>")
print("</html>")
