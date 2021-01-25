# autu :liyongbing
# time: 2021/1/3
import requests
from config.emis_con import EMIS_conf as emis
import json
import pprint
# filldle ={'http':'http://127.0.0.1:8888'}


class Emis_teacher():
    HOST = 'http://localhost:8111'
    """教管系统"""

    def add_teacher(self):
        url = f'{Emis_teacher.HOST}/api/mgr/sq_mgr/'
        header ={'Content-Type':'application/x-www-form-urlencoded'}
        data ={'action': 'add_teacher',
               'data': '''{
                    "username":"lishiming1",
                    "password":"sq888",
                    "realname":"李世民",
                    "desc":"李世民老师",
                    "courses":[{"id":2179,"name":"初中化学3"}],
                    "display_idx":1
}
'''}
        res = requests.post(url=url, data=data, headers=header)
        print(json.loads(str(res.text)))

    def list_teacher(self):
        url =f'{Emis_teacher.HOST}/api/mgr/sq_mgr/'
        data = {'action': 'list_teacher',
                'pagenum': 1,
                'pagesize': 20}
        res = requests.get(url=url, params=data)
        pprint.pprint(json.loads(str(res.text)))

    def modify_teacher(self):
        url = f'{Emis_teacher.HOST}/api/mgr/sq_mgr/'
        data = {'action': 'modify_teacher',
                'id': 263,
                'newdata': '''{
                    "username":"lidadan",
                    "password":"sq888",
                    "realname":"李大蛋",
                    "desc":"李大蛋老师",
                    "courses":[],
                    "display_idx":1
}               
                '''}
        res = requests.put(url=url, data=data)
        print(json.loads(str(res.text)))

    def delete_teacher(self):
        url = f'{Emis_teacher.HOST}/api/mgr/sq_mgr/'
        data = {'action': 'delete_teacher',
                'id': 263}
        res = requests.delete(url=url, data=data)
        print(json.loads(str(res.text)))




if __name__ == '__main__':
    teacher = Emis_teacher()
    # teacher.add_teacher()
    # teacher.list_teacher()
    # teacher.modify_teacher()
    teacher.delete_teacher()