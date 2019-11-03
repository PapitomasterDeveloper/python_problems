# Note: Assume that all the numbers are two digit numbers.

# Sample Input
# 23,34,55

# Expected Output
# 553423

def create_largest_number(number_list):
    r = sorted(number_list, reverse=True)
    return int("".join(str(x) for x in r))
    #remove pass and write your logic here

number_list=[23,45,67]
#number_list=[10,20,32]
#number_list=[98,10,22]

largest_number=create_largest_number(number_list)
print(largest_number)
