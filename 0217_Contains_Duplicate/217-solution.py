class Solution:

    # Solution 1: using set
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = []
        for i in range(len(nums)):
            if nums[i] not in store:
                store.append(nums[i])
            else:
                return True
        return False