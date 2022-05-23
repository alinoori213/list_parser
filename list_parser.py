import math

def list_to_num(l):
    
    l = [2**x for x in l]
    l = sum(l)
    return l


def highest_power_of_two(n):
 
    p = int(math.log(n, 2));
    return int(pow(2, p));


def num_to_list(num):

    num = list_to_num(num)
    print(num)
    l = []
    while num != 0:
        highest = highest_power_of_two(num)
        l.append(highest)
        num = num - highest
    l.reverse()
    l = [int(math.log(x, 2)) for x in l]
    return l


l = [12,13,14,15]
print(num_to_list(l))


