# The problem is, given a list [x1, x2, ..., xn], return whether there are two elements whose summation equals k. For example, given [1, 2, 3, 4], k = 3, because 1 + 2 == 3, return True.

# Brute force method
# Time Complexity O(n^2)
# Space Complexity O(1)
def brute_force(L, k):
    # i points a member in L
    for i in range(len(L)):
        # j points another member except the member pointed by i
        for j in range(i+1, len(L)):
            if L[i] + L[j] == k: return True
    return False
    
# Hashmap based method
# Time Complexity O(n)
# Space Complexity O(n)
def hashmap_based_method(L, k):
    dict_for_L = {}
    for i, x in enumerate(L):
        # x as a unique key
        if x in dict_for_L:
            dict_for_L[x] += 1
        else:
            dict_for_L[x] = 1
    for i, x1 in enumerate(L):
        # x1 + x2 = k
        # Just ask whether x2 as a key in dict_for_L and
        # make sure x2 is not x1 or the same key contains
        # at least 2 elements
        x2 = k - x1
        if x2 in dict_for_L and (x2 != x1 or dict_for_L[x2] > 1):
            return True
    return False
    
# Method based on sorted list
def merge(left_list, right_list):
    L = []
    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] >= right_list[j]:
            L.append(right_list[j])
            j += 1
        else:
            L.append(left_list[i])
            i += 1
    L.extend(left_list[i:])
    L.extend(right_list[j:])
    return L
def merge_sort(L, i, j):
    if i >= j:
        return [L[i]]
    middle = (i + j) // 2
    left_list = merge_sort(L, i, middle)
    right_list = merge_sort(L, middle+1, j)
    sorted_list = merge(left_list, right_list)
    return sorted_list
    
# Time complexity O(nlogn)
# Space complexity O(n)
def sorted_list_method(L, k):
    # See it as a matrix consists of two Ls, each cell
    # value equals the summation of L_coloum_i + L_row_j
    # for all i,j belons to 0 to len(L) - 1
    '''
      1,2,3,4,5
    1 2 3 4
    2
    3
    4
    5 6
    '''
    L = merge_sort(L, 0, len(L) - 1)
    start_column = len(L) - 1
    start_row = 0
    while start_column > -1 and start_row < len(L):
        summation = L[start_column] + L[start_row]
        if summation == k and start_column != start_row:
            return True
        elif summation > k:
            start_column -= 1
        else:
            start_row += 1
    return False
        


from random import randint
L1 = []
L2 = []
L3 = [1,2,3,4,5,6]
L4 = [-100,1,2,3,4,5,6,1000]
for i in range(100):
    L1.append(randint(1, 100))
    L2.append(randint(-50, 100))
assert(brute_force(L1, -4) == False)
assert(brute_force(L2, 1000) == False)
assert(brute_force(L3, 11) == True)
assert(brute_force(L3, 12) == False)
assert(brute_force(L4, -99) == True)

assert(hashmap_based_method(L1, -4) == False)
assert(hashmap_based_method(L2, 1000) == False)
assert(hashmap_based_method(L3, 11) == True)
assert(hashmap_based_method(L3, 12) == False)
assert(hashmap_based_method(L4, -99) == True)

assert(sorted_list_method(L1, -4) == False)
assert(sorted_list_method(L2, 1000) == False)
assert(sorted_list_method(L3, 11) == True)
assert(sorted_list_method(L3, 12) == False)
assert(sorted_list_method(L4, -99) == True)


