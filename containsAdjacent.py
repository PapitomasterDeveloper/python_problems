# Given a list of integer values. 
# Write a python program to check whether it contains same number in adjacent position. 
# Display the count of such adjacent occurrences

# Sample Input

# Expected Output

# [1,1,5,100,-20,-20,6,0,0]

# 3

# [10,20,30,40,30,20]

# 0

# [1,2,2,3,4,4,4,10]

# 3

def get_count(num_list):
    count = 0

    # Write your logic here
    # for i in range(0, len(num_list) - 1):
    #   print(num_list[i] == num_list[i + 1])
    #   if(num_list[i] == num_list[i + 1]):
    #     count += 1
    # return count
    
    for i in range(0, len(num_list)):
      if(len(num_list) != i + 1):
        if(num_list[i] == num_list[i + 1]):
          count += 1
    print(count)

#provide different values in list and test your program
num_list=[1,1,5,100,-20,-20,6,0,0]
#num_list=[2, 4, 1, 6, 9]
print(get_count(num_list))
