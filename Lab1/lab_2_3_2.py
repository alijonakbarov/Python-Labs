print("Beginning")

a = int(input("Enter a: ")) #2
b = int(input("Enter b: ")) #1
c = int(input("Enter c: ")) #3

if a > b:
    max1 = a
else:
    max1 = b
    
print(f"btwn numbers {a} and {b} the greatest {max1}")

if b > c:
    max2 = b
else:
    max2 = c
    
print(f"btwn numbers {b} and {c} the greatest {max2}")  
 
print(f"Comparing numbers {max1} and {max2}")   

if max1 > max2:
    print(max1)
else:
    print(max2)

print("The end")
