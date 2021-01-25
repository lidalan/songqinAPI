# auto :liyongbing  
# time: 2020/12/26

import json


data = {"name":'wyta','agen':12}
# print(type(data))
# print((data))
# print(type(json.dumps(data)))
# print((json.dumps(data)))
# 文件的序列化就是将json数据写入到文件中

json.dump(data,open('json_xuliehua','w'))
# #
# with open('json_xuliehua','w') as f:
#     json.dump(data,f)

# 文件反序列化就是读取json文件
data = json.load(open('./homework/data.txt'))
print(data)
# with open('json_xuliehua') as f:
#     data = json.load(f)
#
# print(data)
