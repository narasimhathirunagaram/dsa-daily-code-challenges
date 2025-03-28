# Leetcode 80 https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

from collections import Counter

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cnt = dict(Counter(nums))
        d = {k:v-2 for k,v in dict(Counter(nums)).items() if v>2}
        for i in nums:
            if i in d:
                while d[i]!=0:
                    nums.remove(i)
                    d[i] -= 1
                    print(i,' removed')
        return None

if __name__ == '__main__':
    # nums = [1,1,1,2,2,3]
    nums = [0,0,1,1,1,1,2,3,3]
    sol = Solution()
    print(sol.removeDuplicates(nums))