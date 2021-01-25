# auto :liyongbing  
# time: 2020/12/26
import pprint
import json
def readFile(filename):
    with open(filename,encoding='utf-8') as f:
        return f.read().split('\n')


def putInfoToDict(fileName):
    stu_dict = {}
    data = readFile(fileName)
    # 拆分数据
    for i in data:
        # 清洗数据
        if i != '':
            datas = i.replace(';','').replace('(','').replace(")",'').replace("'",'').strip(',').strip()
            # 拆分单个元素，获取时间，学生id，课程id
            shuju = datas.split(',')
            times = shuju[0].strip()
            courseid = int(shuju[1].strip())
            studendid = int(shuju[-1].strip())
            # key 则添加进去
            if studendid not in stu_dict:
                stu_dict[studendid] = []
            # 将相同的key的value值追加到列表中
            stu_dict[studendid].append({'lessonid':courseid,'checkintime':times})
    pprint.pprint((stu_dict))
    with open('data.txt','w') as f:
        json.dump(stu_dict,f)

if __name__ == '__main__':
    putInfoToDict('work_05_01.txt')