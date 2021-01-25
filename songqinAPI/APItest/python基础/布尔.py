import copy
#
#
# # 深拷贝，浅拷贝 ---元素可变才可以，元素不可变只能赋值
# #场景：一个元数据，第一个接口需要调用元数据，第二个接口，也需要调用元数据
# # 1 赋值，仅仅是对象的指向和引用,list2和list1，指向同一个地址，改变一个值，同时另一个也发送变化，因为他们指向的是同一个地址
# list1 = [1, 2, 3, 4]
# list2 = list1
#
# list2.append(2)
# print(list1)
# print(list2)
# # [1, 2, 3, 4, 2]
# # [1, 2, 3, 4, 2]
# print("**********************************")
# # 浅拷贝  --拷贝不彻底,如果只有一层列，浅拷贝可以达到效果，但如果存在子列表，浅拷贝不满足要求，因为他们子列表是指向同一个地址
# # 复制出元素的第一层，对复制出的列表操作，不影响元列表，因为他们不在指向同一个地址
# list3 = [1, 2, 3, 4,[2,3]]
# list4 = copy.copy(list3)
# list3.append(2)
# print(list4)
# print(list3)
# # [1, 2, 3, 4, [2, 3]]
# # [1, 2, 3, 4, [2, 3], 2]
# print("**********************************")
# # 深拷贝,对子列表操作有效
# list5 = [1, 2, 3, 4,[2,3]]
# list6 = copy.deepcopy(list5)
# list6[-1].append(10)
# print(list5)
# print(list6)
#
# # [1, 2, 3, 4, [2, 3]]
# # [1, 2, 3, 4, [2, 3, 10]]


# print('shizhen',isinstance(1,int))


phone = input('请输入电话号码：\n')
no = int(phone[0:3])
if phone.isdigit():

    if not len(phone) == 11:
        print("号码长度错误")
    else:
        if no >= 130 and no <= 150:
            print("移动")

        elif no > 150 and no <= 170:
            print('联通')

        elif no > 170 and no <= 199:
            print('电信')
        else:
            print('其他')
else:
    print("输入非法字符")





# tup = (1,2,3)
# print(*tup)