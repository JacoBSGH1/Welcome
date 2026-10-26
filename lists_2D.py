# lists inside a list etc. nested way
# points = [[1,2],
  #        [4,5],
   #       [7,8]] #nested list

points = [[1,2,5],
          [4,5,4],
          [7,8,8]]

print(points)
el_5 = points[1][1]
print(el_5)
print(type(points)) #these are still lists
print(type(points[2]))

#for r in points:
#    print(r)
#    for c in r:
#        print(c)

print('sum_rows')
def sum_rows(my_list):
    sum_rows = []
    for r in my_list:
        row_sum = 0
        for c in r:
            row_sum += c
        sum_rows.append(row_sum)
    return sum_rows
print(sum_rows(points))

print('sum_columns') # not my solution, one of possibilities
def sum_columns(my_list):
    rows = len(my_list)
    cols = len(my_list[0])
    sum_cols = [0] * cols
    for c in range(cols):
        for r in range(rows):
            sum_cols[c] += my_list[r][c]
    return sum_cols
print(sum_columns(points))

print('sum_list')
def sum_list(my_list):
    sum_list = 0
    for r in my_list:
        for c in r:
            sum_list += c
    return sum_list

# the same thing to sum all
print(sum_list(points))
print(sum(sum_rows(points)))
print(sum(sum_columns(points)))

cur = ['USD', 'EUR', 'PLN']
rates = [3.8, 4.3, 1.0]

rates_list = list(zip(cur, rates)) #zip takes the elements of both lists and
# combines them into tuples alongside indexes
# it DOES NOT generate the list object, but allows us to work on it as if we did generate it (?)
print(rates_list)

for cur, rate in zip(cur, rates):
    print(f'{cur} -> {rate}')

currencies_rates = list(zip(*rates_list)) # unzip into a list
print(currencies_rates)

l_a = [1,2,3]
l_b = [3*x for x in l_a if x>1] # conditions inside a list
print(l_b)

print('-'*60)

def sum_rows_single_line(my_list): # with usage of conditions inside a list - look above
    return [sum(row) for row in my_list]

def sum_cols_zip(my_list):
    unzip_cols = list(zip(*my_list))
    print(unzip_cols)
    return sum_rows_single_line(zip(*my_list))

print(f'sum_rows_single_line: {sum_rows_single_line(points)}')
print(f'sum_cols_zip: {sum_cols_zip(points)}') #zip transposes the matrix???

