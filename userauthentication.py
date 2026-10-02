name = 'admin'
password = 'pass123'
attempts = 3


while attempts > 0:
    name_input = input('please enter your name: ')
    if name_input == name :
        pass_input = input('please enter your password: ')
        if pass_input == password:
            print('login successful')
            
            break
        else:
            attempts = attempts - 1
            print(f'invalid password, please enter a valid password. remaining attempts: {attempts}')


    else:
        attempts = attempts - 1
        print(f'invalid name please enter a valid name. remaining attemps: {attempts}')
        
    if attempts == 0:
            print('account blocked')