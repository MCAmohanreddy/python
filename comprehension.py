#a={i for i in range(1,10)}
#print(a)


#a=[i*i for i in range(11,20)]
#print(a)



#from math import factorial
#a=[factorial(i) for i in range(1,7)]
#print(a)



#a=["abcd",{1:2},[4,5,6],{4,7},(9,8,7)]
#a=[len(i) for i in a]
#print(a)



#a=[ i**3 for i in range(1,25) if i%3==0]
#print(a)



#b=([1,2,4,6],(1,2),{4,6,7},{2:1,4:2,1:3},'efgh')
#b=[len(i) for i in b]
#print(b)



#b=[i for i in range(1,100) if i%3==0 if i%2==0  if i%5==0]
#print(b)





#a=[i**2 if i%2==0  else i**3  for i in range(1,10)]
#print(a)


#a=[[i*j for j in range(1,11)]for i in [2,3,4]]
#print(a)



#a={ i:i*2  for i in range(1,5)}
#print(a)





#a='ABCDEF'
#a={j:i for i,j in enumerate(a) if i%2==0}
#print(a)

#seats=int(input('enter no of seats:- '))
#option=int(input('select 1->diamond 2-->silver 3-->gold'))
#match option:
#    case 1:
#        print("diamond class")
#        amount=seats*200
#    case 2:
#        print("silver class")
#        amount=seats*150
#    case 3:
#        print("gold class")
#        amount=seats*100
#    case  _:
#        print('invalid option')
#        amount=None
#print(amount)





#a=int(input('enter a number:- '))
#b=int(input('enter a number:- '))
#option=int(input('select1-->add 2-->sub 3-->mul'))
#match option:
#    case 1:
#        print('add class')
#         out=a+b
#    case 2:
#        print('sub class')
#        out=a-b
#    case 3:
#        print('mul class')
#print(out)




option=int(input('select 1-->red  2-->yellow  3-->green '))
match option:
    case 1:
        print('red')
        out=stop
    case 2:
        print('yellow')
        out=ready togo
    case 3:
        print('green')
        out=go
    print(out)

