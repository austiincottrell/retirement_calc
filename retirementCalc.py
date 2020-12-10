#Calculator to figure out how much expontential money you will make when retired

import locale
locale.setlocale(locale.LC_ALL, 'en_US')

def total_capital():
    print("Let's figure out how much money you will get when you retire!")
    print("Let's start out with your capital investment.")

    return int(input('How much capital do you have to invest now: '))

def years_to_months():
    return int(input('How many years till you retire: ')) * 12 

def exponential_rate():
    return float(input('How much interest do you expect your money to make yearly on your return: '))

def deposit():
    return int(input('How much money are you putting aside monthly for your retirement: '))

def years_to_deposit():
    return int(input('How many years do you plan to keep putting money aside: ') )


def retirement_calc(capital,months,exponential,monthlyDeposit,depositYearly):
    my_list = [num for num in range(0,months+1)]
    exponential = exponential / 12
    depositMonths = depositYearly * 12

    for _ in my_list:
        capital = (capital * exponential) + capital # Interest baring
        depositMonths = depositMonths - 1 # Once we hit 0 and below we no longer add in monthly Deposit
        if depositMonths >= 0:
            capital = capital + monthlyDeposit
        elif depositMonths < 0:
            pass

    return capital


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


#Calling the function 
results = retirement_calc(total_capital(),years_to_months(),exponential_rate(),deposit(),years_to_deposit())
print("Total retirement fund: " + locale.format_string("%d",truncate(results,2), grouping=True))
