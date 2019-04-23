#!C:/Users/MTS/AppData/Local/Programs/Python/Python36-32/python.exe
import cgi,cgitb
r=cgi.FieldStorage()
d=r.getvalue('total')
print("Content-type:text/html\r\n\r\n")
print("""<html><head><title>Calculator</title>
<body style="background-color: #AAAAFF;">
<form method="post" action="calc.py"><center>
<input type="hidden" name="toshow" value=""
>""")
print("""<h2>Calculator</h2>
<br>""")
print("""<input type="text" width="8" name="second" value=%s align="right">""" % (d))
print("""<br>
<p>
<input type="SUBMIT" name="operation" value="="></p>""")
print ("""</center></form></body></html>""")

