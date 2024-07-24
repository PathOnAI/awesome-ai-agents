def two_sum(nums, target):
    num_to_index = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        
        num_to_index[num] = index

    return []

if __name__ == "__main__":
    # Test cases
    print(two_sum([2, 7, 11, 15], 9))  # Expected output: [0, 1]
    print(two_sum([3, 2, 4], 6))       # Expected output: [1, 2]
    print(two_sum([3, 3], 6))          # Expected output: [0, 1]