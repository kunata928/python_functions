import itertools

def rotate(self, nums: list, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

def findUnsortedSubarray(nums: list) -> int:
    if len(nums) < 2:
        return 0
    i = 1
    while i < len(nums) and nums[i - 1] < nums[i]:
        i += 1
    left, right = i - 1, i - 2
    while i < len(nums):
        for n in nums[left:i]:
            if nums[i] < n:
                right = i
                break
        i += 1
    return right - left + 1

def generatePermutations(array: list):
    permutations_object = itertools.permutations(list)
    permutations_list = list(permutations_object)
    print(permutations_list)

def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    count = 1
    maxC = 1
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            count += 1
        else:
            maxC = max(count, maxC)
            count = 1
    return max(maxC, count)

def multiplyElementsArray(nums):
    pre = [1] + [0] * len(nums)
    suf = [0] * len(nums) + [1]
    res = []
    for i in range(len(nums)):
        pre[i+1] = pre[i] * nums[i]
    for i in range(len(nums)-1, -1, -1):
        suf[i] = suf[i+1] * nums[i]
    for i in range(len(nums)):
        res.append(pre[i] * suf[i+1])
    return res

def countPrimes(n) -> int:
    count = []
    is_prime = [False, False] + [True] * (n - 1)
    for num in range(2, n):
        if is_prime[num]:
            count.append(num)
            for p in range(num, n, num):
                is_prime[p] = False
    return len(count)

if __name__ == "__main__":
    nums = [0]
    print(multiplyElementsArray(nums))
    ##print(findUnsortedSubarray(nums))
    ##generatePermutations(nums)