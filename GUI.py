from config import directory, prefix, include_folder_name, space_al, is_lower_cap
from change_name import change_filenames, change_folder_name, new_filename
from tkinter import *
from tkinter import filedialog

new_folder_name = None
folder_name_browse = None
preview_old = StringVar()
preview_old.set("File Name")
preview_name = StringVar()

def space_altenative_ok(text):
    return len(text) <= 1

def create_error_popup(error):
    pass


#*Region: Command 
def change_folder_name_cmd():
    try:
        global folder_directory_entry
        new_dir = change_folder_name(directory=directory,folder_new_name=new_folder_name)
        folder_directory_entry.delete(0, END)
        folder_directory_entry.insert(0, new_dir)
    except Exception as e:
        create_error_popup(error=e)

def browse_folder_cmd():
    #TODO: Try catch
    global folder_name_browse
    global folder_directory_entry
    folder_name_browse = filedialog.askdirectory(
    title="Browse Folder"
    )
    folder_directory_entry.delete(0, END)
    folder_directory_entry.insert(0, folder_name_browse)

def update_preview_cmd():
    # preview_name.set(generate_preview(filename="File Name"))
    pass

main = Tk()
main.geometry("750x750")

#Lower cap tick box
cap_tick_box = BooleanVar()
lower_cap_btn = Checkbutton(main, text="Lower Caps", variable=cap_tick_box)
lower_cap_btn.grid(row=1, columnspan=2, column=0, sticky=W)

#Include folder name in filename
incl_folder_tick_box = BooleanVar()
include_folder_name_btn = Checkbutton(main, text="Include Foldername in Filename", variable=incl_folder_tick_box)
include_folder_name_btn.grid(row=2, columnspan=2, column=0, sticky=W)

#Prefix
prefix_label = Label(main, text="Prefix for file name")
prefix_label.grid(row=3, sticky=W)

prefix_text_box = Entry(main, textvariable=prefix)
prefix_text_box.grid(row=3,column=1,columnspan=2, sticky=W)

#Space Alternative
space_al = Label(main, text="Space alternative")
space_al.grid(row=4, sticky=W)
space_al_text_box = Entry(main,
                        textvariable=space_al, 
                        validate='all', 
                        validatecommand=(space_altenative_ok, '%p')
                    )
space_al_text_box.grid(row=4,column=1,columnspan=2, sticky=W)


#Folder and browse folder
browse_folder_label = Label(main, text="Choose Folder Directory")
browse_folder_label.grid(row=5, column= 0, columnspan=2, sticky=W)

folder_directory_entry = Entry(main, textvariable=folder_name_browse, width=60)
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

preview_name_label = Label(main, textvariable=new_filename)
preview_name_label.grid(row=11, column=2, columnspan=2)

#Update preview btn
update_preview_btn = Button(main, text="Update preview", command=update_preview_cmd, width=50)
update_preview_btn.grid(row=12, columnspan=2)
main.mainloop();



