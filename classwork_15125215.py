#print([chr(i) for  i in range(128) if chr(i).isalpha()])
#import string
#print([chr(i) for  i in range(128) if chr(i) in string.ascii_letters or chr(i).isdigit()])
#print([chr(i) for  i in range(999)])

import random
l= [random.randint(0,1000) for _ in range (100)]
def my_sort(l):
    """
    >>> e = [random.randint(0,1000) for _ in range (100)]
    >>> my_list = my_sort(l)
    >>> py_sorted = sorted(l)
    >>>my_list == py_sorted
    True
    """
#s = True
first = 0
second = 1
n = True
k=0
while True:

    if second < l.__len__():
        print(second)
        f = l[first]
        s = l[second]
        if f < s:
            first+=1
            second+=1
        else:
            l[first] = s
            l[second] = f
            first+=1
            second+=1
            n=True
    else:
        first = 0
        second =1
        n=False





print(l)
print(l==sorted(l))














