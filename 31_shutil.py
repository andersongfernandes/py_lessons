# time code 2:53:47
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copy metadata (file's creation and modification times)

import shutil

shutil.copyfile('test.txt','testCopy1.txt') # a copy may be saved in another folder
