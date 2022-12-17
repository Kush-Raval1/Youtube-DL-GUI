import os
#if you want to use a custom directory, change custompath from False to True, remove the "#" from the start of line 4, and replace "MY/CUSTOM/PATH" with your path
custompath = False
#customdir= r"MY/CUSTOM/DIRECTORY"

def ddlDir():
    local_dir = os.path.dirname(__file__)
    if (os.path.exists(os.path.join(local_dir, "Downloads")) == False) and custompath == False:
        os.makedirs("Downloads")
        dir = os.path.join(local_dir, "Downloads")
    elif (os.path.exists(os.path.join(local_dir, "Downloads")) == True) and custompath == False:
        dir = os.path.join(local_dir, "Downloads")
    elif custompath == True:
        dir = customdir
    return dir
