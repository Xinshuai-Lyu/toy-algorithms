'''
Problem:

given an integer list L [x1, x2, x3, ..., xn], return a new list new_L that the i_th element value in new_L is the multiplication of all other elements in L except i_th element. You are not allowed to use division! Ex. L=[1,2,3], new_L=[6, 3, 2]. (Division has a problem when meeting zero)
'''

# tip1: Begin Brute Force Then ask should I optimize it.
# O(N^2)
def brute_force(L):
    new_L = []
    for i in range(len(L)):
        multiplication = 1
        for j in range(len(L)):
            if j != i:
                multiplication *= L[j]
        new_L.append(multiplication)
    return new_L

# tip2: During optimization, thinking about smaller problems to figure out a pattern.
'''
L = [x1, x2, x3]
new_L = [x2x3, x1x3, x1x2]
pattern: 
     x1 = 1*allrightelements

     x2 = allleftelements*allrightelements

     x3 = allleftelements*1

     x1_(1) -> x2_(x1*1) -> x3_(x2*x1*1)

     x1_(x2*x3*1) <- x2_(x3*1) <- x3_(1)
why I find this pattern: 70%Lucky + 20%Lucky + 10%Experience 
how to use this pattern: Add two list to store the pattern
'''
def smarter_solution(L):
    pattern_L1 = []
    pattern_L2 = []
    new_L = []
    multiplication = 1
    for i in range(len(L)):
        if i == 0:
            pattern_L1.append(multiplication)
        else:
            multiplication *= L[i-1]
            pattern_L1.append(multiplication)
    multiplication = 1
    for j in range(len(L)-1, -1, -1):
        if j == len(L)-1:
            pattern_L2.append(multiplication)
        else:
            multiplication *= L[j+1]
            pattern_L2.append(multiplication)
    for i in range(len(L)):
        new_L.append(pattern_L1[i] * pattern_L2[len(L) - i - 1])
    return new_L

from random import randint

def random_L():
    L = []
    for i in range(10):
        L.append(randint(1, 10))
    return L
    
def division_method(L):
    new_L = []
    multiplication = 1
    for element in L:
        multiplication *= element
    for element in L:
        new_L.append(multiplication/element)
    return new_L
    
def test(func, zero_compatibility=True):
    assert(func([1,2,3]) == [6, 3, 2])
    assert(func([1,1,1]) == [1, 1, 1])
    if zero_compatibility:
        assert(func([0,1,-1]) == [-1, 0, 0])
        R = random_L()
        assert(func(R) == division_method(R))
    assert(func([5,1,-1]) == [-1, -5, 5])

test(brute_force)
test(smarter_solution)
