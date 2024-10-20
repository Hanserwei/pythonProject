# 继承的概念
# 继承是指把已有的功能拿过来继续用

# 语法
# 单继承
class Phone:
    IMEI = None
    producer = "XM"
    def call_by_4g(self):
        print('4G通话!')

class Phone2(Phone): # Phone2内的属性包含了Phone的所有的内容(不含私有)
    face_id = None

    def call_by_5g(self):
        print('5G通话!')

# 多继承
class RemoteControl:
    rc_type = "红外遥控!"
    producer = "HW"

    def control(self):
        print("开启红外遥控!")

class NFC:
    NFC_type = "5代"
    def nfc_control(self):
        print('5代NFC')

class MyPhone(Phone2,RemoteControl,NFC):
    pass # 补全语法

myphone = MyPhone()
# 多继承若父类成员的名称一样,谁先继承谁的优先级更高
print(myphone.producer)
