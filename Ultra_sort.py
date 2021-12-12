import os
import shutil
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk


def getFolderPath():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


def sortFileType():
    local_path = folder_path.get()
    print("Sorting all your shit")

    # creating of list_ to check for errors
    list_ = "none"

    # path of directory that going to be sorted and creating of list_ to check for errors
    try:
        list_ = os.listdir(local_path)
    except OSError as error:
        local_path = local_path[1:]
        try:
            list_ = os.listdir(local_path)
        except OSError as error:
            local_path = local_path[1:]
            print("Warning: File folder_path was intruded with double u202a")
        print("Warning: File folder_path was intruded with u202a")

    for file_ in list_:
        name, ext = os.path.splitext(file_)

        # This is going to store the extension type
        ext = ext[1:]

        # avoids desktop.ini file because it's requires administrator rights to move it
        if name != "desktop" and ext != "ini":

            # This forces the next iteration,
            # if it is the directory
            if ext == '':
                continue

            # This will move the file to the directory
            # where the name 'ext' already exists
            if os.path.exists(local_path + '/' + ext):
                shutil.move(local_path + '/' + file_,
                            local_path + '/' + ext + '/' + file_)

            # This will create a new directory,
            # if the directory does not already exist
            else:
                os.makedirs(local_path + '/' + ext)
                shutil.move(local_path + '/' + file_,
                            local_path + '/' + ext + '/' + file_)


def deleteEmptyFolders():
    local_path = folder_path.get()
    print("Deleting all your shit")
    walk = list(os.walk(local_path))
    for local_path, _, _ in walk[::-1]:
        if len(os.listdir(local_path)) == 0:
            print("removed " + local_path)
            os.rmdir(local_path)


root = Tk()
root.geometry('400x140+{}+{}'.format(int(root.winfo_screenwidth()/2) -
              200, int(root.winfo_screenheight()/2)-200))
root.title("ULTRASORT")
root.resizable(False, False)
# root.iconbitmap(default='icon1.ico')


folder_path = StringVar()

lbl1 = ttk.Label(root, text="Directory")
lbl1.grid(row=0, column=0, sticky=W)

lbl2 = ttk.Label(master=root, textvariable=folder_path)
lbl2.grid(row=1, column=0, columnspan=2)

btnFind = ttk.Button(text="Browse Folder", command=getFolderPath)
btnFind.grid(row=2, column=0, sticky=W)

btnSort = ttk.Button(text="Sort files by type", command=sortFileType)
btnSort.grid(row=3, column=0, sticky=W)

btnDelete = ttk.Button(text="Delete empty folders", command=deleteEmptyFolders)
btnDelete.grid(row=4, column=0, sticky=W)

root.mainloop()
