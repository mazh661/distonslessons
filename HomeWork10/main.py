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
    
def get_max_salary(json_file):
    with open(json_file,"r") as json_file:
        arr = json.load(json_file) 
    max_salary = arr[0]["SALARY"]
    for i in range(len(arr)):
        if max_salary<arr[i]["SALARY"]:
            max_salary=arr[i]["SALARY"]
    print(max_salary) 