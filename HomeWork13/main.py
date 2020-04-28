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

for i in data:
    print(i)

index=0
max_price=data[0][2]
for i in data:
    if max_price<i[2]:
        max_price=i[2]
        index=i
    
print(max_price, index)

