from main import add_object,get_data_from_json,save_data_to_json,delete_object
def add_employee():
    d={}
    d["EMPLOYEE_ID"]=int(input("EMPLOYEE_ID: "))
    d["FIRST_NAME"]=input("FIRST_NAME: ")
    add_object("table.json",d)
add_employee()

