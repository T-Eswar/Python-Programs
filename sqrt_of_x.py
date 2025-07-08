'''Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.'''
#input:-150000 output:-387
def sqrt_of_x(x):
    start=1
    end=x
    ans=0
    if x==0 or x==1:
        return x
    while start<=end:
        mid=start+(end-start)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            start=mid+1
            ans=mid
        else:
            end=mid-1
            
    return ans           
            
x=int(input("Enter the number:"))
print(sqrt_of_x(x))
