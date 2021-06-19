
class Student:
    def __init__(self, userid, name, password, deptname):
        self.userid = userid
        self.name = name
        self.deptname = deptname
        self.password = password

    def __str__(self):
        return f"{self.name}, {self.deptname}"