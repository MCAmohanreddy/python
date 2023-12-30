                                #STORE INDEX VALUE IN VOWELS BY USING WHILE LOOP
a='aeiouasdfgbhZ mkjb'
def store(a):
    out=[]
    i=0
    while i<len(a):
        if a[i] in 'aeiouAEIOU':
            out=out+[i]
        i+=1
    return out
c=store(a)
print(c)