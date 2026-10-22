import os

#my_folder = os.path.join('..')

#my_files = os.listdir(my_folder)
#print(my_files)
# fsize = os.path.getsize('..')
# print(fsize)

def size_compute(folder):
    folder = os.path.join('..', folder)
    if not os.path.exists(folder):
        print('Folder not found')
    else:
        folder_size = os.path.getsize(folder)
        print(f'{folder} folder size:', folder_size)

size_compute('')

# should it show for all 4096? I don't think so, but it also gives that number in way we did on labs