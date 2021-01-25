# auto :liyongbing  
# time: 2020/12/24


# 获取学生信息
stu_info= input('请输入学生信息，按照如下格式输入：\n"Jack Green ,   21  ;  Mike Mos, 9;":\n')
# 提取学生信息到列表
info_list= stu_info.split(';')
del info_list[-1]
print(info_list)

# 提取每个员工信息
for i in info_list:
    tem = i.split(',')
    name = tem[0].strip()
    age = int(tem[1].strip())
    print('{:<20}:{:0>2}'.format(name, age), end='\n')