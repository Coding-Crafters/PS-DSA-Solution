class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      
        next_non_zero = 0

        num_len = len(nums)
        for i in range(num_len):
            
            if nums[i] != 0:
                nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]
                next_non_zero += 1

        nums[next_non_zero:] = [0] * (num_len - next_non_zero)
