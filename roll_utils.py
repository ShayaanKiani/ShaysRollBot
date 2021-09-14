import random


def d6():
    return random.randint(1, 6)


def four_d6_d1():
    array = [d6(), d6(), d6(), d6()]
    lowest = array[0]
    index = 0
    count = 0

    for roll in array:
        if roll < lowest:
            lowest = roll
            index = count
        count += 1
    array.pop(index)

    print(sum(array))
    return sum(array)


def roll_stats():
    return "{}, {}, {}, {}, {}, {}".format(
        str(four_d6_d1()),
        str(four_d6_d1()),
        str(four_d6_d1()),
        str(four_d6_d1()),
        str(four_d6_d1()),
        str(four_d6_d1()),
    )
