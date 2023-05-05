list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(list)

import random

def shuffle(list, n):
    for i in range(n-1, 0, -1):
        a = random.randint(0, i +1)
        list[i], list[a] = list[a], list[i]
    return list 

print(list)
print(shuffle(list, n))
print(shuffle(list,n))
print(shuffle(list,n))
