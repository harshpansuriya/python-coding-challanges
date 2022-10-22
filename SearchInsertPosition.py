class main:

    def first(self, nums, target):

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1

            else:
                r = mid - 1

        return l


n = [1, 3, 5, 6]
target = 7
call = main()
print(call.first(n, target))
