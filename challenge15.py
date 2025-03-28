# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
        return False

if __name__ == '__main__':
    nums1 = [2,3,1,1,4]
    nums2 = [3,2,1,0,4]
    sol = Solution()
    print(sol.canJump(nums1))   
    print(sol.canJump(nums2))     
