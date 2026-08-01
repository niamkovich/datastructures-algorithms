def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test Case 1
nums = [2, 2, 1]
print(singleNumber(nums))   # Output: 1

# Test Case 2
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))   # Output: 4

# Test Case 3
nums = [1]
print(singleNumber(nums))   # Output: 1

# Test Case 4
nums = [7, 3, 5, 4, 5, 3, 4]
print(singleNumber(nums))   # Output: 7