import os
from pathlib import Path


def change_filenames(directory, prefix=None, include_folder_name=False ,space_altenative=None, is_lower_cap=False):
    ''''
    Description:
    Change file name to format prefix?_foldername?_filename
    (_ mean space altenative and can be replace by for example "-")
    Param:
        string directory: Target folder directory
        string prefix:  filename prefix to add
            Default: None (mean no prefix to add)
        char space_altenative: alterative character to replace space
            Default: None (mean keep all space)
        bool is_lower_cap: should all filename be lower cap 
            Default: False
    Return
        bool success: (Successfully change all file name) ? True : False.
    Raise:
        Exception:
    '''
    folder_name = os.path.basename(directory) if include_folder_name else None
    space = space_altenative if space_altenative != None else " "
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if not os.path.isfile(path):
            continue
        new_name = new_filename(filename, prefix, folder_name, space, is_lower_cap)
        p = Path(path)
        ext = p.suffix
        p.rename(Path(p.parent, new_name + ext))
    return True

def new_filename(filename, prefix, folder_name, space, is_lower_cap):
    """
    Description:
    Generate a new file name base on configs and old filename
    Param:
        string filename: Name of file to change
        string prefix:  filename prefix to add
        char space_altenative: alterative character to replace space
        bool is_lower_cap: should all filename be lower cap 
    Return:
        tring new_name: generated file name
    Raise:
        Exception:
    """
    new_name = ""
    if prefix != None: 
        new_name = new_name + prefix + space
    if folder_name != None:
        new_name = new_name + folder_name + space
    words = filename.split(" ")
    for word in words:
        new_name = new_name + word + space
    new_name = new_name[:-1]
    if is_lower_cap: 
        new_name = new_name.lower();
    return new_name

def change_folder_name(directory, folder_new_name):
    if (directory == None or directory == ""): raise Exception("Invalid Directory")
    if (folder_new_name == None or folder_new_name == ""): raise Exception("Invalid Folder Name")
    path = Path(directory)
    new_path = os.path.join(os.path.dirname(directory), folder_new_name)
    path.rename(new_path)
    return str(path)

def generate_preview_name(directory, prefix=None, include_folder_name=False ,space_altenative=None, is_lower_cap=False, filename="File Name"):
    folder_name = os.path.basename(directory) if include_folder_name else None
    space = space_altenative if space_altenative != None else " "
    new_name = new_filename(filename, prefix, folder_name, space, is_lower_cap)
    return new_name