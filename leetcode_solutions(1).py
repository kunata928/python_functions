import itertools
import math

def multiply1(num1, num2) -> str:
    res = str(int(num1) * int(num2))
    return res

def multiply2(num1: str, num2: str) -> str:
    if num1 == '0' or num2 == '0':
        return '0'
    num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
           '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    n1 = 0
    n2 = 0
    for n in num1:
        n1 = (n1 * 10) + num[n]
    for n in num2:
        n2 = (n2 * 10) + num[n]
    return str(n1 * n2)

def getPermutation1(n: int, k: int) -> str:
    arr = []
    for i in range(1, n+1):
        arr.append(str(i))
    perm_obj = itertools.permutations(arr)
    perm_list = list(perm_obj)
    return "".join(perm_list[k - 1])

def getPermutation2(n: int, k: int) -> str:
    nums = [str(num) for num in range(1, n+1)]
    fact = [1] * n
    for i in range(1, n):
        fact[i] = i * fact[i-1]
    k -= 1
    res = []
    for i in range(n, 0, -1):
        id = k // fact[i - 1]
        k -= id * fact[i - 1]
        res.append(nums.pop(id))
    return ''.join(res)

#nums '2'
#fact  1   1   2   6
#k     0
#res  1 3 4
#i     2
#id  = 1

if __name__ == "__main__":
    print(getPermutation2(4, 4))
    #print(multiply2('15', '15'))