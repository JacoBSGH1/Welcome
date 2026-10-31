import os
rates_file = os.path.join('..', 'data', 'rates.csv')

with open(rates_file, 'r') as f:
    next(f)
    rates_dict = {}
    for line in f:
        # currency, value = str.strip(str(line)).strip().split(',')
        currency, value = line.strip().split(',')
        rates_dict[currency] = float(value)

print(rates_dict)

# check
a = 100
print(round(100*rates_dict['PLN']/rates_dict['EUR'],2))

#how to do it quickly - Pandas
import pandas as pd

df = pd.read_csv(rates_file)
print(df.head())

df_cur = df.set_index('Currency')
print(df_cur['Value'])

rates = df_cur['Value'].to_dict()
print(rates)
print(rates['PLN'] * rates['EUR'])
