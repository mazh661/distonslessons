import psycopg2
connection = psycopg2.connect(
    user="postgres",
    password="ayan20()$molda",
    host="127.0.0.1",
    port="5432",
    database="Lesson13DB"
)

cursor = connection.cursor()
sql = "select * from users"
cursor.execute(sql)
data = cursor.fetchall()
# print(data)

for i in data:
    print(i[0])