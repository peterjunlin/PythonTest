import calendar


def calendar1():
    c = calendar.Calendar()
    # first day of weekday
    print('First day of weekday is: ', calendar.firstweekday())
    # leap year
    y = 2000
    print('Is {0} a leap year: {1}'.format(y, calendar.isleap(y)))
    # leap years
    y1 = 1996
    y2 = 2017
    d = calendar.leapdays(y1, y2)
    print('Number of leap years between {0} and {1}: {2}'.format(y1, y2, d))
    # weekday of a date
    w = calendar.weekday(2017, 5, 28)
    print(calendar.day_name[w])
    # month
    print(calendar.month_name[1])
    # calendar weekday header
    print(calendar.weekheader(5))
    # weekday of the first day of a month, days in a month
    m = calendar.monthrange(2017, 5)
    print("(2017, 5) First day of the month is {0}. There are {1} days in this month".format(calendar.day_name[m[0]], m[1]))
    # Get month calendar as a matrix
    calendar.setfirstweekday(6)
    m = calendar.monthcalendar(2017, 5)
    print(m)
    # print month calendar
    calendar.prmonth(2017, 5)
    #
    m = calendar.month(2017, 5)
    print(m)
    # print year calendar
    calendar.prcal(2017)
    # get year calendar in a string array
    y = calendar.calendar(2017)
    print(y)
    # iterator of weekdays
    it = calendar.Calendar().iterweekdays()
    list1 = [s for s in it]
    print(list1)
    # iterator of days in a month
    it = calendar.Calendar().itermonthdates(2017, 5)
    # list1 = ['{0}/{1}'.format(s.month, s.day) for s in it]
    list1 = [s for s in it]
    print(list1)
    #
    m = calendar.Calendar().monthdatescalendar(2017,5)
    print(len(m), m)


def practice1():
    calendar1()
