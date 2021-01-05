def callback_1():
    # Reference to a lambda function
    print('Reference to a lambda function')
    f = lambda x: x*2
    print('f(3)={0}'.format(f(3)))
    # map function
    print('Map function:')
    list1 = [i for i in range(0, 10)]
    t = map(lambda x: x*2, list1)
    r = [i for i in t]
    print(r)

def practice_1():
    callback_1()
