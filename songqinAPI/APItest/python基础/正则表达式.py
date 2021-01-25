# auto :liyongbing  
# time: 2020/12/27
import re
#
#
# res = re.findall('son(.)',r'songqinson')
# print(res)
# res1 = re.findall('s+',r'songssqins')
# print(res1)
# res2 = re.findall('s\w+',r'songssqins')
# print(res2)
res2 = re.findall('\d+',r'15252535354$$$17485066999')
print(res2)
res2 = re.findall('\d+?',r'15252535354$$$17485066999')
print(res2)