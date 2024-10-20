# 多态是指多种状态,在完成某个行为的时候,使用不同的对象得到不同的状态

class Animal:
    def speak(self):
        pass
# 父类是空实现,称之为抽象类

class Dog(Animal):
    def speak(self):
        print("汪汪汪!")

class Cat(Animal):
    def speak(self):
        print("喵喵喵!")

def make_noise(animal:Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)