def rotate(self, nums: list, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]