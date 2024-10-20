# 面向对象的三大特性之一,封装

# 私有成员变量
# 私有成员方法
# 以两个下划线开头(__)即可完成对私有成员的定义

class Phone:
    IMEI = None
    producer = None
    __current_voltage = 1

    def __keep_single_core_running(self):
        print('cpu单核运行!')

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print('5G启动!')
        else:
            self.__keep_single_core_running()
            print('没电了,启动不了一点!')

phone = Phone()
# phone.__Keep_single_core_running() # 无法类外调用私有成语方法
# print(phone.__current_voltage) # 无法类外调用私有变量

phone.call_by_5g()
