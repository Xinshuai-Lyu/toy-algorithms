"""
 Given an integer k and a string s, 
 find the length of the longest substring 
 that contains at most k distinct characters.
 
 For example, given s = "abcba" and k = 2, 
 the longest substring with k distinct characters is "bcb".
 
 k: an integer
 s: a string
"""
#O(N^2)
def get_longest_substring_with_k_distinct_characters_1(k, s):
    i = 0
    longest_i = 0
    longest_j = 0
    unique_letters = []
    while i < len(s):
        j = i 
        while j < len(s):
            if s[j] not in unique_letters:
                if len(unique_letters) == k:
                    unique_letters = []
                    break
                unique_letters.append(s[j])
            j += 1
        if j - i > longest_j - longest_i + 1:
            longest_i = i
            longest_j = j - 1
        i += 1
    return s[longest_i:longest_j+1]
# O(N)
def get_longest_substring_with_k_distinct_characters_2(k, s):
    # window
    N = 256
    window = []
    for i in range(N):
        window.append(0)
    # initialization
    start = 0
    longest_start = 0
    longest_end = -1
    unique_characters_n = 0
    # for loop
    i = 0
    while i < len(s):
        if window[ord(s[i])] == 0: # unique character
            unique_characters_n += 1
        window[ord(s[i])] += 1
        if unique_characters_n > k:
            while start < len(s):
                window[ord(s[start])] -= 1
                if window[ord(s[start])] == 0:
                    unique_characters_n -= 1
                    break
                start += 1
            start += 1
        if i - start > longest_end - longest_start:
            longest_start = start
            longest_end = i
        i += 1
    return s[longest_start: longest_end+1]
            
s = "cdsadasccccaffrtytyyytrytrytryt" 
k = 6

print(get_longest_substring_with_k_distinct_characters_1(k, s))
print(get_longest_substring_with_k_distinct_characters_2(k, s))
