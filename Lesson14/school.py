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

def get_all_students():
    students = []
    connection = get_connection("shool")
    curs = connection.cursor()
    sql = "select * from student"
    curs.execute(sql)
    data = curs.fetchall()
    for i in data:
        d ={
            "id": i[0],
            "id_grade": i[1],
            "first_name": i[2],
            "last_name": i[3]
        }
        students.append(d)
    return students
def get_all_grades():
    grades = []
    connection = get_connection("shool")
    curs = connection.cursor()
    sql = "select * from grade"
    curs.execute(sql)
    data = curs.fetchall()
    for i in data:
        d ={
            "id": i[0],
            "name": i[1],
        }
        grades.append(d)
    return grades

students = get_all_students()
grades = get_all_grades()

student_info = []
for student in students:
    d ={}
    d['id_student'] = student['id']
    for grade in grades:
        if student["id_grade"] == grade['id']:
            d['first_name']=student['first_name']
            d['last_name']=student['last_name']
            d['grade']=grade['name']
            break
    student_info.append(d)
for i in student_info:
    print(i)

grade_info = []
for grade in grades:
    d={}
    d['id_grade'] = grade['id']
    count_of_students=0
    for student in students:
        if grade['id']==student["id_grade"]:
            count_of_students+=1
            d['grade_name']=grade['name']
            d['count_of_students']=count_of_students
    grade_info.append(d)
for i in grade_info:
    print(i)
