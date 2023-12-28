class Solution:

    # Solution: Two Pointers

    def removeElement(self, nums: List[int], val: int) -> int:
        # i: store the index of the kept value
        i = 0
        
        for j in range(len(nums)):
            # if nums[j] != val, then it should be kept
            if nums[j] != val:

                # move the kept value to the front
                nums[i] = nums[j]
                i += 1

        return i