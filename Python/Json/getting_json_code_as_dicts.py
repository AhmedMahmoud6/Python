import json

data ='''
{
 "name" : "Ahmed",
    "phone" : {
    "type" : "intl",
    "number" : "+20 106 6832 2147"
              },

     "email" : {
     "hide" : "yes"
               }

}'''

info = json.loads(data)
print('The Name is', info["name"])
print('Hide', info["email"]["hide"])
print('Phone number:', info["phone"]["number"])
