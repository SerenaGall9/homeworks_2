import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
# sys is a module which writes function plus variables and is used to interact with the python runtime. In this case it gives us information of the platform we are using.
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
#os is the operating system
#hdir is a variable storing the user home directory path
# Construct a portable wildcard patter
# Environ is a method of the operating system which provides access to all the environment variables stored in the operating system.
# Environment variables are values that affect how a processors run.
pattern = os.path.join(hdir,'*')
# join combines the pattern that were setting at an operational level within the whole directory.
#The "*" is a wildcard which in this case means that any path is included.
# TODO: Use the glob.glob() function to obtain the list of filenames
file_name = glob.glob(pattern)
#glob is a module which is short for global and is a function that searches all the files in a particular path or file pattern.
print(file_name)
# TODO: use os.path.getsize to find each file's size
for path_size in file_name:
    print(os.path.getsize(path_size))
# the for loop is used to iterate over the list stored in the file_name variable. In this circumstance we are getting the size in bytes of each path individually.
# TODO: Add a test to only display files that are not zero length
# TODO: Remove the leading directory name(s) from each filename before you print it -
for path_name in file_name:
    if len(path_name) > 0:
        print(os.path.basename(path_name))
#In this statement we are excluding any empty files by finding out the length of the pathname/pathsize is greater than 0. we are also using a new method called basename to remove the leading directory names.

