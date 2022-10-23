class Solution:
    def moveZeroes(self, nums: list[int]) -> None:

        # Solution 1

        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        return nums

        # Solution 2

        # c = 0
        # x = len(nums)
        # if (x == 1):
        #     return nums
        # for i in range(x):
        #     if (nums[i] == 0 and i != x-1):
        #         nums[i-c] = nums[i+1]
        #         c += 1
        #         continue
        #     nums[i-c] = nums[i]
        # for i in range(x-c, x):
        #     nums[i] = 0

        # return nums


nums = [0, 1, 2, 0]
call = Solution()
print(call.moveZeroes(nums))
