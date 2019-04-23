#!C:/Users/MTS/AppData/Local/Programs/Python/Python36-32/python.exe
import cgi,cgitb
r=cgi.FieldStorage()
z=r.getvalue('second')
print("Content-type:text/html\r\n\r\n")
print("""<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>calc.py</title>
</head>
<body>
  <form action="calculator.py" method="post">""")
print("""Total: <input type="text" name="total" value=%s>""" % (eval(z)))
print("""<br />""")


print("""<input type="submit" value="submit"/>""")
print("""</form>
</body>
</html>""")