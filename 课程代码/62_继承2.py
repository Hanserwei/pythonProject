# 若子类继承父类的成员属性和成员方法之后,对其不满意可以,可以进行覆写,即重新定义同名属性或者方法
class Phone:
    IMEI = None
    producer = "XM"
    def call_by_4g(self):
        print('4G通话!')

class Phone2(Phone): # Phone2内的属性包含了Phone的所有的内容(不含私有)
    face_id = None
    producer = 'HW'

    def call_by_5g(self):
        print('5G通话!')

    def call_by_4g(self):
        print('新4G通话!')

myphone = Phone2()
print(myphone.producer)
myphone.call_by_4g()

# 覆写之后若要使用父类的成员
# 在子类中调用父类的成员变量和成员方法
# 使用成员变量: 父类名.成员变量
# 使用成员方法: 父类名.成员方法(self)
# 使用super()调用父类成员
# super().成员变量
# super().成员方法
