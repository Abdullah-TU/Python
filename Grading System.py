class Course:
    def __init__(self, name='', credits=0, grade=0):
        self.name=name
        self.credits=credits
        self.grade=grade
    def __str__(self):
        return 'Name: {}\nCredits: {}\nGrade: {}'.format(self.name, self.credits, self.grade)

class Student:
    def __init__(self, name='', number=0):
        self.name=name
        self.number=number
        self.cl=[]
    def __str__(self):
        return '{} ({})'.format(self.name, self.number)
    def addCourse(self, c=Course()):
        self.cl.append(c)
    def coursesByName(self):
        self.cl.sort(key=lambda x:x.name)
        for i in self.cl:
            print(i)
            print()
    def coursesByCredits(self):
        self.cl.sort(key=lambda x: x.name)
        self.cl.sort(key=lambda x: x.credits, reverse = True)
        for i in self.cl:
            print(i)
            print()
    def coursesByGrade(self):
        self.cl.sort(key=lambda x: x.name)
        self.cl.sort(key=lambda x: x.grade, reverse = True)
        for i in self.cl:
            print(i)
            print()
    def credits(self):
        cr=0
        for i in self.cl:
            cr+=int(i.credits)
        return cr

