# # def fi(a, b=3):
# #     print(a, b)
# #
# #
# # fi(1, b=4)
#
# def f2(a,*kwargs):
#
#     print(a,kwargs)
#
# f2(1,3,4,5,6,7,)
#
#
# def f3(*kwargs,a,b):
#     '''zhegNNM<<>>'''
#     print(a,kwargs)
#
# f3(2,3,4,5,a='ton',b=11)
#
#
# f =open()

a = 'qwerrewq'
# print(a.count(a))
# f = open(r'C:\Users\51064\Desktop\file.txt')
# print(f.read())
# print(a.find('e', 2))

# list1 = ['2','3','8']
# # print('*'.join(list1))
# print(a.replace('e',"*",1))
# print(dir(str))
# print(a.strip('w'))

def f1(a,*args):
    return a, (*args)

print(f1(1,34,5,6,))