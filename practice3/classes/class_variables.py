class Student:
    school = "ABC School"   # ← class variable

    def __init__(self, name):
        self.name = name    # ← instance variable

#2
class Person:
    count = 0   # class variable

    def __init__(self, name):
        self.name = name
        Person.count += 1
