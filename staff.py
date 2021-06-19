
class Staf:
    def __init__(self, staffid, name):
        self.staffid = staffid
        self.name = name

    def __str__(self):
        return f"staff '{self.name}', {self.staffid}"
