import datetime
import random


def make_random_date(range_day):
    delete_day = random.randrange(-range_day, 0)
    today = datetime.datetime.now()
    my_timedelta = datetime.timedelta(days=delete_day)

    random_date = today + my_timedelta
    return random_date.strftime("%Y-%m-%d")
