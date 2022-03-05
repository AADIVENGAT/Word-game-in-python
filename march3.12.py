#word game:
from random import shuffle
list = ['a','s','t','r','u','l']
shuffle(list)
print(list)
list_1=["star","str","url","sat","rat","tar"]
x=input("Enter value: ")
if(x == x in list_1):
    print("Word Found")
else:
    print("Word Not Found")


#word game:
from random import shuffle
list = ['a','s','t','r','u','l']
shuffle(list)
print(list)
list_1=["star","str","url","sat","rat","tar"]
count = 0
while(count<3):
   x=input("Enter value: ").lower().strip()
   if(x == x in list_1):
        print("Word Found")
   else:
        print("Word Not Found")    
   count+=1     
