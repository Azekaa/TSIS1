import os
import shutil

def copy(f1, f2):
    if os.path.isfile(f1):
        shutil.copyfile(f1, f2)
        print('copied')
    else:
        print('file doesnt exists')
    
f1 = 'C:/Users/user/Desktop/pp2/TSIS6/dir_files/7file.txt'
f2 = 'C:/Users/user/Desktop/pp2/TSIS6/dir_files/7file_new.txt'
copy(f1, f2)