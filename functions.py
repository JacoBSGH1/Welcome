def sum_it(a: int, b: int) -> int:
    summm = a + b
    # return summm, - makes it a tuple instead of simple int or float - can be a problem all because of a comma
    return summm

print(sum_it(1.67, 32.53)) #will still calculate - we can specify the type, but not enforce it
# Python is not very restrictive and tries to get the result

'''def sum_it_params(a, b:5) -> int:
    return a + b
print(sum_it_params(1.67))
print(sum_it_params())
print(sum_it_params(b=15))'''

print('-'*60)

b=6
if b > 5:
    d = 10
else:
    d = 5

print(f'd={d}')
# d is defined in the if function -> without else, it will not define d and
# give error if, if condition is not met

for i in range(10):
    bi = i*10

print(f'bi={bi}')

# something defined in the function won't get out of it
# something defined before the function is called can be taken into it

print('-'*60)

def sum_and_multiply(a,b):
    summ = a+b
    #def multiply(c,d):, if we use a and b here, they would get temporarily overwritten for multiplication
                        # depending on our further actions the result would be the same or different
    #    return c*d
    def multiply():
        return a*b
    multi = multiply() # the c and d will already not exist here
    # multi = multiply(a,b)
    return summ,multi #result will be a tuple

result = sum_and_multiply(3,4)
print(f'result: {result}')
print(f'type(result): {type(result)}')

sum_ab, multi_ab = sum_and_multiply(3,4)
print(f'sum_ab: {sum_ab}, multi_ab: {multi_ab}')
