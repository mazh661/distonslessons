import json

user1 = {
    "name":"Yerassyl",
    "phone":"7086394516",
    "address":"makataeva117",
    "email":"tleugazy98@gmail.com"
}
user2={
    "name":"Anel",
    "phone":"707043435435",
    "address":"makataeva117",
    "email":"tleugazy98@gmail.com"
}
contacts=[user1,user2]
with open("contacts.json","w") as filewrite:
    json.dump(contacts,filewrite,indent=4)