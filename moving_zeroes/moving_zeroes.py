'''
Input: a List of integers
Returns: a List of integers
'''

 #You don't have to subtract 1, range already does not include the upper limit as it's starting from 0

def moving_zeroes(arr):
    #Solution for james carpino
    #1. The return statement will always execute after the first non-zero element it incounters. oh no! Move this after the for loop.
    #2. Now that we're looping more than once... but we're actually missing the last element. You don't have to subtract 1, range already does not include the upper limit as it's starting from 0.
    #3. I already increments. you do not neeed to increment it!
    #4 i is the index, not the value. the index of the value of 0 will not always be 0! So don't insert it lol and don't evaluate by it in your if statement
    #5. Python's list insert inserts the item at that index, and shifts all elements after it to the right. You want to append to the end
    #6. Now you've got a problem where whenever you pop, you're actually shifting the rest of the elements DOWN and therefore skipping the next one. Let's use a while loop instead to track how many elements we've evalueated so we can track index separately.
     
    print("New test")

    elem = 0
    i = 0
    while elem < len(arr):
        elem += 1
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
        else:
            i += 1
        print(arr)     
    
    return arr
    
    #######WORKING SOLUTION##############
    # # When you encounter a 0, remove it and move it to the end. if that happens, keep the tracking index the same as another element has shifted to take its place
    # i = 0
    # stop_index = len(arr)
    # while i < stop_index:
    #     if arr[i] == 0:
    #         arr.append(arr.pop(i))
    #         #we don't want to infinite loop!
    #         stop_index -= 1
    #     else:
    #         i+= 1
    # # print(arr)
    # return arr
    #################


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")