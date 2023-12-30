                                #FORMAL(MANDATORY ARGUEMENTS)
#def add(a,b,c=0,d=0,e=0): #(a,b are mandatory and c=0,d=0,e=0 is default values)
#    return a+b+c+d+e
#out=add(1,4,6,8,0)
#print(out)


#def add(a,b,c=0):
#    print('a :-',a)
#    print('b :-',b)
#    print('c :-',c)
#out=add(a=2,b=3,4)       O/P: #SYNTAX ERROR:POSITIONAL ARGUEMEBNT FOLLOWS KEYWORD ARGUEMENT
#print(out)



#def add(a,b,c=0):
#   print('a :-',a)
#  print('b :-',b)
#    print('c :-',c)      #o/p  :TypeError: add() got multiple values for argument 'a'
#out=add(2,a=3,c=4)
#print(out)



                              #PACKING
#def add(*args):
 #   out=0
#    for i in args:
#        out+=i
#    return out
#res=add(3,9,3,667,5,99,65)       #OUTPUT:   851
#print(res)

                              #KEYWORD ARGUEMENTS   IN PACKING
#def add(*args,**kwargs):
#    print(args)
#    print(kwargs)            #OUTPUT:   {'a': 10}
#add(a=10)



#def add(a,*args,**kwargs):
#    print(a,args)               #OUTPUT:3 (5,)  {'b': 9}
#    print(kwargs)
#add(3,5,b=9)



                                     #UNPACKING
                                  #EXAMPLE:1


#def add(a,b,c):
#    print(a)                #OUTPUT:  3  5  9
#    print(b)
#    print(c)
#add(*[3,5,9])

                                   #EXAMPLE:2

#def add(a,b,c,D):
#    print(a) 
#    print(b)                  #OUTPUT: TypeError: add() missing 1 required positional argument: 'D'
#    print(c)
#add(*[3,5,9]) 

                                     #EXAMPLE:3

#def add(a,b,c):
#    print(a)
#    print(b)                     #OUTPUT  : b c  a
#    print(c)
#add(*{'b':34,'c':45,'a':33})

                                      #EXAMPLE:4


#def add(a,b,c):
#    print(a)
#    print(b)                     #OUTPUT  :  33  34  45
#    print(c)
#add(**{'b':34,'c':45,'a':33})



                                     #EXAMPLE:5


#def add(a,b,d):
#    print(a)
#    print(b)                     #OUTPUT  : TypeError: add() got an unexpected keyword argument 'c'
#    print(d)
#add(**{'b':34,'c':45,'a':33})


                                  #EXAMPLE:6

#i=1
#sum=0
#while i<=10:             #OUTPUT  :   55
#    sum=sum+i
#    i+=1
#print(sum)



                                     #RECURSION


                                      #EXAMPLE:1

#def sum(a,b):
#    if a==b:
#       return a                 #OUTPUT  :  55
#    return a+ sum(a+1,b)
#out=sum(1,10)
#print(out)

