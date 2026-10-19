import os
# / will always work, \ will not work every time and not on Linux
my_file = os.path.join('..', 'data', 'mytext.txt') # the recommended way,
# needs import os, relative path, this working depends on working directory

# my_file = 'C:/Users/kbogd/PyCharmMiscProject/data/mytext.txt'  # - absolute path


#Current working directory
cwd = os.getcwd()
print(cwd)

f = open(my_file)
lines = f.readlines() # not recommended for big files,
# because it keeps everything in memory. Better to go line by line.
for line in lines:
    print(line, end='')
f.close()

print('\n')
#preffered syntax, allows to open multiple files at ones
# and no need to manually close the file
with open(my_file, 'r') as f: # r is mode of opening,
# reading (r), writing (w), appending (a), for binary files its +b (rb,wb)
    lines = f.readlines()
    for line in lines:
        print(line, end='')

# if you distribute code along with data, its better to use relative path
# Operating systems differ here, in Windows we can only operate on the same tree
# (like C: and D: will be different trees) !!!
# Linux has only 1 tree, everything is interpreted/seen as a file