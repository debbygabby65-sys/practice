def withdraw_money(balance, amount):
    if balance or withdrawal_amount == "nagetive":
        return "Invalid amount"
    elif withdrawal_amount == 0:
        return "Enter an amount greater than zero"
    elif withdrawal_amount > balance:
        return "Insufficient funds"
    else:
        new_balance = withdrawal_amount - balance
        return new_balance

name = 