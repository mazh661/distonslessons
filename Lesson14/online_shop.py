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

def get_all_users():
    users = []
    connection = get_connection("online_shop")
    curs = connection.cursor()
    sql = "select * from users"
    curs.execute(sql)
    data = curs.fetchall()
    for i in data:
        d ={
            "id": i[0],
            "username": i[1],
            "password": i[2]
        }
        users.append(d)
    return users

def get_all_products():  
    products = []
    connection = get_connection("online_shop")
    curs = connection.cursor()
    sql = "select * from products"
    curs.execute(sql)
    data = curs.fetchall()
    for i in data:
        d ={
            "id": i[0],
            "name": i[1],
            "price": i[2]
        }
        products.append(d)
    return products

def get_all_orders():  
    orders = []
    connection = get_connection("online_shop")
    curs = connection.cursor()
    sql = "select * from orders"
    curs.execute(sql)
    data = curs.fetchall()
    for i in data:
        d ={
            "id": i[0],
            "id_user": i[1],
            "id_product": i[2]
        }
        orders.append(d)
    return orders


users = get_all_users()
products = get_all_products()
orders = get_all_orders()

print(users)
print(products)
print(orders)

order_info=[]
for order in orders:
    d ={}
    d['id_order'] = order['id']
    for user in users:
        if order['id_user'] == user['id']:
            d['user'] = user['username']
            break
    for product in products:
        if order['id_product'] == product['id']:
            d['product']=product['name']
            break
    order_info.append(d)
print(order_info)

    
   