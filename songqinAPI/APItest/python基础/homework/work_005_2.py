# auto :liyongbing  
# time: 2020/12/26


def readFile(filename):
    with open(filename,encoding='utf-8') as f:
        return f.read().splitlines()





def FiveWork(filename):
    data = readFile(filename)
    # 获取员工的姓名和薪资
    for i in data:
        # 排除空数据
        if i != '':
            # 分割出获取姓名和信息
            nameData, salaryData = i.split(';')
            # print(nameData, salaryData)
            name = nameData.split(':')[-1].strip()
            salary = int(salaryData.split(':')[-1].strip())
            # print(name, salary)
            datas = f'name: {name:<6};salary: {salary:>5}; tax: {int(salary*0.1):>4}; income: {int(salary*0.9):>5}\n'
            #
            with open('upto_work_05_02.txt','a') as f:
                f.write(datas)

if __name__ == '__main__':
    # print(readFile('work_05_02.txt'))
    FiveWork('work_05_02.txt')