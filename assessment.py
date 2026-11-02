min_vent_amount = 1000
unit_amount = 300

while True:
    try:
        recharge_amount = int(input('Please enter your vent amount: '))
        if recharge_amount >= min_vent_amount:
            total_token = recharge_amount / unit_amount
            print(f'your vent unit(s) is: {total_token:.2f}')
            break
        else: 
            print('input from 1000 and above')
    except ValueError:
        print('input a valid amount')

    







