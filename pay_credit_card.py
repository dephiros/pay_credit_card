from itertools import count
credit_cards = []
for i in count():
    available_credit = float(raw_input("account {} total credit: ".format(i)))
    current_balance = float(raw_input("account {} current balance: ".format(i)))
    credit_cards.append((available_credit, current_balance))
    cont = raw_input("type n/no if no more account: ")
    if cont.lower().strip() in ['no', 'n']:
        break
cash = float(raw_input("how much do you have available to pay: "))
credit_ratios = [c/a for a, c in credit_cards]
credit_ratios_sum = sum(credit_ratios)
# normalize each ratio
payments = []
for i, credit_ratio in enumerate(credit_ratios):
    payment = (credit_ratio / credit_ratios_sum) * cash
    if payment > credit_cards[i][1]:
        payment = credit_cards[i][1]
    payments.append(payment)
# print in format creditcard: payment
for i, payment in enumerate(payments):
    print "{}:{}: {payment:.2f}".format(i, credit_cards[i], payment=payments[i])
