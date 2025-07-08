'''Given an integer n, return the number of prime numbers that are strictly less than n.
Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
'''
def primes_number_steive(num):
    is_prime=[True]*num  #put the all vales as True
    is_prime[0]=is_prime[1]=False # put 0,1 is not primes and put as false
    for i in range(2,int(num**0.5)+1):#start for loop from 2 to sqrt of num +1
        if is_prime[i]:
            for j in range(i*i,num,i):# thsis logic return the i multipication values as false
                is_prime[j]=False
    primes=[]
    count=0            
    for i,val in enumerate(is_prime):# to print primes numbers
        if val:
            primes.append(i)
            count+=1
    return f"primes{primes} and count {count}" 
        

num=int(input("Enter the number"))
print(primes_number_steive(num))
