#功能协程并发

import  threading #线程接口
import  time      #时间
import eventlet   #并发
cc

eventlet.monkey_patch() #线程控制
pool = eventlet.GreenPool(10) #并发数
InspectLock = threading.Lock() #数据锁
xxs=[1,2,3,4,5,6,7,8,9] #测试数据

def time1():
    time.sleep(1)
def time2():
    time.sleep(1)


def xx(xx):
    print ("start",xx)
    print xx
    time1()
    print ("end")

    print("start1",xx)
    time2()
    InspectLock.acquire()
    print ("start2",xx)
    time1()
    InspectLock.release()

    time2()
    print ("start3",xx)
print time.time()
[x for x in  pool.imap(xx,xxs)]
print time.time()

