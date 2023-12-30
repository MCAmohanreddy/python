                            #GLOBAL VARIABLE 
#a=10
#b=20
#def sample():
#    global a,b
#    print(b)

#    print(a)

#print(a)
#sample()
#print(a)

                           #LOCAL VARIABLE
#a=10
#def sample():
#   b=20
#    c=30
#    print(b,c)

#print(a)
#sample()
#print(b)
                        #
#a=10
#def outer():
#    b=20
#    print(b)#20
#    def inner():
#        nonlocal b
#        c=10
#        b=100
#        print(b)#20
#        print(c)#10
#    print(b)#20
#    inner()
#    print(b)#100

#outer()
