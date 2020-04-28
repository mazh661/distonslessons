import json
def write_to_json(json_file,objects):
    file = open(json_file,"w+")
    json_objects = json.dumps(objects,indent=4)
    file.write(json_objects)
def get_from_json(json_file):
    file = open(json_file,"r+")
    data_from_file = file.read()
    objects = json.loads(data_from_file)
    return objects
def show_persons():
    print("--Show persons Menu--")
    for i in persons:
        st="FirstName:{},Age:{}".format(i['first_name'],i['age'])
        print(st)
    main()
def add_person():
    print("---Add Person Menu---")
    first_name = input("Write first name:")
    last_name = input("Write last name:")
    age = int(input("Write age:"))
    person={
        "first_name":first_name,
        "last_name":last_name,
        "age":age
    }
    persons.append(person)
    write_to_json("persons.json",persons)
    main()
def delete_person():
    print("---Delete Menu---")
    for i in persons:
        st="FirstName:{},Age:{}".format(i['first_name'],i['age'])
        print(st)
    n = int(input())-1
    persons.pop(n)
    main()

def check():
    initial_data=[
            {
            "first_name":"yerasyl",
            "last_name":"tleugazy",
            "age":22,
            },
            {
            "first_name":"kirito",
            "last_name":"shsjsk",
            "age":20,    
            }
    ]
    write_to_json("persons.json",initial_data)

def main():
    if len(persons)==0:
        check()
        exit()
    print("Welcome to main menu")
    print("[1]Show Persons")
    print("[2]Add Person")
    print("[3]Delete Person")
    num = int(input())
    if num == 1:
        show_persons()
    elif num == 2:
        add_person()
    elif num == 3:
        delete_person()
    else:
        exit()
persons=get_from_json("persons.json")
main()