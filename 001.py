# -*-coding:utf-8 -*-


class People(object):
    def __init__(self, age):
        print 'P'
        self.age = age

    def getinfo(self):
        return self.age,self.name

    def setinfo(self, newage):
        self.age = newage
    
    x = property(getinfo, setinfo)


class Student(People):
    def __init__(self, age):
        print 'S'
        self.age = age
    # def info(self):
    #     print self.name + ':' + str(self.score)
    #     print self.age


stu1 = Student(22)
stu1.name = '乔'
# stu1.score = 100
# stu1.info()
# stu1.getinfo()
print stu1.x[0],stu1.x[1].decode('utf-8')
stu1.x = 18
print stu1.x[0],stu1.x[1].decode('utf-8')
1111111111111


