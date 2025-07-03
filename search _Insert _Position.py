'''Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [1,3,5,6,7], target = 5
Output: 2
'''
def searchInsert(array, target):
    left=0
    right=len(array)-1
    while(left <=right):
        mid=(left+right)//2
        if(array[mid]==target):
            return mid
        elif target<array[mid]:
            right=mid-1
        else:
            left=mid+1
    return left    

array=list(map(int,input("Enter Elements:").split()))  
target=int(input("Enter Target Number"))  
print(searchInsert(array,target))