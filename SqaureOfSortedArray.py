import time


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        start = time.time()

        '''
            These 2 lines for first 2 programs only
        '''

        # for i in range(0, len(nums)):
        #     nums[i] *= nums[i]

        '''
            For this program time is 6
        '''

        # for i in range(0, len(nums)):

        #     for j in range(len(nums)-i-1):
        #         if nums[j] > nums[j+1]:

        #             nums[j], nums[j+1] = nums[j+1], nums[j]

        # end = time.time()
        # print("Time: ", end-start)
        # return nums

        '''
            For this program time is 5
        '''
        # for j in range(1, len(nums)):
        #     key = nums[j]
        #     i = j - 1
        #     while i >= 0 and nums[i] > key:
        #         nums[i+1] = nums[i]
        #         i -= 1
        #     nums[i+1] = key

        # end = time.time()
        # print("Time: ", end-start)
        # return nums

        '''
            For this program time is 3.
        '''

        for i in range(len(nums)):
            nums[i] = (nums[i])**2

        end = time.time()
        print("Time: ", end-start)
        nums.sort()
        return nums

        '''
            For this Program time is 5.
        '''
        # i, j, n = 0, len(nums)-1, len(nums)-1
        # result = [0 for _ in range(len(nums))]
        # while n >= 0:
        #     if abs(nums[i]) > abs(nums[j]):
        #         result[n] = nums[i]**2
        #         i += 1
        #     else:
        #         result[n] = nums[j]**2
        #         j -= 1
        #     n -= 1

        # end = time.time()
        # print("Time: ", end-start)

        # return result


nums = [-4, -1, 0, 3, 10]
call = Solution()
print(call.sortedSquares(nums))
