import timeit

def get_count_of_decode_ways1(encoded_str):
    if len(encoded_str) <= 1:
      return 1
    lack1 = get_count_of_decode_ways1(encoded_str[:-1])
    if (int(encoded_str[-1]) + 10*int(encoded_str[-2])) <= 26:
      lack2 = get_count_of_decode_ways1(encoded_str[:-2])
    else:
      lack2= 0
    result = lack1+ lack2

    return result

memory = {}
def get_count_of_decode_ways2(encoded_str):
    global memory
    if len(encoded_str) <= 1:
        return 1
    if encoded_str[:-1] in memory:
        lack1 = memory[encoded_str[:-1]]
    else:
        lack1 = get_count_of_decode_ways2(encoded_str[:-1])
        memory[encoded_str[:-1]] = lack1
    if (int(encoded_str[-1]) + 10*int(encoded_str[-2])) <= 26:
        if encoded_str[:-2] in memory:
            lack2 = memory[encoded_str[:-2]]
        else:
            lack2 = get_count_of_decode_ways2(encoded_str[:-2])
            memory[encoded_str[:-2]] = lack2
    else:
        lack2 = 0
    result = lack1 + lack2
    return result
    
def get_running_time(func, *args):
    start = timeit.default_timer()
    print(func(*args))
    stop = timeit.default_timer()
    print('Time: ', stop - start)  

get_running_time(get_count_of_decode_ways1, "1111")
get_running_time(get_count_of_decode_ways2, "1111")

