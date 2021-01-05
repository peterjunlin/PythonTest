import datetime
from datetime import timedelta

def date_1():
    print('------date-------')
    dt2 = datetime.date(2017, 5, 30)
    print(dt2)
    # get current date
    dt1 = datetime.date.today()
    print('get current date', dt1)
    # date properties
    print('date range: {0}, {1}'.format(dt1.min, dt1.max))
    print('date resolution: {0}'.format(datetime.date.resolution))
    print('year: {0}, month {1}, day {2}'.format(dt1.year, dt1.month, dt1.day))
    print('weekday: {0}'.format(dt1.weekday()))
    # comparison
    tf = dt2 > dt1
    print('{0} > {1} is {2}'.format(dt2, dt1, tf))
    tf = dt2 == dt1
    print('{0} == {1} is {2}'.format(dt2, dt1, tf))
    # change date
    dt3 = dt1.replace(year=2016)
    print(dt3)
    # convert to time.struct_time
    print(dt1.timetuple())
    #
    print(dt1.toordinal())
    #
    print(dt1.isoweekday())
    #
    print(dt1.isocalendar())
    #
    print(dt1.isoformat())
    print(dt1)
    #
    print(dt1.strftime('%A %x'))

def time_1():
    print('------time-------')
    tm1 = datetime.time(23, 0, 0)
    print(tm1)

def datetime_1():
    print('------datetime-------')
    dt1 = datetime.datetime(2017, 5, 29, 23, 0, 0)
    print(dt1)

def timedelta_1():
    print('------timedelta-------')
    # declare timedelta object
    dt1 = timedelta(seconds=-1)
    print('declare timedelta object: ', dt1)
    # timedelta properties
    print('timedelta properties: {0} days, {1} seconds, {2} microseconds'.format(dt1.days, dt1.seconds, dt1.microseconds))
    print('Resolution: {0}'.format(timedelta.resolution))
    print('Range min: {0}\nRange max: {1}'.format(timedelta.min, timedelta.max))
    print('Total seconds: {0}'.format(dt1.total_seconds()))
    # difference between two datetime objects
    dt1 = datetime.datetime(2017, 5, 29, 10, 0, 0)
    dt2 = datetime.datetime(2017, 5, 29, 13, 10, 0)
    d1 = dt2 - dt1
    print('{0} - {1} = {2}'.format(dt2, dt1, d1))

def practice1():
    date_1()
    # time_1()
    # datetime_1()
    # timedelta_1()
