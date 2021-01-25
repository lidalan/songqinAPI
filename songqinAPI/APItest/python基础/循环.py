# def add(start, end, step=1):
#     # i = start
#     sum = 0
#     while start <= end:
#         sum += start
#         start += step
#     return sum
#
#
#
#
# print(add(1,100,2))
# # print(2550*2)

# 乘法口诀
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}*{}={:>2}'.format(j, i, i*j),end='')
#         print(end=' ')
#     print()


# 列表推导式/生成式
# lit1 = [8000,9000,10000]
# print(type(x*1.1 for x in lit1))
# print([x*1.1 for x in lit1 if x!=8000])


# for i in range(10):
#     if i == 5:
#         break
#         continue
#     else:
#         print(i)
# else: # 当循成功环循环结束，打印else内容----continue 可以执行，break 结束循环，所有不打印
#     print("结束")

n= 100

class F:
    pass

import time
for i in range(10,-1,-1):
    print(f'\r倒计时{i}秒', end='')  # \r光标返回行首
    time.sleep(1)
else:
    print('\r倒计时结束')