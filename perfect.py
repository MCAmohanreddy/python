a=int(input(' enter a number to check :- '))
out=0
for i in range(1,a):
 if a%i == 0:
    out=out+i
    
if out==a:
   print("it is perfect number'")
else:
    print('it is not perfect number')

