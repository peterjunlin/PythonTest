import re

def practice1():
    print(">>>")
    pattern = '\w+ly'
    re1 = re.compile(pattern)
    str1 = 'hello world! carefully to watch, and wonderfully to perform'
    result = re1.findall(str1)
    print("re.findall")
    print("---")
    print(pattern)
    print(str1)
    print("---")
    if result is None:
        print('no match')
    else:
        print(result)
