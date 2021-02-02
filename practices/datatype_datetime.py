import datetime
from datetime import timedelta


def datetime_initialization():
    dt = datetime.date(2017, 5, 30)
    assert dt.strftime("%m/%d/%Y") == "05/30/2017"

    tm = datetime.time(23, 0, 0)
    assert tm.strftime("%H:%M:%S") == "23:00:00"


def datetime_current_time():
    dt1 = datetime.date.today()


def datetime_properties():
    dt1 = datetime.datetime(2017, 5, 30, 10, 20, 30, 0)
    dt2 = datetime.datetime(2018, 1, 20, 10, 20, 30, 0)

    # datetime properties
    assert dt1.min == datetime.datetime(1, 1, 1, 0, 0, 0)
    assert dt1.max == datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
    assert dt1.year == 2017
    assert dt1.month == 5
    assert dt1.day == 30
    assert dt1.weekday() == 1  # Tuesday

    # change date
    dt3 = dt1.replace(year=2016)
    assert dt3.strftime("%m/%d/%Y") == "05/30/2016"
    assert dt1.strftime("%m/%d/%Y") == "05/30/2017"  # dt1 didn't change


def datetime_calculation():
    dt1 = datetime.datetime(2017, 5, 30, 10, 20, 30, 0)
    dt2 = datetime.datetime(2018, 1, 20, 10, 20, 30, 0)

    # comparison
    assert dt2 > dt1


def datetime_timedelta():
    dt1 = datetime.datetime(2017, 5, 29, 10, 0, 0)
    dt2 = datetime.datetime(2017, 5, 29, 13, 10, 0)

    # timedelta initialization
    delta1 = timedelta(seconds=-1)
    assert delta1.total_seconds() == -1.0

    # get time delta from subtraction of two datetime
    delta1 = dt2 - dt1
    assert delta1.total_seconds() == (3 * 60 + 10) * 60


if __name__ == "__main__":
    datetime_initialization()
    datetime_current_time()
    datetime_properties()
    datetime_calculation()
    datetime_timedelta()
