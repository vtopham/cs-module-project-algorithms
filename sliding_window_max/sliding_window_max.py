'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    windows = []
    if len(nums) <= k:
        windows.append(max(nums))
    
    #The number of iterations is always length - (k - 1)
    
    else: 
        for i in range(0, len(nums) - (k - 1)):
            #each range is i + k - 1
            max_in_window = max(nums[i:i + k])
            windows.append(max_in_window)

    return windows


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
