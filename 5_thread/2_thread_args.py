import threading
import time
# 带有参数的任务
def task(count):
    for i in range(count):
        print("任务执⾏中..")
        time.sleep(0.2)
    else:
        print("任务执⾏完成")
if __name__ == '__main__':
 # 创建⼦线程
 # args: 以元组的⽅式给任务传⼊参数
    sub_thread = threading.Thread(target=task, args=(5,))
    sub_thread.start()