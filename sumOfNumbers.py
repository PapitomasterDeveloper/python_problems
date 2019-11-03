#Write a Python program to find the sum of digits of a given number. E.g. Sum of number 123 will be 6

def find_sum_of_digits(number):
    sum_of_digits=0
    l = list(str(number))
    #Write your logic here
    for i in range(0, len(l)):
        sum_of_digits += int(l[i])
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)

#sum_of_digits=find_sum_of_digits(78975)
#sum_of_digits=find_sum_of_digits(780)
#sum_of_digits=find_sum_of_digits(909)

print("Sum of digits:",sum_of_digits)
