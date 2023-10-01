# time code 3:01:21
# os remove

# exclusive to delete files
import os, shutil

filePath = 'assets/test1.txt'
try:
    os.remove(filePath)
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to delete that.")
    
# the folder must be EMPTY to be deleted
folderPath = 'assets/tree'
try:
    os.rmdir(folderPath)
except FileNotFoundError:
    print("That file was not found.")
except PermissionError:
    print("You do not have permission to delete that.")
except OSError:
    print("You cannot delete thar using this function.")
else:
    print(folderPath+ " was deleted.")


# tree = folder with file or an empty folder
treePath = 'assets/tree'
try:
    shutil.rmtree(treePath)
except FileNotFoundError:
    print("That tree was not found.")
except PermissionError:
    print("You do not have permission to delete this tree.")
except OSError:
    print("You cannot delete that using this function.")
else:
    print(treePath+" was deleted.")