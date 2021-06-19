
class Library:
    def __init__(self, accessinno, lib_isbn, lib_userid="nobody"):
        self.accessinno = accessinno
        self.lib_isbn = lib_isbn
        self.lib_userid = lib_userid

    def __str__(self):
        return f"{self.accessinno}, {self.lib_isbn}, {self.lib_userid}"