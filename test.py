import math
def my_function(arg):
    # write the body of your function here

    def is_valid(c):
        return (ord(c.lower()) > 96 and ord(c.lower()) < 123)

    def add(dic, s):
        if s:
            if s not in dic:
                dic[s] = 1
            else:
                dic[s] += 1

    def symbol_embedded_in_word(string, symbol_idx):
        return symbol_idx < len(string)-1 and symbol_idx > 0 \
               and is_valid(string[index+1]) and is_valid(string[index-1])

    dictionary = {}
    current_word = ''

    for index, c in enumerate(arg):
        if is_valid(c):
            current_word += c.lower()
        else:
            if c == ' ':
                add(dictionary, current_word)
                current_word = ''
            elif symbol_embedded_in_word(arg, index):
                current_word += c.lower()
            else:
                add(dictionary, current_word)
                current_word = ''

    if current_word:
        add(dictionary, current_word)

    print(str(dictionary))
    return 'running with %s' % arg


def my_func(string, index):
    # write the body of your function here
    counter = 0

    for c in string[index:]:
        if c == ')':
            counter -= 1
            if counter == 0:
                print(index)
        if c == '(':
            counter += 1
        index += 1

    return 'running with %s' % ''.join(string)


def mult(nums):
    # write the body of your function here
    if len(nums) == 0: return nums

    left_and_right = [1] * len(nums)
    acc = 1
    for i in xrange(1, len(nums)):
        acc *= nums[i - 1]
        left_and_right[i] = acc
    print(left_and_right)
    acc = 1
    for i in range(len(nums)-2, -1, -1):
        print(i)
        acc *= nums[i + 1]
        left_and_right[i] *= acc

    print(left_and_right)
    return 'running with %s' % nums


def solution(nums, N):
    if not nums: return -1

    lefts = [0] * N
    acc = 0
    for i in xrange(1, N):
        acc += nums[i-1]
        lefts[i] = acc

    acc = 0
    i = N - 2
    while i >= 0:
        acc += nums[i+1]
        lefts[i] -= acc
        i -= 1

    for i in range(N):
        if lefts[i] == 0:
            return i
    return -1

# print(solution([-1,3,-4,5,1,-6,2,1], 8))
# print(solution([], 0))
# print(solution([1], 1))
# print(solution([1, 2, 3, -2, -1], 5))

# def solution(S):
#
#     S = S.replace('.', ':').replace('!', ':').replace('?', ':')
#     strings = S.split(':')
#     strings = [string.strip(' ').split(' ') for string in strings]
#     strings = [len([s for s in string if len(s) > 0]) for string in strings]
#
#     print(max(strings))
#
#
# print(solution("We test coders. Give us a try?"))
# print(solution("Forget  CVs..Save time . x x"))


def solution(A, B):
    # write your code in Python 2.7


    if B < 0 or A == B:
        return 0

    res = 0

    n = A
    while n <= B:
        n += 2*math.sqrt(n) + 1
        res += 1

    return res

print(solution(4, 36))

#
# # run your function through some test cases here
# # remember: debugging is half the battle!
# print mult([1,7,3,4])
#
# # run your function through some test cases here
# # remember: debugging is half the battle!
# print my_func('Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.', 10)
#
#
# # run your function through some test cases here
# # remember: debugging is half the battle!
# print my_function("We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake.")
