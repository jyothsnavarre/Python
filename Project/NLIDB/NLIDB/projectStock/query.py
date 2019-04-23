#!C:\Users\MTS\PycharmProjects\projectStock\venv\Scripts\python.exe
import cgi,cgitb
x=cgi.FieldStorage()
value=x.getvalue('field')
print(value)
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<b>%s</b>" %(value))

print("</form>")
print("</body>")
print("</html>")