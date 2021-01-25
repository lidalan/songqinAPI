# autu :liyongbing
# time: 2021/1/3
import requests
from config.emis_con import EMIS_conf as emis
import json
import pprint
filldle ={'http':'http://127.0.0.1:8888'}

class Test_Emis():
    HOST = 'http://localhost:8111/'
    """教管系统"""

    def get_md5(self):
        """md5加密"""
        pass

    def test_login(self, username, password, flag=True):
        """登录接口"""
        login_url = f'{Test_Emis.HOST}api/mgr/loginReq'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload_login = {'username': username,
                         'password': password}
        res = requests.post(url=login_url, data=payload_login, headers=header)
        if flag:
            return res.cookies['sessionid']
        else:
            return json.loads(str(res.text))
            # print(json.loads(str(res.text)))

    def test_add_course(self):
        """增加课程"""
        add_course_url = f'{Test_Emis.HOST}api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload_add_course = {'action': 'add_course',
                              'data': '''
                              {
                                      "name":"初中化学4",
                                      "desc":"初中化学课程",
                                      "display_idx":"4"
                            }
                                     '''}
        res = requests.post(url=add_course_url, data=payload_add_course, headers=header)
        print(json.loads(str(res.text)))
        return json.loads(str(res.text))

        # print(res.request.body)

    def get_course(self):
        """查询所有课程"""
        get_course_url = f'{Test_Emis.HOST}api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}

        param = {'action': 'list_course',
                 'pagenum': 1,
                 'pagesize': 20}
        res = requests.get(url=get_course_url, params=param, headers=header)
        # print(res.request.url)
        pprint.pprint(json.loads(str(res.text)))

    def modify_course(self):
        modify_course_url = f'{Test_Emis.HOST}api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        modify_course_data = {
                    'action': 'modify_course',
                    'id': 2177,
                    'newdata': '''{"name":"初中化学5",
                            "desc":"初中化学课程5",
                    "display_idx":"5" }
                    '''}
        res = requests.put(url=modify_course_url, headers=header, data=modify_course_data)
        print(res.text)

    def delete_course(self):
        delete_course_url = f'{Test_Emis.HOST}api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'action': 'delete_course',
                'id': '2177'}
        res = requests.delete(url=delete_course_url, data=data, headers=header)
        print(res.request.url)
        print(json.loads(str(res.text)))

    def add_course_json(self):
        add_course_url = f'{Test_Emis.HOST}apijson/mgr/sq_mgr/'
        header = {'Content-Type': 'application/json'}
        payload = {
                "action": "add_course_json",
                "data":
                    {
                        "name": "初中化学44",
                        "desc": "初中化学课程",
                        "display_idx": "44"
  }
}
        res = requests.post(url=add_course_url, headers=header, json=payload, proxies=filldle)
        print(json.loads(str(res.text)))
        # print(res.request.body)







if __name__ == '__main__':
    emis =Test_Emis()
    # emis.test_add_course()
    # emis.get_course()
    # print(emis.test_login('auto','sdfsdfsdf'))
    # emis.modify_course()
    # emis.delete_course()
    emis.add_course_json()