class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a dictionary to store the number and its index
        num_dict = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in num_dict:
                return [num_dict[diff], i]
            num_dict[val] = i
            # Very important! The structure of the dictionary is {number: index}
            # Because we need to return the index instead of the number
        return []