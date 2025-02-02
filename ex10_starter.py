import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
file_name = glob.glob(pattern)
print(file_name)
# TODO: use os.path.getsize to find each file's size
for path_size in file_name:
    print(os.path.getsize(path_size))
# TODO: Add a test to only display files that are not zero length
# TODO: Remove the leading directory name(s) from each filename before you print it -
for path_name in file_name:
    if len(path_name) > 0:
        print(os.path.basename(path_name))

