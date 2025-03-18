def product_array_except_self(nums):
    n = len(nums)
    result = [1]*n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for j in range(n-1,-1,-1):
        result[j] *= suffix
        suffix *= nums[j]
    return result

nums1 = [1,2,3,4]
nums2 = [-1,1,0,-3,3]
print(product_array_except_self(nums1))
print(product_array_except_self(nums2))
