# 560. Subarray Sum Equals K

# Hint
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.



# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

def subarraySum(nums, k):
    cnt = 0
    sum = 0
    sum_count = {0:1}

    for num in nums:
        sum += num
        if (sum - k) in sum_count:
            cnt += sum_count[sum - k]
        if sum in sum_count:
            cnt += sum_count[sum]
        else:
            sum_count[sum] = 1

    return cnt

print(subarraySum([1,2,3],3))