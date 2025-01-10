
list1=input("Enter color for list1 separate by comma:")
list2=input("Enter color for list2 separate by comma:")
l1=list1.split(',')
l2=list2.split(',')
result=set(l1)-set(l2)
print(result)