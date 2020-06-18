'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    
    # Working code#########
    single = []
   
    for x in arr:
        
        in_single_index = None
        for i in range(0, len(single)):
            # print(f"i is {i}, length of single is {len(single)}")
            if single[i] == x:
                #if the value is already in single, remove it
                in_single_index = i
                next
        if in_single_index == None:
            #if the value wasn't in single, add it
            single.append(x) 
        else:
            #if it was in the array, pop it out
            single.pop(in_single_index)
    
    return single[0]


    ######OLD CODE########
    # if len(arr) == 1:
    #     return arr[0]

    # for i in range(0,len(arr)):
    #     for j in range(i+1,len(arr)):
    #         if arr[i] == arr[j]:
    #             item = arr[i]
    #             arr.remove(item)
    #             arr.remove(item)
    #             return single_number(arr)
    
    ##########WORKS FOR 100#######


    # if len(arr) == 1:
    #     return arr[0]
    
    # for i in range(0,len(arr)):
    #     for j in range(i+1,len(arr)):
    #         if arr[i] == arr[j]:
    #             item = arr[i]
    #             arr.remove(item)
    #             arr.remove(item)
    #             return single_number(arr)
    
    

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


