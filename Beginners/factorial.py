# Factorial using recursion
def factorial(n):
    return 1 if(n==1 or n==0) else n*factorial(n-1)

print(factorial(3))

# Take a look at the iterative process

def facto(n):
    if(n<0):
        return 0
    elif n==0 or n==1:
        return 1
    else :
        fct = 1
        while(n>1):
            fct *=n
            n-=1
        return fct

facto(3)