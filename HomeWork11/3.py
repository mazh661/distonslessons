from main import get_data_from_json,save_data_to_json
data = get_data_from_json("table.json")
employee_id="Ayan"
employee_key="FIRST_NAME"
employee_index=[]
for i in range(len(data)):
    employee = data[i]
    if employee[employee_key]==employee_id:
        employee_index.append(i)
        

for i in employee_index:
    print(i)
    
# data.pop(employee_index)
save_data_to_json("table.json",data)