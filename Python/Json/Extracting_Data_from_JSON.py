import urllib.request, urllib.parse, urllib.error
import json
sum = 0
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = input('Enter URL: ')


print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read().decode()
print('Retrieved', len(data), 'Characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'comments' not in js :
    print('==== Faliure To Retrieve the data')
    print(data)
    quit()

print(json.dumps(js, indent=4))

for i in js["comments"]:
    sum = sum + i["count"]
print(sum)
