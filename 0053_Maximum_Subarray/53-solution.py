class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # define max_sum and current_sum
        # define max_sum as the first element in nums, because if you definr max_sum as 0,
        # it will return 0 if all elements in nums are negative
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            current_sum += num

            if current_sum > max_sum:
                max_sum = current_sum
                
            # if current_sum < 0, then there is no need to add the next element to current_sum
            if current_sum < 0:
                current_sum = 0

        return max_sum