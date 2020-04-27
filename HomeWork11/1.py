from main import save_csv_to_json,get_data_from_json,save_data_to_json
csv_file="table.csv"
json_file  = "table.json"
save_csv_to_json(csv_file,json_file)
data=get_data_from_json(json_file)

# print(data)

# new_data ={
#     "employee_id":"10"
# }

# save_data_to_json(json_file,new_data)