withdrawal_amount,balance_amount=map(float,input().split())
if (withdrawal_amount %5 == 0) and (withdrawal_amount+0.5<=balance_amount):
    balance_amount=balance_amount-(withdrawal_amount+0.5)
print(balance_amount)