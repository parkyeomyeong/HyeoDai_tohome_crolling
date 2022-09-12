import random


def make_random_num(range_num):
    random_number = random.randrange(0, range_num+1)
    return random_number


def make_random_num2(start, end):
    random_number = random.randrange(start, end)
    return random_number
