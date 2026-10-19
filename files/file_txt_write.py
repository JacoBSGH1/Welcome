import os
my_file = os.path.join('..','data', 'myfile_out.txt')

f=open(my_file,'w')
f.write('hello world\n')
f.write('at sgh\n')
f.flush()
f.write('something\n')
f.close()

with open(my_file, 'a') as f:
    f.write('Appending this\n')