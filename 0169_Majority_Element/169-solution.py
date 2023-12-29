class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        max_time = len(nums) // 2
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
        for key, value in m.items():
            if value > max_time:
                return key
        return 0