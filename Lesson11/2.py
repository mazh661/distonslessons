import json
d={}
d["EMPLOYEE_ID"]=int(input("EMPLOYEE_ID:"))
d["FIRST_NAME"]=input("FIRST_NAME")
d["LAST_NAME"]=input("LAST_NAME")
d["EMAIL"]=input("EMAIL")
d["PHONE_NUMBER"]=input("PHONE_NUMBER")
d["HIRE_DATE"]=input("HIRE_DATE")
d["JOB_ID"]=input("JOB_ID")
d["SALARY"]=int(input("SALARY"))
d["COMMISSION_PCT"]=input("COMMISSION_PCT")
d["MANAGER_ID"]=int(input("MANAGER_ID"))
d["DEPARTMENT_ID"]=int(input("DEPARTMENT_ID"))

arr=[]
with open("table.json","r") as jsonFile:
    data = jsonFile.read()
    arr = json.loads(data)

arr.append(d)


with open("table.json","w") as jsonFile:
    json_arr= json.dumps(arr,indent=4)
    jsonFile.write(json_arr)