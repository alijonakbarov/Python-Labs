print("Beginning")

a = int(input("a = ")) #2
b = int(input("b = ")) #1
c = int(input("c = ")) #3

if a > b:
    print("END of code block for true expression")
    print("a is greater than b comparing with C")
    if a > c:
        print("а-the greatest")
        print(a)
    else:
        print("с-the greatest")
        print(c)
    print("END of code block for true expression")
else:
    print("END of code block for false expression")
    print("b greater than a comparing with C")
    if b > c:
        print("b-the greatest")
        print(b)
    else:
        print("с-the greatest")
        print(c)
    print("END of code block for false expression")

print("The end")
