from bank import Account, Customer, Bank, BankException, InsufficientFundsException


def transfer_between_accounts(acc1, acc2):
    is_done = False
    while not is_done:
        try:
            print(f"Transfer from -> to: {acc1} -> {acc2}")
            transfer_amount_str = input('Enter transfer amount: ')
            transfer_amount = float(transfer_amount_str)
            bank.transfer_money(acc1,acc2,transfer_amount)
            is_done = True
        except ValueError as e:
            print(e)
            print('The amount provided is invalid')
        except BankException as e:
            print(e)
            return

'''
def withdraw_amount_from_input(acc):
    is_done = False
    while not is_done:
        try:
            print(f'You have: {acc.get_balance()} {acc.currency}')
            withdraw_amount_str = input('Enter withdraw amount: ')
            withdraw_amount = float(withdraw_amount_str)
            if withdraw_amount == 0:
                break
            Account.withdraw(withdraw_amount)
            is_done = True
        except InsufficientFundsException as e:
            print(e)
            print(f'req/avl: {e.amount_req}/{e.amount_avl}')
        except ValueError as e:
            print('The amount provided is invalid')
            # except:
            #    print('Error')
        except BankException as e:
            print(e)
'''

#Creating accounts for a showcase
bank = Bank('SGH')
c1 = bank.create_customer('Anne', 'Brown')
a1 = bank.create_account(c1)
a2 = bank.create_account(c1, currency='PLN')
c2 = bank.create_customer('John', 'Doe')
a3 = bank.create_account(c2, currency='EUR')
a4 = bank.create_account(c2, currency='JPY')
print(bank)
print('---- Operations ----')
# Setting opening balances for the accounts
#step 0
a1.deposit(1000,'USD')
a2.deposit(2000,'PLN')
a3.deposit(500,'EUR')
a4.deposit(100000,'JPY')

# Same-currency deposits, Step 1-2
a1.deposit(250,'USD')
a2.deposit(500,'PLN')

# Withdrawal - always same currency, Step 3-4
a1.withdraw(100,'USD')
a2.withdraw(300,'PLN')

# End of Day 1 - interest, Step 4.5
bank.run_daily_interest_updater()

# Different-currency deposits -> currency conversion, Step 5-7
# EUR->USD
a1.deposit(100,'EUR')
# PLN->EUR
a3.deposit(1000,'PLN')
# JPY->USD
a1.deposit(5000,'JPY')

# End of Day 2 - interest, Step 7.5
bank.run_daily_interest_updater()

# Transfers between currencies -> on input, Step 8-12
transfer_between_accounts(1001,1002) #200 USD->PLN
transfer_between_accounts(1003,1004) #100 EUR->JPY
transfer_between_accounts(1002,1003) #500 PLN->EUR
transfer_between_accounts(1004,1001) #10000 JPY->USD
transfer_between_accounts(1001,1004) #50 USD->JPY

# non-base conversion (deposit), Step 13
a2.deposit(200,'CAD') #CAD->PLN

# End of Day 3 - interest, Step 13.5
bank.run_daily_interest_updater()

# non-base conversion (deposit), Step 14
a1.deposit(300,'CZK') #CZK->USD

# withdrawal (again), Step 15-16
a4.withdraw(20000)
a3.withdraw(100)

# End of Day 4 - interest, Step 16.5
bank.run_daily_interest_updater()

# non-base conversion (again), Step 17
a3.deposit(150,'GBP') #GBP->EUR

# Transfer again, Step 18
transfer_between_accounts(1002,1001) #1000 PLN->USD

# End of Day 5 - interest, Step 18.5
bank.run_daily_interest_updater()

# Transaction report for USD account, Step 19
bank.transaction_report(1001)

# showcasing interest compounding - hence no other operations
# End of Day 8 - interest x3, Step 20
bank.run_daily_interest_updater()
bank.run_daily_interest_updater()
bank.run_daily_interest_updater()
print(bank)

#just not sure, why it sometimes breaks the rounding to 2 decimal places

#-----------------------------------------------------------------------------------------------

# Operations causing errors
# a1.withdraw(5000,'USD') # InsufficientFundsException
# a2.deposit(-50,'PLN') # InvalidAmountException
# a1.deposit(100,'BTC') #NonAvailableCurrencyException
# transfer_between_accounts(1001,9999) # f.e. 0 or -1 (printed) InvalidAmountException
                                       # or (if correct amount used)
                                       # InvalidAccountException (non-existing account error)
# transfer_between_accounts(1004,1002) # f.e. 500000, (printed) InsufficientFundsException,
                                       # should leave account and history/report unchanged
# transfer_between_accounts(1001, 1001) # (printed) InvalidAccountException (same account error)
# transfer_between_accounts(1001, 1002) # f.e. abc -> can't convert string to float

#------------------------------------------------------------------------------------------------







#withdraw_amount_from_input()
#try:
 #   a3.deposit(400)
  #  a3.withdraw(200)

    # a = 1414
    # b = '2545'
    # c = a + b
   # a1.deposit(200)
   # print(f'You have: {a1.get_balance()} {a1.currency}')
   # withdraw_amount_str = input('Enter withdraw amount: ')
   # withdraw_amount = float(withdraw_amount_str)
   # a1.withdraw(withdraw_amount)
    #a1.withdraw(100)
#except InsufficientFundsException as e:
#    print(e)
#    print(f'req/avl: {e.amount_req}/{e.amount_avl}')
#except ValueError as e:
#    print('The amount provided is invalid')
#except BankException as e:
#    print(e)
# except:
#    print('Error')
# except Exception as e:  # Don't use it as this will hide every error or bug
#     print(f'SEVERE error {e}')
#     raise e

import sys
#sys.exit(-1000)
