def two_sum(nums, target):
    # Create a dictionary to store the indices of the elements
    num_to_index = {}
    
    # Iterate over the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in num_to_index:
            # If found, return the indices of the current number and its complement
            return [num_to_index[complement], i]
        
        # If not found, add the current number and its index to the dictionary
        num_to_index[num] = i

    # If no solution is found, return an empty list (this line should never be reached in this problem)
    return []

# Test cases
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]
    assert two_sum([4, 6, 10, 12], 16) == [2, 3]
    print("All tests passed.")

test_two_sum()
