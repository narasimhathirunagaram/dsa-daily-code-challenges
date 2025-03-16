def start_end_position(nums,target):
    start, end = -1, -1
    for i, num in enumerate(nums):
        if num == target:
            if start == -1:
                start = i
            end = i
    return [start,end]

nums1,target1 = [5,7,7,8,8,10], 8
nums2, target2 = [5,7,7,8,8,10], 6
nums3, target3 = [], 0

print(start_end_position(nums1,target1))
print(start_end_position(nums2,target2))
print(start_end_position(nums3,target3))

'''
import bisect

def start_end_position(nums, target):
    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target) - 1  # Last occurrence

    if left < len(nums) and nums[left] == target:
        return [left, right]
    return [-1, -1]  # Target not found

# Example usage
nums1, target1 = [5, 7, 7, 8, 8, 8, 10], 8
nums2, target2 = [5, 7, 7, 8, 8, 10], 6
nums3, target3 = [], 0

print(start_end_position(nums1, target1))  # Output: [3, 5]
print(start_end_position(nums2, target2))  # Output: [-1, -1]
print(start_end_position(nums3, target3))  # Output: [-1, -1]
'''