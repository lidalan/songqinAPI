# # auto :liyongbing
# # time:
#
#
# class Person:
#     nickName = '人类' # 类属性
#
#     def __init__(self, name, age, weight): # 实例属性
#         self.name = name
#         self.age = age
#         self.weight = weight
#         print('mingzi,nian', name, age, self.nickName)
#
#     def eat(self):
#         self.weight += 10
#         print('eat---体重增加了10kg', self.weight)
#
#     @classmethod
#     def say(cls):
#         cls.nickName='renlei'
#         print('我叫：{}'.format(cls.nickName))
#
#     @classmethod
#     def say2(cls):
#         print('我叫：{}'.format(cls.nickName))
#
#     @staticmethod
#     def run():
#         print('我叫：{}'.format())
#
#     @property
#     def getName(self):
#         print(self.name)
#
# p1 = Person('黄飞鸿', 12, 190)
# # print(p1.nickName)
# # print(Person.nickName)
# # print(p1.age)
# # print(Person.age)
#
# # p1.eat()
# # Person.eat()
# # p1.say2()
# # Person.say()
# # p1.say2()
# # p1.run('黄飞鸿')
# # Person.run('黄飞鸿')
# Person.getName
# p1.getName


class Tiger:
    nickName = '老虎'
    __money=12

    def __init__(self, weight):
        self.weight = weight

    def __fangfa(self):
        print('我是私有方法')
    def roar(self):
        print(Tiger.nickName)

        print('我又很多钱',self.__money)
        self.__fangfa()
        self.weight -= 5
        print('我是老虎--wow--体重减5kg')

    def feed(self, foot):
        # if foot == 'meat':
        #     self.weight += 10
            print('喂对了体重加10kg')
        # else:
        #     self.weight -= 5
        #     print('喂错了，体重减5kg')


class smallTiger(Tiger):
    def feed(self, foot):
        super().feed(foot)
        Tiger.feed(self,foot)
        print('11111111111',foot)
    # pass

Tiger(12).roar()
sm = smallTiger(1200)
print(smallTiger.__bases__)    # 显示父类方法
print(sm.roar())
# sm.feed('rice')

# class Sheet:
#     nickName = '羊'
#
#     def __init__(self, weight):
#         self.weight = weight
#
#     def roar(self):
#         self.weight -= 5
#         print('我是羊--mei--体重减5kg')
#
#     def feed(self, foot):
#         if foot == 'grass':
#             self.weight += 10
#             print('喂对了体重加10kg')
#         else:
#             self.weight -= 5
#             print('喂错了，体重减5kg')
#
#
# class Room:
#     def __init__(self, inNum, inAnimale):
#         self.inAnimale = inAnimale
#         self.inNum = inNum



if __name__ == '__main__':
    pass
    # t1 = Tiger(200)
    #
    # # t1.feed('cao')
    # # print(t1.weight)
    # # t1.feed('rou')
    # # print(t1.weight)
    #
    # r1 = Room(1, t1)
    # r1.inAnimale.roar()
    # print(r1.inAnimale.weight)

    # t3 = Tiger(200)
    # print(t3.__dict__)   # 显示对象的属性
