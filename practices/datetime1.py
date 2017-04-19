from datetime import timedelta

def datetime_functions():
    pass

def timedelta_functions():
    dt1 = timedelta(seconds=-1)
    print(dt1.days, dt1.seconds, dt1.microseconds)

def practice1():
    print(dir(timedelta))
    timedelta_functions()
