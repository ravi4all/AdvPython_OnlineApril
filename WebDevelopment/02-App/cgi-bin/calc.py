import cgi

form = cgi.FieldStorage()

a = int(form.getvalue('f_num'))
b = int(form.getvalue('s_num'))

c = a + b

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

    <h1>Hello World using Python Programming</h1>
    <h2>Sum of {} and {} is {}</h2>

</body>
</html>
""".format(a,b,c))