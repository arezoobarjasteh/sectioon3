import random
a=[]
lenght= int (input("enter lenght of array :"))
for i in range (lenght):
    NUMBER = int(input("Enter a numbers of arraye :"))
    a.append(NUMBER)
flag= True

for  i in range (len(a) -1 ) :
    if a[i] > a [i+1] :
        flag=False
        break
if flag:
    print ('sort')    
else :
    print("no sort")
print(a)    