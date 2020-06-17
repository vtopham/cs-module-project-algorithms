'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    print(f"n is {n}")
    #returns combinations
    def find_combination(n, combo = [], ways = []):
        #need a nullifying statement here
        if n < 2:
            ways.append(n)
        else:
            
            for i in range (1, n + 1):
                print(f"i is {i}, range is 1 to {n + 1}")
                print(f"The combo at the beginning is {combo}")
                
                #if we're returning, set combo back to be able to include the new value
                # while sum(combo) > n - i:
                #     combo.pop(-1)

                if i + sum(combo) == n:
                    #if our branch has resulted in a sum of n, return the combo
                    combo.append(i)
                    print(f"!!!!!!! combo is {combo}")
                    ways.append(combo)
                    #pop off the right answer
                    
                    #TODO: only set combo back the appropriate amount
                   
                    
                    # next
                elif i + sum(combo) < n:
                    #if we still haven't hit the number, run again
                    combo.append(i)
                    # print(f"combo is now {combo}")
                    
                    find_combination(n, combo, ways)
                
                
                
        # print(f"Ways is {len(ways)}")
        return ways
    
    answer = find_combination(n)
        

    return len(answer)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
