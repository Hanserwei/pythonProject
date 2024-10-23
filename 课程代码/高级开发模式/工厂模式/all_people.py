class People:
    pass

class Worker(People):
    pass

class Student(People):
    pass

class Teacher(People):
    pass

class Factory:
    def Get_Person(self,p_type):
        if p_type == 'student':
            return Student()
        elif p_type == 'teacher':
            return Teacher()
        elif p_type == 'worker':
            return Worker()

factory = Factory()
worker = factory.Get_Person('worker')
teacher = factory.Get_Person('teacher')
student = factory.Get_Person('student')

# 有统一的入口，代码易于维护

