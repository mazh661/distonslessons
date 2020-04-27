  
from main import save_csv_to_json,get_max_salary

csv_file = "table.csv"
json_file = "table.json"

save_csv_to_json(csv_file,json_file)
get_max_salary(json_file)

