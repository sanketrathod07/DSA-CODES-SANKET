# 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

# Follow up:

# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# def rotate(nums, k):
#     k = k % len(nums)  # This handles cases where k > len(nums)
#     nums[:] = nums[-k:] + nums[:-k]  # Slice the list to rotate
#     return nums

# print(rotate([1,2,3,4,5,6,7],3))

# def rotate(nums, k):
#     k = k % len(nums)  # Handle cases where k > len(nums)

#     # Reverse the entire list
#     nums.reverse()
#     # Reverse the first k elements
#     nums[:k] = reversed(nums[:k])
#     # Reverse the rest
#     nums[k:] = reversed(nums[k:])
    
#     return nums

# print(rotate([1, 2, 3, 4, 5, 6, 7], 3))


def rotate(nums, k):
    k = k % len(nums)

    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

    return nums

print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
# Output: [5,6,7,1,2,3,4]