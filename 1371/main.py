print(ord('e'))
print(ord('e') ^ ord('e'))
word = "eleetminicoworoep"
wished_result = 13

def solution(s: str):
    number = 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    prefix_sum = [None] * len(s)
    vowels_hash_table = {
        "a": 0,
        "e": 1,
        "i": 2,
        "o": 3,
        "u": 4
    }
    vowels_list = [0] * 5
    # a - 0
    # e - 1
    # i - 2
    # o - 3
    # u - 4
    for index, char in enumerate(s):
        if char in vowels:
            vowels_list[vowels_hash_table[char]] += 1
        prefix_sum[index] = vowels_list.copy()
        print(prefix_sum)
    print(vowels_list)
    return number

print(solution(word))
assert solution(word) == wished_result