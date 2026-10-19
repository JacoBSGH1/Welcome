for i in range(10):
    print(i)
print('-'*80)

for i in range(5,11):
    print(i, end=' ')

print('\n'+'-'*80)

for i in reversed(range(20,50,3)):
    print(i, end=' ')
print('\n'+'-'*80)

# negative steps (3rd number above) works the same and reversed(range())

# while loop operates as long as condition is true and we need a stopping condition.
# Otherwise it will run indefinitely.
print('While loop')
i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # incrementing the condition so while stops at some point
print('\n'+'-'*80)

i = 0
while i < 10:
    i += 1 # the increment must be here, not after if statement
    # (it would infinitely continue and run forever -
    # continue makes it go back to beginning without printing)
    if i % 3 == 0:
        continue
    if i == 8:
        break # stops whole loop prematurely,
        # generally bad practice to use break or continue
    print(i, end=' ')

print('\n'+'-'*80)

# In general if you can, you want to avoid too many conditions