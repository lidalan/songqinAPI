# auto :liyongbing  
# time: 2021/1/3

import requests
from config.emis_con import EMIS_conf as emis
import json
import pprint

filldle ={'http':'http://127.0.0.1:8888'}


class Emis_training():
    HOST = 'http://localhost:8111'
    """教管系统"""

    def add_training(self):
        url = f'{Emis_training.HOST}/api/mgr/sq_mgr/'
        header ={'Content-Type':'application/x-www-form-urlencoded'}
        data ={'action': 'add_training',
               'data': '''{
                    "name":"接口自动化2",
                    "courselist": "[]",
                    "desc": "45期接口自动化课程2",
                    "display_idx": 1

}
'''}
        res = requests.post(url=url, data=data, headers=header)
        # print(json.loads(str(res.text)))
        print(res.text)

    def list_training(self):
        url =f'{Emis_training.HOST}/api/mgr/sq_mgr/'
        data = {'action': 'list_training',
                'pagenum': 1,
                'pagesize': 20}
        res = requests.get(url=url, params=data)
        pprint.pprint(json.loads(str(res.text)))

    def modify_training(self):
        url = f'{Emis_training.HOST}/api/mgr/sq_mgr/'
        data = {'action': 'modify_training',
                'id': 51,
                'newdata': '''{
                    "name":"接口自动化11111",
                    "courselist":[{"id":2179,"name":"初中化学3"}],
                    "desc":"45期接口自动化课程21111",
                    "display_idx":"22"}
                '''
                }
        res = requests.put(url=url, data=data,proxies=filldle)
        print(json.loads(str(res.text)))
#
    def delete_training(self):
        url = f'{Emis_training.HOST}/api/mgr/sq_mgr/'
        data = {'action': 'delete_training',
                'id': 51}
        res = requests.delete(url=url, data=data)
        print(json.loads(str(res.text)))




if __name__ == '__main__':
    training = Emis_training()
    # training.add_training()
    # training.list_training()
    # training.modify_training()
    training.delete_training()
