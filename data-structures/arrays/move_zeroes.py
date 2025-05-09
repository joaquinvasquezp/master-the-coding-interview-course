# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

# Follow up: Could you minimize the total number of operations done?

def move_zeroes(nums):
    idx = 0
    counter = 0

    while True:
        if nums[idx] == 0:
            nums.append(nums[idx])
            del nums[idx]
        else:
            idx += 1
        
        counter += 1

        if counter == len(nums):
            break

    return nums

# BEST SOLUTION O(N)
# def move_zeroes(nums):
#     slow = 0
#     for fast in range(len(nums)):
#         print(f'Slow: {slow}')
#         print(f'Fast: {fast}')
#         if nums[fast] != 0 and nums[slow] == 0:
#             nums[slow], nums[fast] = nums[fast], nums[slow]

#         # wait while we find a non-zero element to
#         # swap with you
#         if nums[slow] != 0:
#             slow += 1
    
#     return nums

input = [0,0,1]
result = move_zeroes(nums=input)
print(result)
