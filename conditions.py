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

a = 10
if a<12:
    print('a<12')
    print('2nd line')
print('after the block')

def sumit(a,b):
    # comment
    return a+b

print(sumit(3,8))
print(sumit(3,4))