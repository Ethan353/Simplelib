import sqlite3

# make (if there is no db with that name) and connect to sql
connection = sqlite3.connect('Libdb.db')

# make a curser which  allows us to execute sql command then we can run sql commands with execute method
cu = connection.cursor()

# cu.execute("""CREATE TABLE "Staff" (
#         "staff_id" VARCHAR(20) NOT NULL,
#         "name" VARCHAR(40) NOT NULL,
#         "password" VARCHAR(40) NOT NULL,
#         PRIMARY KEY	( staff_id )
#         );
#         """)

# cu.execute("""CREATE TABLE "Student" (
#             "userid" VARCHAR(20) NOT NULL,
#             "deptname" VARCHAR(40) NOT NULL,
#             "name" VARCHAR(40) NOT NULL,
#             "password" VARCHAR(40) NOT NULL,
#             PRIMARY KEY	( userid ));
#             """)

connection.commit()

connection.close()