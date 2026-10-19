arr_a = [3, 5, 7, 9, 5, 9] # this is a list (python arrays are lists)
for i in arr_a:
    print(i, end=' ')
print(arr_a[2])

#arr_a.remove(7)
#print(arr_a)

print('\n'+'-'*80)
print('sets')
set_a = set(arr_a)
for i in set_a:
    print(i, end=' ') # prints only unique values, has no indexing - no order
    # print(set_a[2]) will give you an error

print('\n'+'-'*80)
set_b = set_a.copy()
set_b.remove(9)

print(set_b)

print('\n'+'-'*80)
list_a = list(set_a) #turning set into a list
print(list_a)
print(list_a[2])
list_a.append(8)
print(list_a)

list_a.insert(2,100)
list_a.remove(8)
print(list_a)

#remove 2nd element
list_a.pop(1)
print(list_a)

print('\n'+'-'*80)
t_1 = (2,56,86) #this is a tuple, works similar to list, but 1 major difference
print(t_1) #you can add and remove items from sets and lists, but NOT from tuples,
# they are immutable
print(type(t_1))
# unlike sets, tuples have indexed elements
print(t_1[2])