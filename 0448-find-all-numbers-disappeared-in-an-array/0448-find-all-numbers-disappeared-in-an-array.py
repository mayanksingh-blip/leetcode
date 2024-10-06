class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        presence = [False] * (n+1)
        for num in nums:
            presence[num] = True
        missing_numbers = [i for i in range(1, n + 1) if not presence[i]]
        return missing_numbers     

        