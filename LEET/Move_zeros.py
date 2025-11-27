class Solution:
    def moveZeroes(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0: #in 1st iteraation if the element in nums isnt equal to zero then copy it to the 0th position and increase the count by 1. 
                nums[count] = nums[i]
                count += 1
        for i in range(count, len(nums)): #the count was finished at 2 so from their 3rd and 4th indexes are replaced by 0s. 
            nums[i] = 0
            print(i)

obj1 = Solution()
obj1.moveZeroes([0,1,0,3,12])
