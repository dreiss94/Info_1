from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}
        ######## CODE MISSING HERE

    def add_module(self,module):
        self.modules.append(module)
        self.grades[module] = module.get_grade()
        ######## CODE MISSING HERE

    def get_list_modules(self):
        print('Modules of Student {}'.format(self.name))
        for e in self.modules:
            print('\t'+ e.get_title())
        ######## CODE MISSING HERE

    def get_grades(self):
        print('Grades of Student {}'.format(self.name))
        for key in self.grades:
            print('\t' '{}: {}'.format(key.get_title(), self.grades[key]))
        ######## CODE MISSING HERE


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
