a='abc'
b='xyz'
c='123'
out=" "
for i,j,k in zip(a,b,c):                   # OUTPUT  : xaybzc
    out=out+i+j+k
print(out)