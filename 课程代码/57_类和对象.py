# 程序中的类也有属性和行为
# 类类比于设计图纸,但是需要基于图纸生产实体(对象),才可以正常工作,这种套路称之为面向对象编程

class Clock:
    id = None
    price = None

    def ring(self):
        print(f"{self.id}闹钟开始叫唤了!\n{self.id}号闹钟价值{self.price}!")
        return

clock1 = Clock()
clock1.id=1
clock1.price=100
clock1.ring()
