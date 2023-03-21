class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def introduce(self):
        print(f'Hello my name is {self.name} and I am {self.height}cm tall')

    def yell(self):
        print('아?')
    

class Developer(Person):
    
    def __init__(self, name, age, height, keyboard = '기계식'):
        super().__init__(name, age, height)
        self.keyboard = keyboard
        

    def yell(self):
        print('어?')
    
class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease

class ProductManager(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)

    def aging(self):
        self.age += 2
        self.height -= 5
        print('개발자를 새로 뽑아야하나...')
        Developer.keyboard = '멤브레인'

d1 = Developer('김지호', 26, 182)
p1 = ProductManager('이수경', 26, 164)

d1.introduce()
d1.yell()

p1.introduce()
p1.yell()

p1.aging()
p1.introduce()



        
