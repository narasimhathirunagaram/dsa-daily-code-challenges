class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        max_gap = 0
        nums.sort()
        for i in range(len(nums)-1):
            diff = nums[i+1]-nums[i]
            max_gap = max(max_gap,diff)
        return max_gap
    
if __name__ == '__main__':
    sol = Solution()
    nums = [3,6,9,1]
    print(sol.maximumGap(nums=nums))