A = [66, 66, 66, 66, 66, 66, 66, 66, 66, 66]

def list_sum(A):
    list = A
    sum = 0
    
    for i in range(len(A)):       
        sum += A[i]
        
    print(f'As the result {sum}')
         
       
list_sum(A)

print("")
#
def zero_finder(A):
    zeroes = A.count(0)
    print(f'in the arrays  {zeroes} zeroes')  
zero_finder(A)
print()
#
def ladder(n):
        for i in range(n):
            for j in range(i+1):
                print(j + 1, end=' ')
            print()
ladder(5)
print()
#
def pyramid(n):
    
    for i in range(1, n + 1):
        for j in range(1, n + 1 - i):
            print(' ', end = ' ')
            
        for j in range(1, i + 1):
            print(j, end=' ')
            
        for j in range(i - 1, 0, -1):
            print(j, end=' ')
        print()
            
pyramid(5)