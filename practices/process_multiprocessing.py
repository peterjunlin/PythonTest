from multiprocessing import Pool
import os
import time


def process_info():
    # Number of CPU
    print("\n\nProcess info:")
    print("Number of CPU: {0}".format(os.cpu_count()))
    print("Process ID: {0}".format(os.getpid()))
    print("Parent process ID: {0}".format(os.getppid()))


def f(x):
    print(os.getpid())
    time.sleep(1)
    return x*x


def process_multiprocessing():
    with Pool(os.cpu_count()) as p:
        r = p.map(f, [x for x in range(0, 100)])
        print(r)


if __name__ == '__main__':
    process_info()
    process_multiprocessing()
