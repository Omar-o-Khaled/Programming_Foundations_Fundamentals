def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance


current = withdraw_money(100, 80)

if(current <= 50):
    print("We need to make a deposit your balance =",current)
else: 
    print("Nothing to see here!")

