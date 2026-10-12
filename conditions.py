p = True
q = False
print(type(p))

if p:
    print('p is true')
else:
    print('p is false')

print('---------')

if p and q:
    print('p and q is true')
else:
    print('p or q is false')

print('----------')

if p or not q:
    print('p or q is true')
else:
    print('p and q is false')

print('----------')

if p ^ q:
    print('p xor q is true')
else:
    print('not xor p and q')