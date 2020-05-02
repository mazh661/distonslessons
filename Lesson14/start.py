import psycopg2

def get_connection(db):
    connection = psycopg2.connect(
        user="postgres",
        password="ayan20()$molda",
        host="127.0.0.1",
        port="5432",
        database=db
    )
    return connection

def get_new_id_for_backup():
    id =0
    connection = get_connection("phone_app")
    curs = connection.cursor()
    sql = "select * from backup"
    curs.execute(sql)
    data = curs.fetchall()
    n = len(data)
    if n !=0:
        last_element = data[n-1]
        return last_element[0]+1

    else:
        return 1

def backup(name_query):
    id = get_new_id_for_backup()
    
    connection = get_connection("phone_app")
    curs = connection.cursor()
    sql = "insert into backup values ('{}','{}')".format(id,name_query)
    curs.execute(sql)
    connection.commit()

def find_by_phone():
    phone = input("Введите номер:")
    connection = get_connection("phone_app")
    curs = connection.cursor()
    sql = "select * from users where phone='{}'".format(phone)
    curs.execute(sql)
    data = curs.fetchall()
    for i in data:
        print(i)
    backup("search by phone")
    main()

def find_by_name():
    name = input("Введите имя:")
    connection = get_connection("phone_app")
    curs = connection.cursor()
    sql = "select * from users where name='{}'".format(name)
    curs.execute(sql)
    data = curs.fetchall()
    for i in data:
        print(i)
    backup("search by name")
    main()
def get_new_id():
    id =0
    connection = get_connection("phone_app")
    curs = connection.cursor()
    sql = "select * from users"
    curs.execute(sql)
    data = curs.fetchall()
    n = len(data)
    last_element = data[n-1]
    return last_element[0]+1

def add_contact():
    name = input("Введите имя:")
    phone = input("Введите номер:")
    id = get_new_id()
    connection = get_connection("phone_app")
    curs = connection.cursor()
    sql = "insert into users values ('{}','{}','{}')".format(id,name,phone)
    curs.execute(sql)
    connection.commit()
    backup("add contact")
    main()




def main():
    print("[1]Найти по телефону")
    print("[2]Найти по имени")
    print("[3]Добавить новый контакт")
    print("[4]Выйти")
    num = int(input())
    if num == 1:
        find_by_phone()
    elif num == 2:
        find_by_name()
    elif num == 3:
        add_contact()
    else:
        backup("exit")
        exit()

main()