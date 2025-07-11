


#to find unique vale sum in given array
#input=[1,2,3,3,2,5,6] output=12

def unique_sum(arry):
    dic={}
    total=0
    for item in arry:
        if item in dic:
            dic[item]+=1
        else:
            dic[item]=1

    for item,val in dic.items():
        if val==1:
            total=total+item
    return total
arry=list(map(int,input("enter the number").split()))
print(unique_sum(arry))          



