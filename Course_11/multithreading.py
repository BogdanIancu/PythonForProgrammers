import threading
import time


def thread_function():
    time.sleep(2)
    print("Hello from another thread!")


result = 0


def do_sum(a, b):
    global result
    time.sleep(2)
    result = a + b


t1 = threading.Thread(group=None, target=thread_function)

t1.start()
print("Message from main")
t1.join()

t2 = threading.Thread(target=do_sum, args=(4, 5))
t2.start()
t2.join()
print(result)


class MyThread(threading.Thread):
    def run(self):
        print("Hello World 2!")


t3 = MyThread()
t3.start()

print("Main ended")
