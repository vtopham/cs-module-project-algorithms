'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    # When you encounter a 0, remove it and move it to the end. if that happens, keep the tracking index the same as another element has shifted to take its place
    i = 0
    stop_index = len(arr)
    while i < stop_index:
        if arr[i] == 0:
            arr.append(arr.pop(i))
            #we don't want to infinite loop!
            stop_index -= 1
        else:
            i+= 1
    print(arr)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")