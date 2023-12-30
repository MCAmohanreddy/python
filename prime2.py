num=int(input(' enter a number to check :- '))
i=1
count=0
while i<=num:
    if num%i==0 and i!=0 and i!=num:
        count+=1

    i+=1
if count==2:
   print('it is prime number')
else:
    print('it is not prime number')

