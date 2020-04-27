import csv
import json
def save_csv_to_json(csv_file,json_file):
    arr=[]
    #read from csv and convert to [{},{},{}]
    with open(csv_file) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for i in csvReader:
            arr.append(i)
    #transform from str to int
    for i in range(len(arr)):
        d = arr[i]
        d["EMPLOYEE_ID"]=int(d["EMPLOYEE_ID"])
        if d["DEPARTMENT_ID"] !=" - ":
            d["DEPARTMENT_ID"]=int(d["DEPARTMENT_ID"])
        d["SALARY"]=int(d['SALARY'])
    #write data to json file  
    with open(json_file,"w") as jsonFile:
        json_arr= json.dumps(arr,indent=4)
        jsonFile.write(json_arr)

def get_data_from_json(json_file):
    arr=[]
    with open(json_file,"r") as jsonFile:
        data = jsonFile.read()
        arr = json.loads(data)
    return arr

def save_data_to_json(json_file,data):
    with open(json_file,"w") as jsonFile:
        json_arr= json.dumps(data,indent=4)
        jsonFile.write(json_arr)

def add_object(json_file,object_example):
    data = get_data_from_json(json_file)
    data.append(object_example)
def delete_object():
    pass