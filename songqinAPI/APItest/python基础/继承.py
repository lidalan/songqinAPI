# auto :liyongbing  
# time: 2020/12/21


class Tiger:
    nickNane = '老虎'
    __height = 100 # 私有属性

    def __init__(self, weight, age):
        self.weight = weight
        self.age = age

    def eat(self, food):
        print('我是老虎，我喜欢吃{}'.format(food))


class Momtiger():
    def eat(self,people):
        print('我是母老虎，我贴别喜欢吃{}'.format(people))


class SmallTiger(Momtiger,Tiger):
    def __init__(self, weight, age, name):
        Tiger.__init__(self,weight, age)
        self.name = name

    def myWeight(self):
        print('我的体重{}'.format(self.weight))

    def eat(self, grass, meat):
        # Tiger.eat(self, meat)
        super().eat(meat)
        print(('我是{}，我不喜欢吃{}'.format(self.name, grass)))




if __name__ == '__main__':
    # t1 = SmallTiger(110, 22, '小老虎')
    # print(t1.nickNane)
    # t1.eat('cao','肉')
    # # t1.myWeight()
    name, age = [1, 2]
    print(name, age)
