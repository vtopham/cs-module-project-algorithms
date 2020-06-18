#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

ItemExp = namedtuple('Item', ['index', 'size', 'value', 'ratio'])





def knapsack_solver(items, capacity):
  #first let's add the ratio to our tuple so we can have easy access
  new_arr = []
  for x in items:
    ratio = x[2] / x[1]
    new_arr.append(ItemExp(x[0], x[1], x[2], ratio))
  
  
  #x[0] is index, x[1] is size, x[2] is value, x[3] is the ratio
  #to make things even easier, let's now sort our items array high to low by the ratio
  
  #helper function
  def find_ratio(x):
    return x[3]

  sorted_items = sorted(new_arr, key = find_ratio, reverse = True)
  
  #okay let's fill our napsack! If the item fits we'll put it in, and if not we'll chuck it out

  weight = 0
  value = 0
  knapsack = []

  while len(sorted_items) > 0 and weight < capacity:
    item = sorted_items[0]
    
    if item[1] + weight <= capacity:
      #if it fits, add it!
      knapsack.append(item[0])
      weight += item[1]
      value += item[2]
    
    #either way, we'll pop it off
    sorted_items.pop(0)

  knapsack.sort()
  return {'Value': value, 'Chosen': knapsack}

  




####################GOOD SOLUTION
#x[0] is index, x[1] is size, x[2] is value
#ratio is value over size like dollars a pound 
#     weight = 0
#     knapsack = []
#     value = 0
    
#     #as long as we still have items to pack or our bag has room
#     while weight < capacity and len(items) > 0:
#       max_ratio = 0
#       max_item = ""
      
#       #go through each item
#       for x in range(0, len(items)):
#         cur_item = items[x]
#         cur_ratio = cur_item[2] / cur_item[1] 
#         if cur_ratio > max_ratio:
#           #if this item has the better ratio, earmark it
#           max_ratio = cur_ratio
#           max_item = cur_item
#           index = x
#       #Once you've gone through all the items, see if the max ratio will fit
#       print(f"max item is {max_item}")
#       if max_item[1] + weight <= capacity:
#         #it fits so let's add it to our bag
#         weight += max_item[1]
#         knapsack.append(max_item[0])
#         value += max_item[2]
        
#       #whether we've added it to our bag or not we'll add it to our array
#       items.pop(index)
      
    
#     knapsack.sort()
#     return {'Value': value, 'Chosen': knapsack}


  ######################################################


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')