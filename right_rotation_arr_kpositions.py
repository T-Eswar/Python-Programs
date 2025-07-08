'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
'''
def reverse(arr,left,right):
    while left <= right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
      

def  rotate_array(arr,k):
    k=k%len(arr)
    reverse(arr, 0, len(arr) - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, len(arr) - 1)
    return arr    


arr=list(map(int,input("Enter the Array for rotational:- ").split()))
k=int(input("Enter the  k position :- "))
print(rotate_array(arr,k))