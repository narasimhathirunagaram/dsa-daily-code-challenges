
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        min_len = len(nums)+1
        arr_sum = 0
        for right in range(len(nums)):
            arr_sum += nums[right]
            while arr_sum>=target:
                # print(arr_sum, target)
                min_len = min(min_len,right-left+1)
                arr_sum -= nums[left]
                left += 1
        return min_len if min_len!=len(nums)+1 else 0

if __name__ == '__main__':
    nums1, target1 = [2,3,1,2,4,3], 7
    nums2, target2 = [1,4,4], 4
    nums3, target3 = [1,1,1,1,1,1,1,1], 11
    sol = Solution()
    print(sol.minSubArrayLen(nums=nums1,target=target1))
    print(sol.minSubArrayLen(nums=nums2, target=target2))
    print(sol.minSubArrayLen(nums=nums3, target=target3))
