#Leetcode 658

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # mn = min(range(len(arr)), key=lambda i: abs(arr[i] - x)) 
        # print(mn)
        sub_arr = [abs(i-x) for i in arr]
        lngt = len(arr)
        # print(sub_arr)
        mn_idx = sub_arr.index(min(sub_arr))
        left_avail = mn_idx
        right_avail = lngt - left_avail - 1
        print("Available: ",left_avail, right_avail)
        print(mn_idx)
        if k//2 < left_avail:
            left_use = k//2
        else:
            left_use = left_avail
        left_idx = mn_idx - left_use
        right_use = k-left_use-1
        print(left_use,right_use)
        

            # print(before)
        # print(arr[before_index:before_index+k])
        return arr[left_idx:left_idx+k]



if __name__ == '__main__':
    arr,k,x = [1,2,3,4,5], 4, 3
    sol = Solution()
    print(sol.findClosestElements(arr,k,x))