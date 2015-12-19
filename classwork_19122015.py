import random
l = [random.randint(0, 1000) for _ in range(100)]

def max_el(l):
    """
    >>>l = [1,2,3,4,8,6]
    >>>max_el(l)
    8
    """
    #if len(l) == 1:
    #    return l[0]
    first = l.__len__()-1
    second = l.__len__() - 2
    while len(l) > 1:
        if second < l.__len__():
            f = l[first]
            s = l[second]
        if f <= s:
            #print(l.__len__())
            #print(first)
            l.pop(first)
            first=l.__len__()-1
            second=l.__len__()-2
        else:
            l.pop(second)
            first=l.__len__()-1
            second=l.__len__()-2
    return l[0]
print(max_el(l))

l2 = [random.randint(0, 1000) for _ in range(100)]

def sum_el (l):
    """
    >>> l = [1,2,3,4,5]
    >>> sum_el(l)
    15
    """
    sum_ = 0
    for el in l:
        sum_ = sum_ + el
    return sum_
print(sum_el(l2))

def mul_el (l):
    """
    >>>l = [1,2,3]
    >>>mul_el(l)
    6
    """
    mul_ = 1
    for el in  l:
        mul_ = mul_*el
    return mul_
print(mul_el(l2))

