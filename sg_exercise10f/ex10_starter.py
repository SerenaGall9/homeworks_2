# get the directory name form the environment using os.environ(class)
# sys is a module
# glob is a module
# sys.platform : platform (string) is variable of sys module
# # print(os.environ)
# # print(sys)
# # print(glob)
# print(sys.platform)
# print(type(sys.platform))

import sys, glob, os
# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
# # # Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
# # # TODO: Use the glob.glob() function to obtain the list of filenames
file_list = glob.glob(pattern)
# # # TODO: use os.path.getsize to find each file's size
for file in file_list:
    size = os.path.getsize(file)
    print(file, size)
    # # # TODO: Add a test to only display files that are not zero length
    # # # TODO: Remove the leading directory name(s) from each filename before you print it -
    if size > 0 :
        file_name = os.path.basename(file_name)
        print(file_name)


# # # using os.path.basename()
#
