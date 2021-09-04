def find_lowest_missing_positive1(L):
    lowest_missing_positive = 1
    while True:
        if lowest_missing_positive not in L:
            return lowest_missing_positive 
        lowest_missing_positive += 1

def find_lowest_missing_positive2(L):
    L_set = set()
    for x in L:
        L_set.add(x)
    lowest_missing_positive = 1
    while True:
        if lowest_missing_positive not in L_set:
            return lowest_missing_positive 
        lowest_missing_positive += 1

def find_lowest_missing_positive3(L):
    L.sort()
    max_number = len(L)
    i = 0
    while i < len(L):
        if L[i] <= 0 or L[i] > max_number:
            L[i] = 0
        i += 1
    i = 0
    while i < len(L):
        x = L[i]
        L[i] = 0
        if x > 0 and L[x-1] != x:
            L[x-1] = x
        i += 1
    i = 0
    while i < len(L):
        if L[i] == 0:
            return i + 1
        i += 1
    return i + 1

def find_lowest_missing_positive4(L):
    max_number = len(L)
    i = 0
    while i < len(L):
        if L[i] <= 0 or L[i] > max_number:
            L[i] = 0
        i += 1
    temp = None
    i = 0
    def insert(L, i=None, x=None):
        if i != None:
            x = L[i]
        temp = L[x-1]
        if i != None:
            L[i] = 0
        if temp == x:
            return False
        L[x-1] = x
        return temp
    while i < len(L):
        if L[i] > 0 and L[i] != i+1:
            x_need_to_be_moved_to_temp = insert(L, i=i)
            if not x_need_to_be_moved_to_temp: continue
            while temp and temp != x_need_to_be_moved_to_temp and x_need_to_be_moved_to_temp:
                the_second_x_need_to_be_moved_to_temp = insert(L, x=temp)
                temp = x_need_to_be_moved_to_temp
                x_need_to_be_moved_to_temp = the_second_x_need_to_be_moved_to_temp
            if not temp:
                temp = x_need_to_be_moved_to_temp
        i += 1
    if temp:
        L[temp - 1] = temp
    i = 0
    while i < len(L):
        if L[i] == 0: return i+1
        i += 1
    return i + 1            

L = [1,432,52,646,-1,54,-5346,0,0,2134,1,2,3,7,42,]
assert(find_lowest_missing_positive2(L) == find_lowest_missing_positive1(L))   
assert(find_lowest_missing_positive3(L) == find_lowest_missing_positive1(L))   
assert(find_lowest_missing_positive4(L) == find_lowest_missing_positive1(L)) 
from random import randint
L = []
for i in range(100):
    i = randint(-100, 100)
    L.append(i)
assert(find_lowest_missing_positive2(L) == find_lowest_missing_positive1(L))   
assert(find_lowest_missing_positive3(L) == find_lowest_missing_positive1(L))   
assert(find_lowest_missing_positive4(L) == find_lowest_missing_positive1(L))
                

