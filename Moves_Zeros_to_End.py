#moves zeros to end of array
#input_list=[1,3,0,5,0,7]
def move_zeros_end(input_list ):
    j=0
    for i in range(len(input_list)):
        if input_list[i]!=0:# non_element zeros  go irst
            input_list[j]=input_list[i]
            j+=1
    while j<len(input_list):#rest of the array is filled with zeros
        input_list[j]=0
        j+=1
    return input_list        
   
input_list = list(map(int,input("Enter the elements:").split()))
print(move_zeros_end(input_list))
