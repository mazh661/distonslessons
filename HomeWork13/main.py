import psycopg2
connection = psycopg2.connect(
    user="postgres",
    password="ayan20()$molda",
    host="127.0.0.1",
    port="5432",
    database="Lesson13DB"
)

cursor = connection.cursor()
sql = "select * from products"
cursor.execute(sql)
data = cursor.fetchall()

max_price=data[0][2]
index=0
for i in data:
    if max_price<i[2]:
        max_price=i[2]
    
print(max_price)

