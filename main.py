import re
from os import system, name
import os
from subprocess import call
import libraryorm
import studentorm
import bookorm


def clear():
    print('\n'*30)


while True:
    command = input("what you want to do?(you can type these command whenever you need\n"
                    "exit \n"
                    "STUDENT: ------------------------------------------------- \n"
                    "list students \n"
                    "find student by name \n"
                    "find student by id \n"
                    "find student by department \n"
                    "find student by name and department \n"
                    "insert new student \n"
                    "delete student by id \n"
                    "update student password by student id\n"
                    "BOOK: --------------------------------------------------- \n"
                    "list books \n"
                    "find book by title \n"
                    "find book by isbn \n"
                    "find book by author \n"
                    "find book by publisher \n"
                    "find book publisher and author \n"
                    "find book publisher and title \n"
                    "find book author and title \n"
                    "insert new book \n"
                    "delete book by isbn \n"
                    "update book title by its isbn \n"
                    "update book author by its isbn \n"
                    "update book publisher by its isbn \n"
                    "Libray manger : ----------------------------------------- \n"
                    "list books inside the library \n"
                    "insert a book to library \n"
                    "barrow a book from library \n"
                    "give back a book to library \n"
                    "find in lib by student id \n"
                    "find in lib by isbn \n"
                    "find in lib by accessinno \n"
                    "find who barrowed by student id \n"
                    )
    getting = ["get", "barrow", "take"]
    if re.match('ex', command):
        break

    if re.match("delete book", command):
        clear()
        isbn = int(input("enter the isbn: "))
        bookorm.delete(isbn)
        print("book deleted !!!!!!!")
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("update book author", command):
        clear()
        isbn = int(input("enter the isbn: "))
        author = input("enter the author: ")
        bookorm.update_author(isbn, author)
        print(f"book author changed to {author} !!!!!!!")
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("update book title", command):
        clear()
        isbn = int(input("enter the isbn: "))
        title = input("enter the title: ")
        bookorm.update_title(isbn, title)
        print(f"book title changed to {title} !!!!!!!")
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("update book publisher", command):
        clear()
        isbn = int(input("enter the isbn: "))
        publisher = input("enter the publisher: ")
        bookorm.update_publisher(isbn, publisher)
        print(f"book publisher changed to {publisher} !!!!!!!")
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("insert book", command):
        clear()
        isbn = int(input("enter the isbn: "))
        title = input("enter the title: ")
        author = input("enter the author: ")
        publisher = input("enter the publisher: ")
        book_obj = bookorm.Book(isbn, title, author, publisher)
        bookorm.insert(book_obj)
        print("book added !!!!!!!")
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("insert book to library", command):
        clear()
        isbn = int(input("enter the isbn: "))
        access = input("enter the accessinno: ")
        lib_obj = libraryorm.Library(access, isbn)
        libraryorm.insert(lib_obj)
        print("book added to library!!!!!!!")
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("insert student", command):
        clear()
        userid = int(input("enter the userid: "))
        name = input("enter the name: ")
        deptname = input("enter the deptname: ")
        password = input("enter the password: ")
        stu_obj = studentorm.Student(userid, name, password, deptname)
        studentorm.insert(stu_obj)
        print("student added !!!!!!!")
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("delete student", command):
        clear()
        userid = int(input("enter the userid: "))
        studentorm.delete(userid)
        print("student deleted !!!!!!!")
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("list book", command):
        books = bookorm.select_all()
        clear()
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("find by isbn", command):
        clear()
        isbn = input("enter the isbn:")
        books = bookorm.select_isbn(isbn)
        clear()
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("find by userid", command):
        clear()
        userid = input("enter the userid:")
        students = studentorm.select_id(userid)
        clear()
        for book in students:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("find by name", command):
        clear()
        userid = input("enter the userid:")
        students = studentorm.select_id(userid)
        clear()
        for book in students:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("find by title", command):
        clear()
        title = input("enter the title:")
        books = bookorm.select_title(title)
        clear()
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("find by publisher", command):
        clear()
        publisher = input("enter the publisher:")
        books = bookorm.select_publisher(publisher)
        clear()
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("find by author", command):
        clear()
        author = input("enter the author:")
        books = bookorm.select_author(author)
        clear()
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("find author and title", command):
        clear()
        title, author = input("enter the author then title:").split()
        books = bookorm.select_author_title(author, title)
        clear()
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("find author and publisher", command):
        clear()
        publisher, author = input("enter the publisher then author:").split()
        books = bookorm.select_publisher_author(publisher, author)
        clear()
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("find title and publisher", command):
        clear()
        publisher, title = input("enter the publisher then title:").split()
        books = bookorm.select_publisher_title(publisher, title)
        clear()
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match("give", command):
        clear()
        access = int(input("type access in number: "))
        libraryorm.update_user(access, 'nobody')
        print('change commited')
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match('list lib', command):
        books = libraryorm.select_all()
        clear()
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match('find in lib accessinno', command):
        accessno = int(input("enter access in number: "))
        books = libraryorm.select_accessinno(accessno)
        clear()
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match('find in lib isbn', command):
        isbn = int(input("enter isbn:"))
        clear()
        books = libraryorm.select_isbn(isbn)
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    if re.match('find in lib by student id', command):
        stuid = input('enter student number: ')
        clear()
        books = libraryorm.select_userid(stuid)
        for book in books:
            print(*book)
        back = input("enter back to continue: ")
        if re.match('ba', back):
            continue

    for pattern in getting:
        if re.match(pattern, command):
            clear()
            while True:
                libcommand = input("if u wanna continue or any other in library type it if u wanna back type it: ")
                if re.match('ba', libcommand):
                    break

                if re.match('list', libcommand):
                    libraryorm.select_all()

                if re.match('access', libcommand):
                    accessno = int(input("enter access in number: "))
                    libraryorm.select_accessinno(accessno)

                if re.match('isbn', libcommand):
                    isbn = int(input("enter isbn:"))
                    libraryorm.select_isbn(isbn)

                if re.match('stud', libcommand):
                    stuid = input('enter student number: ')
                    libraryorm.select_userid(stuid)

                access = int(input("type access in number: "))
                student = int(input("type your student num"))
                if libraryorm.select_accessinno(access)[0][1] == 'nobody':
                    libraryorm.update_user(access, student)
                    print('changes commited!')
                else:
                    print("this book is barrowed")
                    continue