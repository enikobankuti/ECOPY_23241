# 1., Írjon egy függvényt ami vissza adja a bemeneti lista páros elemeit
# függvény név: evens_from_list
# bemeneti paraméterek: input_list
# kimeneti típus: List
#
def evens_from_list(input_list):
    e = list()
    for i in input_list:
        if i % 2 == 0:
            e.append(i)
    return e


#
# 2., Írjon egy függvényt ami megvizsgálja, hogy a listában minden elem páratlan-e
# függvény név: every_element_is_odd
# bemeneti paraméterek: input_list
# kimeneti típus: bool

def every_element_is_odd(input_list):
    for i in input_list:
        if i % 2 == 0:
            return False
    return True


# 3., Írjon egy függvényt ami visszaadja a k. legnagyobb elemet listában
# függvény név: kth_largest_in_list
# bemeneti paraméterek: input_list, kth_largest
# kimeneti típus: int

def kth_largest_in_list(input_list, kth_largest):
    return sorted(input_list)[kth_largest]


# 4., Írjon egy függvényt ami kiszámítja a lista elemek gördülő átlagát
# függvény név: cumavg_list
# bemeneti paraméterek: input_list
# kimeneti típus: List

def cumavg_list(input_list):
    new = []
    avg = []
    for i in range(0, len(input_list)):
        new.append(input_list[i])
        avg.append(sum(new) / len(new))
    return avg


# 5., Írjon egy függvényt ami kiszámítja 2 lista elemenként vett szorzatát
# függvény név: element_wise_multiplication
# bemeneti paraméterek: input_list1, input_list2
# kimeneti típus: List

def element_wise_multiplication(input_list1, input_list2):
    new = []
    for i in range(0, len(input_list1)):
        new.append(input_list1[i] * input_list2[i])
    return new


# 6., Írjon egy függvényt amely összekapcsol n listát 1 listába
# függvény név: merge_lists
# bemeneti paraméterek: *lists
# kimeneti típus: List

def merge_lists(*list):
    result = []
    for i in list:
        result = result + i
    return result


# 7., Írjon egy függvényt amely visszaadja a lista páratlan elemeinek a négyzetét
# függvény név: squared_odds
# bemeneti paraméterek: input_list
# kimeneti típus: List

def squared_odds(input_list):
    new = []
    for i in input_list:
        if i % 2 == 1:
            new.append(i * i)
    return new


# 8., Írjon egy függvényt amely a fordítottan sorba rendezi a kulcs-érték párokat a kulcs értéke szerint egy dictionary-ben
# függvény név: reverse_sort_by_key
# bemeneti paraméterek: input_dict
# kimeneti típus: Dict

def reverse_sort_by_key_old(input_dict):
    reversed_dict = {}
    while input_dict:
        key, value = input_dict.popitem()
        reversed_dict[key] = value
    return reversed_dict


def reverse_sort_by_key(input_dict):
    keys = reversed(sorted(input_dict))
    reversed_dict = {}
    for i in keys:
        reversed_dict[i] = input_dict[i]
    return reversed_dict


# 9., Írjon egy függvényt amely a bemeneti, pozitív egész számokat tartalmazó listát kiválogatja 2-vel, 5-el, 2-vel és 5-el, és egyikkel sem osztható számokat, és visszaad egy olyan dictionary-t, amelyben a kulcsok a 'by_two', 'by_five', 'by_two_and_five', és a 'by_none', az értékek, pedig a listák. (2 pont)
# függvény név: sort_list_by_divisibility
# bemeneti paraméterek: input_list
# kimeneti típus: Dict

def sort_list_by_divisibility(input_list):
    by_two = []
    by_five = []
    by_two_and_five = []
    by_none = []

    for i in input_list:
        if i % 10 == 0:
            by_two_and_five.append(i)
        elif i % 5 == 0:
            by_five.append(i)
        elif i % 2 == 0:
            by_two.append(i)
        else:
            by_none.append(i)
    return {'by_two': by_two, "by_five": by_five, "by_two_and_five": by_two_and_five, "by_none": by_none}
