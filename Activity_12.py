def main():
    a,b,c=input_numbers()
    largest=compare(a,b,c)
    display(largest,a,b,c)
   
def compare(a, b, c):
   if (a >= b) and (a >= c): 
       largest = a 
   elif (b >= a) and (b >= c):
       largest = b 
   else:
       largest = c 
   return largest

def display(largest,a,b,c):
    print("{0} is the largest among {1},{2},{3}".format(largest,a,b,c))
    
    
def input_numbers():
        a,b,c=input("Enter three numbers: ").split()
        a,b,c=[int(a),int(b),int(c)]
        return a,b,c
       
main()
