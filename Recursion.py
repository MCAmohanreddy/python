
             #RECRSION
       # WAP TO ADD ALL THE VALUES IN GIVEN HOMOGENEOUS LIST USING RECURSION      



#a=[1,2]
#def add_int(a,i=0):
#    if len(a)-1==i:
#        return a[i]
#    return len(a)+add_int(a,i+1)
#out=add_int(a)
#print(out)




                 #RECURSION
               #FACTORIAL USING RECURSION

#a=[6]
#def fact(a,n=1):
#    if a==n:
#        return n              #OUTPUT  : 720
#    return n*fact(a,n+1)
#out=fact(6)
#print(out)


                    #LAMBDA FUNCTIONS/ANONYMOUS FUNCTIONS
       # SQUARE OF A NUMBER USING LAMBDA FUNCTIONS

#a=lambda x:x*x
#out=a(2)            #output  :  4
#print(out)

                     #LAMBDA FUNCTIONS
           #ADD OF TWO NUMBERS
#a=lambda x,y:x+y
#out=a(2,3)              #output  :  5
#print(out)





#a=(lambda st,ch:ch in st)
#out=a('salaar','l')            #output  :  if l is present TRUE otherwise FALSE will Printed
#print(out)

                          #LAMBDA FUNCTIONS
                 #TO CHECK GIVEN NUMBER IS DIVISIBLE BY 13 OR NOT

#a=lambda x:x%13==0
#out=a(52)                # OUTPUT   :  TRUE
#print(out)


                             ##GENERATORS
              #TO CHECK SQUARE OF A NUMBER AND TWICE

#def square(a,b):
#    for i in range(a,b+1):
#        yield i*2
#        yield i**2
#out=square(5,15)
#print(type(out))
#print(list(out))



