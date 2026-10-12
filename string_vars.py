s_1 = 'abcdefg'
s_2 = 'hijkl'

print(f's_1[2]={s_1[2]}')
print(f's_1[2-4]={s_1[2:4]}')
print(f's_1[:4]={s_1[:4]}')
print(f's_1[4:]={s_1[4:]}')
print(f's_1[-3:]={s_1[-3:]}')

print('\n\n\nabgg\tgrhreh')
print(r'\n\n\nabgg\tgrhreh')
s_3 = s_1 + s_2
print(f's_3={s_3}')

#find position of character in ascii table
c_a = ord('a')
print(f'c_a={c_a}')

#find character from position in ascii table
c_b = chr(98)
print(f'c_b={c_b}')

#ascii table has not enough characters - for different languages there
# are different "codepages". There are also standards for encoding characters
# in languages as Polish etc. there is ISO 8859-2

# most current universal standard is Unicode. It marks every character with
# a code point. And those characters outside typical ascii table are represented
# with 2 or more characters.

# finding stuff in a string
s_5 = "abcdefgabcdefg"
i_abc = s_5.find('bce')
print(f'i_abc={i_abc}')
i_abc = s_5.rfind('bc')
print(f'i_abc={i_abc}')

#i_abc = s_5.index('bce')
#print(f'i_abc={i_abc}')
i_abc = s_5.rindex('bc')
print(f'i_abc={i_abc}')
# as long as they work, they don't differ

#separating
s_6='1445;2553;3647'
arr_s6 = s_6.split(';')
print(f'arr_s6={arr_s6}')

#stripping
s_7 = '     sgsbg  '
s_8 = s_7.strip()
print(f's_8={s_8}')