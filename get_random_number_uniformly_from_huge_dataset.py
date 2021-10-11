# """
# Given a stream of elements too large to store in memory, 
# pick a random element from the stream with uniform probability.
# """
from random import randint
# element is uniformly picked
# https://www.dailycodingproblem.com/blog/how-to-pick-a-random-element-from-an-infinite-stream/
def get_random_element_uniformly_from_huge_dataset(L):
    i = 0
    while True:
        try:
            if i == 0:
                # [0,0] uniformly
                random_number = L[i]
            else:
                # [0...i] uniformly
                if randint(0, i) == 0:
                    random_number = L[i]
            i += 1
        except: break
    return random_number
    
d = {}
for i in range(7):
    d[i+1] = 0
for i in range(10000):
    d[get_random_element_uniformly_from_huge_dataset([1,2,3,4,5,6,7])] += 1
print(d)
