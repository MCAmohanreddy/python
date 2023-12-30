print('welcome to Book My Show')
name=input('enter your name :-  ')
c=int(input('select number of seats you want  :-  '))
category=int(input('please select 1----> diamond class 2 gold class 3 silver class'))
if  c==1:
    amount=c*200
elif c==2:
    amount=c*150
elif c==3:
    amount=c*100
print(f'hi{name}you have booked {c}amount is{amount}')
     





