# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

# def majorityElement(nums):
#     majority = {}

#     for num in nums:
#         if num in majority:
#             majority[num] += 1
#         else:
#             majority[num] = 1

#     for key , val in majority.items():
#         if val > len(nums)// 2:
#             return key


def majorityElement(nums):
    a=nums[0]
    x=0
    for i in nums:
        if i==a:
            x+=1
        else:
            x-=1
        if x==0:
            a=i
            x+=1
    return a


print(majorityElement([2,3,3,2,1,3,1,1,3,1,2,2,3,1]))