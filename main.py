money = 1000.00

def interest(percent, orig):
    return orig * (percent / 100)


for i in range(25):
    balance = money + interest(money, 6.5)
    if i + 1 < 10:
        frontspace = '    '
    else:
        frontspace = '   '
    print(f'{i + 1}:{frontspace}current balence: {money}, intrest: {interest(6.5, money)}, deposit: 100, new balance: {balance}')
    money = balance + 100