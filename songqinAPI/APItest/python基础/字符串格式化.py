# height = 187.65
# name = 'tony{}'
# age = 12
# rate = "23"
#
# # print('我的名字叫：%-05s,年龄：%09s，身高：%1.2fcm，增长率%s' %(name, age, height, rate))
# print('我的名字叫{:0>7}，年龄：{:*>7}，身高：{:&>7}，增长率{:#>7}%'.format(name, age, height, rate))
#
# print('我的名字叫{0}，年龄：{1}，身高：{1}，增长率{1}%'.format(name, age, height, rate))
#
# print(f'我的名字叫{name}，年龄：{age}，身高：{height}，增长率{rate}%')
# print(str([1,2]))
#
# def t(a):
#     a= 3
#
# b='2'
# t(b)
# print(b)

str1 = 'A old lady come in, the name is Mary, level 94454'

data = str1.replace(' ', '').split('is')[1].split(',')[0]
print(data)