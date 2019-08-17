from tqdm import tqdm
from time import sleep

# for i in tqdm(range(10),leave=True, ncols = 100, mininterval = 0.3):
#     '''do something'''
#     sleep(0.1)
#     pass


with tqdm(total=100) as pbar:
    for i in range(10):
        sleep(0.1)
        pbar.update(10)
 
 
# 也可以这样
pbar = tqdm(total=100)
for i in range(10):
    pbar.update(10)
pbar.close()


from tqdm import trange
from random import random, randint
from time import sleep
with trange(100) as t:
    for i in t:
        # Description will be displayed on the left
        t.set_description('下载速度 %i' % i)
        # Postfix will be displayed on the right,
        # formatted automatically based on argument's datatype
        t.set_postfix(loss=random(), gen=randint(1,999), str='详细信息',
                     lst=[1, 2])
        sleep(0.1)

#iterable=None,            
#desc=None,      传入str类型，作为进度条标题（类似于说明）
#total=None,     预期的迭代次数
#leave=True,             
#file=None, 
#ncols=None,         可以自定义进度条的总长度
#mininterval=0.1,    最小的更新间隔
#maxinterval=10.0,   最大更新间隔
#miniters=None, 
#ascii=None, 
#unit='it',
#unit_scale=False, 
#dynamic_ncols=False, 
#smoothing=0.3,
#bar_format=None, 
#initial=0, 
#position=None, 
#postfix             以字典形式传入 详细信息 例如  速度= 10，  


dict = {"a":123,"b":456}
for i in tqdm(range(10), leave=True, desc = "进度条测试", ncols = 100,unit_scale=False, dynamic_ncols=False, postfix = dict, mininterval = 0.3):
    sleep(1)
    pass