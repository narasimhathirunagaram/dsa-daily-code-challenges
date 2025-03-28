class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_cnt = 0
        left = 0
        zero_cnt = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1
            while zero_cnt>1 and left < right:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            max_cnt = max(max_cnt, right - left + 1)
        return max_cnt

if __name__ == '__main__':
    nums1 = [1,0,1,1,0]
    nums2 = [1,0,1,1,0,1]
    nums3 = [1, 0, 1, 1, 0, 1, 1]
    # nums3 = [0, 0, 0, 0, 0, 0, 0]
    sol = Solution()
    print(sol.findMaxConsecutiveOnes(nums=nums1))
    print(sol.findMaxConsecutiveOnes(nums2))
    print(sol.findMaxConsecutiveOnes(nums3))
