from multiprocessing import Process
import os

processes = []
num_processes = os.cpu_count()

print(num_processes)

def square_nums():
    for i in range(100):
        i*i

if __name__ == '__main__':
    #create process
    for i in range(num_processes):
        p = Process(target=square_nums)
        processes.append(p)

    #start process
    for p in processes:
        p.start()

    #join process
    for p in processes:
        p.join()


print("End of main")