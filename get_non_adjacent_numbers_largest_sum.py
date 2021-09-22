'''
Given a list of integers, write a function that returns the largest sum of non-adjacent 
numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] 
should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''
'''
[x1] => x1
[x1, x2] => x1; x2
[x1, x2, x3] =>x1; x2; x3; x1+x3;
[x1, x2, x3, x4] => x1; x2; x3; x1+x3; x4; x1+x4; x2+x4
[x1, x2, x3, x4, x5] => x1; x2; x3; x1+x3; x4; x1+x4; x2+x4; x5; x1+x5; x2+x5; x3+x5; x1+x3+x5
'''
def get_non_adjacent_numbers_largest_sum(L):
    last_last_largest_sum = None
    last_largest_sum = L[0]
    i = 1
    while i < len(L):
        # single largest sum
        single_largest_sum = L[i]
        # new largest sum
        if last_last_largest_sum:
            new_largest_sum = L[i] + last_last_largest_sum
        else:
            new_largest_sum = L[i]
        temp = last_largest_sum
        last_largest_sum = max(single_largest_sum, new_largest_sum, last_largest_sum)
        last_last_largest_sum = temp
        i += 1
    return new_largest_sum
assert(get_non_adjacent_numbers_largest_sum([2, 4, 6, 2, 5]) == 13)
assert(get_non_adjacent_numbers_largest_sum([5, 1, 1, 5]) == 10)
 


