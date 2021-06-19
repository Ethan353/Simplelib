import sqlite3
from libraryclass import Library

connection = sqlite3.connect('Libdb.db')
cu = connection.cursor()


def insert(lib: Library):
    with connection:
        cu.execute("INSERT INTO Library VALUES (:accessinno, :isbn, :userid)",
                   {
                       "accessinno": lib.accessinno,
                       "isbn": lib.lib_isbn,
                       "userid": lib.lib_userid
                   })


def update_user(accessinno, userid):
    with connection:
        cu.execute("UPDATE Library SET lib_userid = :userid WHERE accessinno = :accessinno",
                   {"accessinno": accessinno, "userid": userid})


def select_all():
    cu.execute('''SELECT accessinno, Student.name, lib_userid, Book.*
                  FROM Library JOIN Book on lib_isbn = isbn JOIN Student on userid = lib_userid''')

    return cu.fetchall()


def select_accessinno(accessinno):
    cu.execute('''SELECT accessinno, Student.name, lib_userid, Book.*
                  FROM Library JOIN Book on lib_isbn = isbn JOIN Student on userid = lib_userid
                  WHERE accessinno = :accessinno''', {"accessinno": accessinno})

    return cu.fetchall()


def select_isbn(isbn):
    cu.execute('''SELECT accessinno,Student.name, lib_userid, Book.*
                  FROM Library JOIN Book on lib_isbn = isbn JOIN Student on userid = lib_userid
                  WHERE isbn = :isbn''', {"isbn": isbn})

    return cu.fetchall()


def select_userid(userid):
    cu.execute('''SELECT accessinno, Student.name, lib_userid, Book.*
                  FROM Library JOIN Book on lib_isbn = isbn JOIN Student on userid = lib_userid
                  WHERE userid = :userid''', {"userid": userid})

    return cu.fetchall()


li = Library(24, 65844, "9766")
# insert(li)
# print(select_all())