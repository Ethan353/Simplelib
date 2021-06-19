import sqlite3
from studentclass import Student

connection = sqlite3.connect('Libdb.db')
cu = connection.cursor()


def insert(student: Student):
    with connection:
        cu.execute("INSERT INTO Student VALUES (:userid, :name, :password, :deptname)",
                   {'userid': student.userid,
                    'name': student.name,
                    'password': student.password,
                    'deptname': student.deptname})


def delete(userid: str):
    with connection:
        cu.execute("DELETE from Student WHERE userid = :userid", {"userid": userid})


def update(userid, password):
    with connection:
        cu.execute("UPDATE Student SET password = :password WHERE userid = :userid", {"userid": userid,
                                                                                      "password": password})


def select_all():
    cu.execute('''SELECT userid, name, deptname
                  FROM Student''')

    return cu.fetchall()


def select_name(name):
    cu.execute('''SELECT userid, name, deptname
                  FROM Student
                  WHERE name = :name''', {"name": name})

    return cu.fetchall()


def select_id(userid):
    cu.execute('''SELECT userid, name, deptname
                  FROM Student
                  WHERE userid = :userid''', {"userid": userid})

    return cu.fetchall()


def select_dept(deptname):
    cu.execute('''SELECT userid, name, deptname
                  FROM Student
                  WHERE deptname = :deptname''', {"deptname": deptname})

    return cu.fetchall()


def select_name_dept(name, deptname):
    cu.execute('''SELECT userid, name, deptname
                  FROM Student
                  WHERE deptname = :deptname AND name = :name''', {"deptname": deptname, "name": name})

    return cu.fetchall()


stu = Student("973613", "Ehsan", "Math", "1234")


# delete("973613")

# update("973613", "25")

# print(select_name("Ehsan"))
# print(select_id("973613"))
# print(select_dept("Math"))
# print(select_name_dept("Ehsan", "Math"))
# print(select_all())