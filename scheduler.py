from time import sleep 

def scheduler(f, n):
    # transform n to milliseconds
    n = n / 1000
    sleep(n)
    f()
    
def f(): print(1)

import timeit
start = timeit.default_timer()
scheduler(f, 5000)
stop = timeit.default_timer()
print(f'time: {stop - start}')

