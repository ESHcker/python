class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(0,length-(k%length)):
            nums.append(nums.pop(0))
