class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        min_len = len(nums)+1
        sum_arr = 0
        for right in range(len(nums)):
            sum_arr += nums[right]
            while sum_arr>=target:
                min_len = min(min_len,right-left+1)
                sum_arr -= nums[left]
                left += 1
        return min_len if min_len!=len(nums)+1 else 0
        
if __name__ == '__main__':
    nums1, target1 = [2,3,1,2,4,3], 7
    nums2, target2 = [1,4,4], 4
    nums3, target3 = [1,1,1,1,1,1,1,1], 11
    nums4, target4 = [12,28,83,4,25,26,25,2,25,25,25,12], 213
    sol = Solution()
    print(sol.minSubArrayLen(target1,nums1))
    print(sol.minSubArrayLen(target2,nums2))
    print(sol.minSubArrayLen(target3,nums3))
    print(sol.minSubArrayLen(target4,nums4))