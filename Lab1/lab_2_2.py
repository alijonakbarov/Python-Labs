a = int(input())
b = int(input())

if a == b:
    print("Two same numbers")
else:
    print("а < b or а > b")
    if a < b:
        print(a)
    else:
        print(b) 
    
print("The end")