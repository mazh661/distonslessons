import psycopg2
connection = psycopg2.connect(
    user="postgres",
    password="ayan20()$molda",
    host="127.0.0.1",
    port="5432",
    database="phone_app"
)

cursor = connection.cursor()
name=input("Введите имя: ")
sql = "select * from users where name='{}'".format(name)
cursor.execute(sql)
data = cursor.fetchall()
for i in data:
    print(i[2])