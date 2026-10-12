import sys

a = 153.36361
b = 546
c = a + b
print('c')
print(f'a={a}')
print(f'b={b}')
print(f'c={c}')
type_c = type(c)
print(f'type_c: {type_c} c={c}')

d = 43245248927230975024760927309573296424972094760925342752098475
e = 69472093759137062743975931692853972052739579137062795709427096

f = d+e
print(f'f={f}')
print(f'type_f={type(f)}')
print('f={}'.format(f))
s_d = str(d)
num_digits_d = len(s_d)
print(f'num_digits_d={num_digits_d}')

f_d = 43245248927230975024760927309573296424972094760925342752098475.0
f_e = 69472093759137062743975931692853972052739579137062795709427096.0
print(f'type(f_d)={type(f_d)}')
print(f'f_d={f_d}')
print(f'f_e={f_e}')
f_f = f_d + f_e
print(f'f_f={f_f}')
# big or very small floats will lose us information - that's why data type is important
# that applies only to pure python. Packages may have different length limit

g = 1.52e-2
print(f'g={g}')
# the amount we can store in int is memory, float has a limit of ~1.79e308

max_f = 1.79e308
print(f'max_f={max_f}')

print(sys.float_info) # exact limit of float
# floats often can present rounding errors

# binary
b_b=0b1011
print(f'b_b={b_b}')

# hexadecimal
# 1f = 1*16^1 + f=(15)*16^0 = 16+15 = 31

h_c = 0x1f
print(f'h_c={h_c}')

#grounding
a = 1.9835
b = round(a,2)
print(f'a={a}')
print(f'b={b}')

#division+rest
f = 10
g = 4
r = f % g
print(f'r={r}')

#will cause error, cause python does not automatically convert the string into int,
#and it cannot operate on strings. If we add int it will work, but we can't
# add decimals or letters to it.
h = 9
i = int('9')
j = h + i
print(f'j={j}')