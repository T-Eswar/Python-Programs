#To find maximum element in the list .if list is empty then return -1 or any other value which is not present in the list
#input=[12,32,16,5,36,22]
#output=36
def find_max_element(input_list):
    max_element=0
    if not input_list:
        return -1
    max_element=input_list[0]
    for i in range(1,len(input_list)):
       
        if input_list[i]>max_element:
               max_element=input_list[i]
    return max_element           
input_list = list(map(int, input("Enter the elements separated by space: ").split()))
print(find_max_element(input_list))
