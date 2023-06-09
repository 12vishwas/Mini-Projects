# class computer:

#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram


#     def config(self):
#         print('config is', self.cpu, self.ram)



# com1  = computer('i5', '16gb')
# com2 = computer('i3', '8gb')


# computer.config(com1)
# computer.sum(com2)

# com1.config()
# com2.config()

# class computer:

#     def __init__(self):
#         self.name = 'naveen'
#         self.age = 25

#     def compare(self,other):
#         if self.age == other.age:
#             print('They r same')
#         else:
#             print("They r different")
         

        

# c1 = computer()
# c2 = computer()

# c1.name = 'rashi'
# c1.age = 20


# c2.compare(c1)
    

# print(c1.name)
# print(c2.name)
# print(c1.age)
# print(c2.age)

# class car():

#     wheels = 4

#     def __init__(self):
#         self.mil = 8
#         self.com = "BMW"

# c1 = car()
# c2 = car()

# c1.mil = 10
# print(c1.mil,c1.com,c1.wheels)
# print(c2.mil,c2.com,c2.wheels)

# class student():

#     school = 'telusko'


#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)/3
    
#     def get_m1(self):
#         return self.m1
    
#     def set_m1(self,value):
#         self.m1 = value

#     @classmethod
#     def getschool(cls):
#         return cls.school
    
#     @staticmethod
#     def info():
#         return "this is a student class"


# s1 = student(23,45,68)
# s2 = student(56,78,90)


# print(s1.get_m1())
# print(student.getschool())
# print(student.info())

# class A():

#     def __init__(self):
#         print('in A init')

#     def feature1(self):
#         return('this is feature 1')

#     def feature2(self):
#         return ('this is feature 2')
    
# class B(A):

#     def __init__(self):
#         super().__init__()

#     def feature3(self):
#         return("this is feature 3")
    
#     def feature4(self):
#         return("this is feature 4")
    
# class C(B):
#     def feture5(self):
#         return("this is feature 5")

# a1 = A()
# a2 = A()

# b1 = B()
# b2 = B()

# c1 = C()
# print(b1.init())

# class pycharm:
    
#     def execute(self):
#         return('compiling')
#         return('running')

# class myeditor:

#     def execute(self):
#         return('spell check')
#         return('convention check')
#         return('compiling')
#         return('running')

# class laptop:

#     def code(self,ide):
#         ide.execute()

# ide = myeditor()
# lap1 = laptop()
# lap1.code(ide)

# class student:

#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2

#     def __add__(self,other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = student(m1,m2)
#         return s3
    
#     def __gt__(self,other):
#         r1 = self.m1 +self.m2
#         r2 = other.m1 + other.m2

#         if r1 > r2:
#             return True
#         else:
#             return False
    
#     def __str__(self):
#         return '{} {}'.format(self.m1,self.m2)
    
# s1 = student(78,89)
# s2 = student(60,90)
# s3 = s1 + s2
# print(s1.m1,s1.m2)
# if s1 > s2:
#     print('s1 wins')
# else:
#     print('s2 wins')

# print(s1)

# concept of method overloading

# class method:

#     def sum(self,a=None,b=None,c=None):
        
#         if a!=None and b!=None and c!=None:
#             s = a+b+c
#         elif a!=None and b!=None:
#             s = a+b
#         else:
#             s = a

#         return s

# s1 = method()
# print(s1.sum(12,14,15))


# method overriding
# class A:

#     def show(self):
#         print("in A show")

# class B(A):

#     def show(self):
#         print("in B method")

# s1 = B()
# s1.show()

from sketchpy import library as lib
obj = lib.rdj()
obj.draw()

    




