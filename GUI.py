from config import directory, prefix, include_folder_name, space_al, is_lower_cap
from change_name import change_filenames, change_folder_name, new_filename, generate_preview_name
from tkinter import *
from tkinter import filedialog

def space_altenative_ok(text):
    return len(text) <= 1

def create_error_popup(error):
    raise error

def update_config():
    global prefix
    global directory
    global include_folder_name
    global is_lower_cap
    global space_al

    prefix = prefix_var.get()
    is_lower_cap = lower_cap_var.get()
    directory = directory_var.get()
    include_folder_name = incl_folder_var.get()
    space_al = space_al_var.get()


#Region: Command 
def change_folder_name_cmd():
    try:
        global folder_name_browses
        global directory
        new_path = change_folder_name(directory=directory,folder_new_name=new_folder_name.get())
        directory = new_path
        directory_var.set(directory)
    except Exception as e:
        create_error_popup(error=e)

def browse_folder_cmd():
    #TODO: Try catch
    global directory_var
    global directory
    update_config()
    directory = filedialog.askdirectory(
    title="Browse Folder"
    )
    directory_var.set(directory)


def update_preview_cmd():
    global preview_old
    global preview_name

    update_config()
    preview_name.set(generate_preview_name(
                directory=directory,
                prefix=prefix,
                space_altenative=space_al,
                include_folder_name=include_folder_name,
                is_lower_cap=is_lower_cap,
                filename=preview_old.get()
            )
        )
    
def change_name_cmd():
    try:
        update_config()
        change_filenames(
            directory=directory,
            prefix=prefix,
            space_altenative=space_al,
            include_folder_name=include_folder_name,
            is_lower_cap=is_lower_cap,
        )
    except Exception as e:
        create_error_popup(e)
    
#Engregion

#Region UI
main = Tk()
main.geometry("750x750")

preview_old = StringVar()
preview_old.set("File Name")
preview_name = StringVar()
new_folder_name = StringVar()
directory_var = StringVar()

#Lower cap tick box
lower_cap_var = BooleanVar()
lower_cap_btn = Checkbutton(main, text="Lower Caps", variable=lower_cap_var)
lower_cap_btn.grid(row=1, columnspan=2, column=0, sticky=W)

#Include folder name in filename
incl_folder_var = BooleanVar()
include_folder_name_btn = Checkbutton(main, text="Include Foldername in Filename", variable=incl_folder_var)
include_folder_name_btn.grid(row=2, columnspan=2, column=0, sticky=W)

#Prefix
prefix_label = Label(main, text="Prefix for file name")
prefix_label.grid(row=3, sticky=W)

prefix_var = StringVar()
prefix_text_box = Entry(main, textvariable=prefix_var)
prefix_text_box.grid(row=3,column=1,columnspan=2, sticky=W)

#Space Alternative
space_al_var = StringVar()
space_al_label = Label(main, text="Space alternative")
space_al_label.grid(row=4, sticky=W)
space_al_text_box = Entry(main,
                        textvariable=space_al_var, 
                        validate='all', 
                        validatecommand=(space_altenative_ok, '%p')
                    )
space_al_text_box.grid(row=4,column=1,columnspan=2, sticky=W)


#Folder and browse folder
#TODO: Drag and drop file to browse.

browse_folder_label = Label(main, text="Choose Folder Directory")
browse_folder_label.grid(row=5, column= 0, columnspan=2, sticky=W)

folder_directory_entry = Entry(main, textvariable=directory_var, width=60)
folder_directory_entry.grid(row=6,column=0,columnspan=4, sticky=W)

folder_browse_btn = Button(main, text="Browse", command=browse_folder_cmd)
folder_browse_btn.grid(row=6, column=5, sticky=W, padx= 10)

#Rename Folder
rename_folder_label = Label(main, text="Rename folder")
rename_folder_label.grid(row=7, column= 0, columnspan=2, sticky=W)

rename_folder_entry = Entry(main, textvariable=new_folder_name, width=40)
rename_folder_entry.grid(row=8,column=0,columnspan=4, sticky=W)

rename_folder_btn = Button(main, text="Rename", command=change_folder_name_cmd)
rename_folder_btn.grid(row=8, column=5, sticky=W, padx= 10)

#Label Preview
preview_label = Label(main, text="Filename Preview:")
preview_label.grid(row = 9)

Label(main,text="Old: ").grid(row=10, column=0)

preview_old_label = Label(main, textvariable=preview_old)
preview_old_label.grid(row=10, column=2, columnspan=2)


Label(main,text="New: ").grid(row=11, column=0)

preview_name_label = Label(main, textvariable=preview_name)
preview_name_label.grid(row=11, column=2, columnspan=2)

#Update preview btn
update_preview_btn = Button(main, text="Update preview", command=update_preview_cmd, width=50)
update_preview_btn.grid(row=12, columnspan=4)

#Change name button
change_name_btn = Button(main, text="Process Change Name", command=change_name_cmd, width=50)
change_name_btn.grid(row=13, columnspan=4)

#End region

main.mainloop();



