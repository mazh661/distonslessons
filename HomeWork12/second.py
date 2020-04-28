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
#main