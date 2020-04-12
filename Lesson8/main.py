  
#Yerassyl +7086394516
#Anel +707043435435
#China 1232132121314

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
start=input("Name:")
for i in contacts:
    if i["name"]==start:
        print(i["phone"],i["address"],i["email"])