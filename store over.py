number=input("Enter the numbers with space:")
num=[int(x) for x in number.split()]
result=['over' if x>100 else x for x in num]
print(result)