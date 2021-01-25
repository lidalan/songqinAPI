# -*- coding:utf-8 -*-
# autu :liyongbing  
# time: 2021/1/15
import requests,json
from config.config import HOST


def file_upload(filename, filepath, filetype,token):
    """
    文件上传接口
    :param filename:
    :param filedir:
    :param filetype:

    :return:
    """
    url = f'{HOST}/file'
    # 封装cookies
    header = {'Authorization': token}
    # (文件名称，文件对象--二进制形式，类型)
    file_data = {'file': (filename, open(filepath, 'rb'), filetype)}

    res = requests.post(url=url, headers=header, files=file_data)
    # print(res.json())
    return json.loads(res.text)['data']['realFileName']


if __name__ == '__main__':
    print(type(file_upload('updata_png.png',
                r'C:\Users\51064\Desktop\updata_png.png',
                'image/png', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1Ni'
                             'J9.eyJleHAiOjE2MTA5ODQxNzAsInVzZXJJZCI6MTAwOD'
                             'csInVzZXJuYW1lIjoibWQwMDgzIn0.tvZXFJ9kSmTWSgPu1Q'
                             'gi1ZYWWFEsExqMqfxFRjNXENc')))


