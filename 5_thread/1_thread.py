import threading
import time

def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)

def dance():
 # 扩展： 获取当前线程
 # print("dance当前执⾏的线程为：", threading.current_threa
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)

if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing)
    # 创建跳舞的线程
    dance_thread = threading.Thread(target=dance)
    # 开启线程
    sing_thread.start()
    dance_thread.start()