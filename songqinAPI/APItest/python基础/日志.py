# auto :liyongbing  
# time: 2021/1/5

import logging
import time
import traceback # 异常信息显示模块
filename = time.strftime("%y-%m-%d")

logging.basicConfig(level='DEBUG', filename=f'../log/'+filename+'.log',filemode='a',)  # 调整级别，打印所有信息
# logging.info('这是info信息')
# logging.debug('这是debug信息')
# logging.warning('这是warning信息') # 默认只打印warning信息
# logging.error('这是error信息')
# logging.critical('这是critical信息')

try:
    1 / 'q'

except Exception as e:
    logging.error(time.strftime("%y-%m-%d %H:%M:%S")+'--'+traceback.format_exc())

else:
    print('程序没有异常执行')

finally:
    print('程序最终执行')