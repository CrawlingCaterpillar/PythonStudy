class Dog():
    """"一次模拟小狗的简单测试"""

    def __init__(self, name="hello", age=0):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now stting")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over")


my_dog = Dog('willie', 6)
print("My Dog's Name is " + my_dog.name.title() + ".")
print("My Dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
