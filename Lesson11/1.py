from main import add_object,get_data_from_json,save_data_to_json
def add_employee():
    d={}
    d["EMPLOYEE_ID"]=int(input("Employee_id:"))
    d["FIRST_NAME"]=input("FirstName:")
    add_object("table.json",d)
#code for deleting
data = get_data_from_json("table.json")
employee_id=9
employee_index=0
for i in range(len(data)):
    employee = data[i]
    if employee["EMPLOYEE_ID"]==employee_id:
        employee_index=i
data.pop(employee_index)
save_data_to_json("table.json",data)