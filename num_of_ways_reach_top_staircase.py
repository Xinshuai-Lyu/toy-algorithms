"""
 There exists a staircase with N steps, 
 and you can climb up either 1 or 2 steps at a time. 
 Given N, write a function that 
 returns the number of unique ways 
 you can climb the staircase. 
 The order of the steps matters.
 
 X: a set of positive integers 
 N: a staircase with N steps
 
 X=[1, 2]
 1 -> 1
 2 -> [1] + 1
 3 -> [2] + [1]
 4 -> [3] + [2]
 5 -> [4] + [3]
 6 -> [5] + [4]
 X=[2, 3]
 1 -> 0
 2 -> 1
 3 -> [1] + 1
 4 -> [2] + [1]
 5 -> [3] + [2]
 6 -> [4] + [3]
 7 -> [5] + [4]
"""

def num_of_ways_reach_top_staircase(X, N):
    memory = {}
    for i in range(1, N+1):
        num_of_ways = 0
        for x in X:
            if (i - x) in memory:
                num_of_ways += memory[i-x]
            elif i == x: 
                num_of_ways += 1
        memory[i] = num_of_ways
    return memory[N]
print(num_of_ways_reach_top_staircase([1, 2, 3], 4))
            
    
