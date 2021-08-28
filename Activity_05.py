var = input("Enter five numbers : ")
numbers  = var.split()
sum = 0
for num in numbers:
    sum += int (num)
print("Sum of all the numbers is = ", sum)
