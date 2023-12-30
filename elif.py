
                             #TO CHECK LOWERCSA OR UPPER CASE LETTERS 


char=input('enter a character :-')
if 'A'<=char <='Z':
    print('it is an uppercase character')
elif 'a'<=char <='z':
    print(' it is an lowercase character')
elif '0' <=char <= '9':
    print('it is digit')
else:
    print('it is special character')
