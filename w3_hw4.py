unique_list = [1,2,3,3,3,4,5,5]
print("Input list  :", unique_list)
# Empty list
output_list = []
for i in unique_list:
    if i not in output_list:
        output_list.append(i) #add empty list
print("Output list :",output_list)