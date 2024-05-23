
#get loan details
money_owned = float(input("how much money do you owe in dollars?\n")) #50,000
apr = float(input("what is the annual percentage rate of the loan?\n")) #3%
payment = float(input("how much will you pay each month in dollars?\n")) #1,000
months =  int(input("how many months do you want to see the results for?\n")) #24

monthly_rate = apr/100/12

for i in range(months):
    #calculate interest to pay
    interest_paid = money_owned*monthly_rate

    #add in interest
    money_owned = money_owned + interest_paid

    if(money_owned - payment < 0):
        print('The last payment is', money_owned)
        print('you paid off the loan in', i+1, 'months')
        break

    #make payment
    money_owned = money_owned - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest', end='')
    print ('now I owe', money_owned)