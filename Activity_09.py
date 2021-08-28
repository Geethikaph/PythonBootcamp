l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

k= (l*l) + (b*b) + (h*h)
print(k)
vol= ((b*b)*(h*h))/k**(1/2)
print('Volume of tromboloid= ',format(vol,'0.3f'))
rad=((3*vol)/(4*(22/7)))**(1/3)
print('Radius of sphere= ',format(rad,'0.3f'))

