import sqlite3
from bookclass import Book

connection = sqlite3.connect('Libdb.db')
cu = connection.cursor()


def insert(book: Book):
    with connection:
        cu.execute("INSERT INTO Book VALUES (:isbn, :title, :author, :publisher)",
                   {
                       'isbn': book.isbn,
                       'title': book.title,
                       'author': book.author,
                       'publisher': book.publisher
                   })


def delete(isbn):
    with connection:
        cu.execute("DELETE from Book WHERE isbn = :isbn", {"isbn": isbn})


def update_title(isbn, title):
    with connection:
        cu.execute("UPDATE Book SET title = :title WHERE isbn = :isbn", {"title": title, "isbn": isbn})


def update_author(isbn, author):
    with connection:
        cu.execute("UPDATE Book SET author = :author WHERE isbn = :isbn", {"author": author, "isbn": isbn})


def update_publisher(isbn, publisher):
    with connection:
        cu.execute("UPDATE Book SET publisher = :publisher WHERE isbn = :isbn", {"publisher": publisher, "isbn": isbn})


def select_all():
    cu.execute('''SELECT isbn, title, author, publisher
                  FROM Book''')

    return cu.fetchall()


def select_isbn(isbn):
    cu.execute('''SELECT isbn, title, author, publisher
                  FROM Book
                  WHERE isbn = :isbn''', {'isbn': isbn})

    return cu.fetchall()


def select_title(title):
    cu.execute('''SELECT isbn, title, author, publisher
                  FROM Book
                  WHERE title = :title''', {'title': title})

    return cu.fetchall()


def select_author(author):
    cu.execute('''SELECT isbn, title, author, publisher
                  FROM Book
                  WHERE author = :author''', {'author': author})

    return cu.fetchall()


def select_publisher(publisher):
    cu.execute('''SELECT isbn, title, author, publisher
                  FROM Book
                  WHERE publisher = :publisher''', {'publisher': publisher})

    return cu.fetchall()


def select_publisher_author(publisher, author):
    cu.execute('''SELECT isbn, title, author, publisher
                  FROM Book
                  WHERE publisher = :publisher AND author = :author''', {'publisher': publisher, 'author': author})

    return cu.fetchall()


def select_publisher_title(publisher, title):
    cu.execute('''SELECT isbn, title, author, publisher
                  FROM Book
                  WHERE publisher = :publisher AND title = :title''', {'publisher': publisher, 'title': title})

    return cu.fetchall()


def select_author_title(author, title):
    cu.execute('''SELECT isbn, title, author, publisher
                  FROM Book
                  WHERE author = :author AND title = :title''', {'author': author, 'title': title})

    return cu.fetchall()


boo = Book(65146546, "Compiler", "Shapoori", "Rahyaft")

# insert(boo)
# delete(65146546)
# update_publisher(65146546, "Rahian arshad")

# print(select_author_title("Fardin", "OS"))

# print(select_all())