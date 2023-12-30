                      #count   no of digits in string using functions
def count_digit():
    a=input('enter a character:- ')
    count=0
    for i in a:
        if '0'<i<'9':
         count+=1
    print(count)
count_digit()