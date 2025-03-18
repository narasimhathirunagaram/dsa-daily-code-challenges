class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if k==1:
            return 0
        nums.sort()
        min_diff = nums[-1]
        for i in range(len(nums)-k+1):
            diff = nums[i+k-1] - nums[i]
            min_diff = min(diff,min_diff)
        return min_diff

if __name__ == '__main__':
    nums1,k1 = [90],1
    nums2,k2 = [9,4,1,7],2
    sol = Solution()
    print(sol.minimumDifference(nums1,k1))
    print(sol.minimumDifference(nums2,k2))