def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums[:] = nums[len(nums) - (k % len(nums)):] + nums[:len(nums) - (k % len(nums))]

def main ():
    nums = [1, 2, 3, 4, 5, 6]
    rotate(nums, 2)
    print(nums)