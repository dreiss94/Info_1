
### implement class Module here ###
class Module(object):
    def __init__(self, ects, title, semester, grade=None):
        self.ects = ects
        self.title = title
        self.semester = semester
        self.grade = grade
        self.dates = []
        self.elements = []

    def get_important_dates_overview(self):
        for elt in self.dates:
            print(elt)

    def set_grade(self, new_grade):
        self.grade = new_grade

    def add_module_element(self, other_class, date):
        new_object = other_class(self)
        new_object.add_important_date(date)
        self.elements.append(new_object)

################################################################################

### implement class ModuleElement here ###
class ModuleElement(object):
    def __init__(self, module):
        self.module = module
    def add_important_date(self, kind_of_date, date):
        self.module.dates.append((kind_of_date, date))

################################################################################

### implement class Lesson here ###
class Lesson(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "Lesson", date)

################################################################################

### implement class Lab here ###
class Lab(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "Lab Session", date)

################################################################################

### implement class Midterm here ###
class Midterm(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "Midterm", date)


################################################################################

### implement class FinalExam here ###
class FinalExam(ModuleElement):
    def __init__(self, module):
        ModuleElement.__init__(self, module)

    def add_important_date(self, date):
        ModuleElement.add_important_date(self, "Final Exam", date)

################################################################################

### test cases ###

info1 = Module(6,"Info 1",1)
info1.add_module_element(Midterm,"31.10.2017")
info1.add_module_element(FinalExam,"20.12.2017")
info1.get_important_dates_overview()

