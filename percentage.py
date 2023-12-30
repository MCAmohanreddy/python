marks=float(input('enter marks'))
if marks>=90 and marks<100:
    print('A+')
elif marks>=80 and marks<90:
    print('A')
elif marks>=70 and marks<80:
    print('B')
elif marks>=60 and marks<70:
    print('C')
elif marks>=35 and marks<60:
    print('pass')
elif marks>0 and marks<35:
    print('debar')
else:
    print('fail')