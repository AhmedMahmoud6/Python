import json
data = '''[
{ "id" : "002",
  "x" : "69",
  "name" : "UwU"
},

{ "id" : "003",
  "x" : "96",
  "name" : "Oni Chan"

}


]'''
info = json.loads(data)
print(len(info))
for i in info:
    print('The Name is', i["name"])
    print('The id is', i["id"])
    print('Attribite is', i["x"])
