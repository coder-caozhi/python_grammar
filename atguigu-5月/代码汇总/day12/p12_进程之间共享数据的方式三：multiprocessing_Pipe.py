"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
import random
from multiprocessing import current_process,Pipe,Process,Pool


#定义任务函数1：往里放数字。可以取对方的字母。
def put_num_get_letter(conn1):
    cp = current_process()
    for i in range(10):
        num = random.randint(1,100)
        conn1.send(num)
        print(f"{cp.name}放了数字：",num)
        letter = conn1.recv() #等着取，阻塞了
        print(f"{cp.name}获取了字母：{letter}")


#定义任务函数2：往里放字母。可以取对方的数字。
def put_letter_get_num(conn2):
    cp = current_process()
    for i in range(10):
        letter = chr(ord('a') + i)
        conn2.send(letter)
        print(f"{cp.name}放了字母：",letter)
        num = conn2.recv()
        print(f"{cp.name}获取了数字：{num}")

# if __name__ == "__main__":
#     pipe = Pipe()
#     conn1,conn2 = pipe
#     p1 = Process(target=put_num_get_letter,args=(conn1,))
#     p2 = Process(target=put_letter_get_num,args=(conn2,))
#     p1.start()
#     p2.start()

# if __name__ == "__main__":
#     pipe = Pipe()
#     conn1,conn2 = pipe
#     with Pool() as p:
#         p.apply(put_num_get_letter,args=(conn1,))
#         p.apply(put_letter_get_num,args=(conn2,))
#         #同步，一个任务执行时，另一个任务等待

if __name__ == "__main__":
    pipe = Pipe()
    conn1,conn2 = pipe
    with Pool() as p:
        p.apply_async(put_num_get_letter,args=(conn1,))
        p.apply_async(put_letter_get_num,args=(conn2,))
        #同步，一个任务执行时，另一个任务等待
        p.close()
        p.join()

