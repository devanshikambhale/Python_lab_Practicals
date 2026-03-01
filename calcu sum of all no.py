#calculate sum of all numbers from 1 to a given number.
number=int(input("Enter a positive integer N: "))
if number<=0:
    print("Please enter a positive integer.")   
else:
    sum=0
    i =1
    while i <= number:
        sum += i
        i += 1
    print("The sum of integers from 1 to", number, "is:", sum)