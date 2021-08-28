list_num = [int(num) for num in input("Enter five numbers : ").split()]
fthree = list_num[:3]
print("Sliced list is : ", fthree)
list_num[0] = list_num[4]=fthree[0] = fthree[2]= 0
print("replaced list-1 : ",list_num)
print("replaced list-2 : ",fthree)

#challenge
reverse_list = list_num[::-1]
print("reverse list", reverse_list)
