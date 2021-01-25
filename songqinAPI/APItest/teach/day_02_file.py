# autu :liyongbing
# time: 2021/1/2
import requests, json
import hashlib  # 加密库


def get_md5():
    # 加密一定是type  字节形式  b''
    pwd = hashlib.md5(b'zr111111hg').hexdigest()  # 获取16进制的值
    # print(type(pwd))
    return pwd


def get_md5_1(pwd):

    md5 = hashlib.md5()  # 实例化md5对象
    md5.update(pwd.encode('utf-8'))  # 需要进行编码操作，防止错误加密操作
    return md5.hexdigest()  # 返回十六进制对象





def get_token():
    # 密码md5加密
    url = 'http://121.41.14.39:2001/login/redis/login'
    payload = {'mobile': '13588000000',
            'password': get_md5()}
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = requests.post(url=url, data=payload)
    print(res.text)
    return json.loads(res.text)['data']
# 49ef7e51fcfb43b1bb87015841365451


def upload():
    url = 'http://121.41.14.39:2001/user/doUpload'
    # 封装cookies
    cookie = {'token': get_token()}
    # (文件名称，文件对象--二进制形式，类型)
    file_data = {'file':('updata_png.png',open(r'C:\Users\51064\Desktop\updata_png.png','rb'), 'jpg/png/gif')}
    header = {}
    res = requests.post(url=url, cookies=cookie,files =file_data )
    print(res.text)

if __name__ == '__main__':
    # print(get_token())
    # print(get_md5())
    upload()
    # print(get_md5_1('zr111111hg'))
