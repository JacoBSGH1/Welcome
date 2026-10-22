import os
rates_file = os.path.join('..', 'data', 'rates.csv')

with open(rates_file, 'r') as f:
    next(f)
    rates_dict = {}
    for line in f:
        currency, value = str.strip(str(line)).strip().split(',')
        rates_dict[currency] = float(value)

print(rates_dict)

