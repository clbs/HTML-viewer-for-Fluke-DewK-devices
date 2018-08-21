import re
import json

with open("RHT.INI", "r") as f:
   data = f.read()

pattern = '(\n?\[[AB][0-9AB]{1,9}[\-]?[0-9AB]{1}\]\n?)'
result = re.split(pattern, data)
result = [x.strip() for x in result]
d = {}
for item in result:
   if not item:
       continue
   if re.match(pattern, item):
       active_key = item.strip("[").strip("]")
       d[active_key] = {}
   else:
       # we has values that should go in the previous key
       bits = item.split("\n")
       for bit in bits:
           k, v = bit.split("=")
           d[active_key][k] = v
f.close()           
start = """
<html>
<table style="width: 400px; height: 400px; margin-left: auto; margin-right: auto;" border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr style="height: 20px;">
<td style="width: 180px; height: 20px;" align="center" valign="center"><b>Location</b></td>
<td style="width: 180px; height: 20px;" align="center" valign="center"><b>Temperature</b></td>
<td style="width: 180px; height: 20px;" align="center" valign="center"><b>Humidity</b></td>
<td style="width: 180px; height: 20px;" align="center" valign="center"><b>Time</b></td>
</tr>
"""

td0 = """<tr style="height: 35px;"><td style="width: 180px; height: 35px;" align="center" valign="center">""" + "MetCal 1" + "</td>"
td1 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + d['A42394']['Temperature'] + "</td>"
td2 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + d['A42394']['Humidity'] + " %" + "</td>"
td3 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + "time" + ("</td></tr>")

td4 = """<tr style="height: 35px;"><td style="width: 180px; height: 35px;" align="center" valign="center">""" + "MetCal 2" + "</td>"
td5 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + d['B94832']['Temperature'] + "</td>"
td6 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + d['B94832']['Humidity'] + " %" + "</td>"
td7 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + "time" + ("</td></tr>")

td8 = """<tr style="height: 35px;"><td style="width: 180px; height: 35px;" align="center" valign="center">""" + "MetCal 3" + "</td>"
td9 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + d['B94832']['Temperature'] + ("</td>")
td10 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + d['B94832']['Humidity'] + " %" + ("</td>")
td11 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + "time" + ("</td></tr>")

td12 = """<tr style="height: 35px;"><td style="width: 180px; height: 35px;" align="center" valign="center">""" + "MetCal 4" + "</td>"
td13 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + d['B20034']['Temperature'] + "</td>"
td14 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + d['B20034']['Humidity'] + " %" + "</td>"
td15 = """<td style="width: 180px; height: 35px;" align="center" valign="center">""" + "time" + "</td></tr>"

finish = """
</tbody>
</table>
</html>
"""

full = start + td0 + td1 + td2 + td3 + td4 + td5 + td6 + td7 + td8 + td9 + td10 + td11 + td12 + td13 + td14 + td15 + finish
x= open("test.html","w+")
x.write(full)
x.close()
exit
