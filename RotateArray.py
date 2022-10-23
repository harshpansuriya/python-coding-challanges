class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        a = nums.copy()
        n = len(nums)

        for i in range(0, n):
            j = (i+k) % n
            print(j)
            nums[j] = a[i]
            print(nums)

        return nums


nums = [1, 2, 3, 4]
k = 2
call = Solution()
print(call.rotate(nums, k))
