'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, tracking = 0):
    print(f"n is {n}")
    if n < 2:
        return 1

    num1 = 0

    for i in range(1, 4):
        if tracking + i == n:
            
            return num1 + 1
        elif tracking + i < n:
            num1 = eating_cookies(n, tracking + i)
    return num1

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
