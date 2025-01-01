str=input("enter string:")
if str[-3:]=='ing':
    str+='ly'
else:
    str+='ing'
print(str)