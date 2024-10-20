class Student_information:
    name = None
    age = None
    address = None
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

for num in range(1,11):
    print(f'当前是第{num}位学生在录入信息,一共需要录入10位学生的信息!')
    stu = Student_information(input('请输入学生姓名:'),int(input('请输入学生年龄:')),input('输入学生地址:'))
    print(f"学生{num}的信息录入完成,信息为:[学生姓名:{stu.name},年龄:{stu.age},地址:{stu.address}]")
