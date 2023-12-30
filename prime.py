num=int(input(' enter a number to check :- '))
i=1
temp=False
while i<=num:
    if num%i==0 and i!=1 and i!=num:
        temp=True

    i+=1
if not temp:
   print("it is prime number'")
else:
    print('it is not prime number')

