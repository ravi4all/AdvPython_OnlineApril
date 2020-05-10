import json
import urllib.request as url
import cgi

form = cgi.FieldStorage()

player_name = form.getvalue('name')
# player_name = player_name[0].replace(' ', '')
print(player_name)
req = url.urlopen('https://cricapi.com/api/playerFinder?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&name={}'.format(player_name))
data = json.load(req)
pid = data['data'][0]['pid']

req = url.urlopen('https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid={}'.format(pid))
data = json.load(req)
name = data['fullName']
bat_style = data['battingStyle']
bowl_style = data['bowlingStyle']
profile = data['profile']
age = data['currentAge']
role = data['playingRole']
img = data['imageURL']
tests = data['data']['batting']['tests']
tests_keys = tests.keys()
tests_values = tests.values()

odi = data['data']['batting']['ODIs']
odi_keys = odi.keys()
odi_values = odi.values()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

    <h2>Data for {}</h2>
    <p><b>Profile : </b>{}</p>
    <img src ="{}" alt="{}"/>
""".format(name, profile, img, name))

print("""
<table width="100%" border=2 cellpadding=10>
    <tr>
        <th>Name</th>
        <th>Batting Style</th>
        <th>Bowling Style</th>
        <th>Current Age</th>
        <th>Role</th>
    </tr>
    <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
    </tr>
</table>
<hr>
""".format(name, bat_style, bowl_style, age, role))

# print(odi,odi_keys,odi_values)
print("<h2>ODI Data</h2>")
print('<table width="100%" border=2 cellpadding=10> <tr>')

for i in range(len(odi_keys)):
    print("<th>{}</th>".format(list(odi_keys)[i]))

print("</tr><tr>")

for i in range(len(odi_keys)):
    print("<td>{}</td>".format(list(odi_values)[i]))

print("</tr> </table>")

print("<h2>Test Data</h2>")
print('<table width="100%" border=2 cellpadding=10> <tr>')

for i in range(len(tests_keys)):
    print("<th>{}</th>".format(list(tests_keys)[i]))

print("</tr><tr>")

for i in range(len(tests_keys)):
    print("<td>{}</td>".format(list(tests_values)[i]))

print("</tr> </table>")

print("""
</body>
</html>
""".format(name, profile))