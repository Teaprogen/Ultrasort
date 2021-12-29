import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter


def getFolderPath():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


def sortFileType():
    local_path = folder_path.get()

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
    msgWorkDone()


def deleteEmptyFolders():
    local_path = folder_path.get()
    walk = list(os.walk(local_path))
    for local_path, _, _ in walk[::-1]:
        if len(os.listdir(local_path)) == 0:
            print("removed " + local_path)
            os.rmdir(local_path)
    msgWorkDone()


def msgWorkDone():
    global pop
    pop = Toplevel(root)
    pop.title("Done!")
    popWindowSize = "200x100"
    pop.geometry(popWindowSize + '+{}+{}'.format(int(root.winfo_screenwidth() /
                 2) - 200, int(root.winfo_screenheight()/2)-200))
    pop.resizable(False, False)
    pop.config(bg="#1e1e1e")
    pop.grid_columnconfigure(0, weight=1)
    pop.grab_set()

    lblMsg = Label(pop,
                   text="Work done!",
                   font=("Arial", 25),
                   bg="#1e1e1e",
                   fg="#ffffff")
    lblMsg.grid(row=0, column=0)

    btnMsg = Button(pop,
                    text="OK",
                    command=popDestroy,
                    font=("Arial", 15), activeforeground="#f0f0f0", activebackground="#444444", bg="#333333", fg="#ffffff")
    btnMsg.grid(row=1)


def popDestroy():
    pop.grab_release()
    pop.destroy()


root = Tk()
rootWindowSize = '400x150'
root.geometry(rootWindowSize+'+{}+{}'.format(int(root.winfo_screenwidth() /
              2) - 200, int(root.winfo_screenheight() / 2) - 200))
root.title("ULTRASORT")
root.resizable(False, False)
root.configure(bg='#1e1e1e')
root.iconphoto(True, tkinter.PhotoImage(file='icon.png'))


folder_path = StringVar()

lblHint = Label(root,
                text="Directory:",
                font=("Arial", 13),
                bg="#1e1e1e",
                fg="#ffffff",)
lblHint.grid(row=0, column=0, sticky=W, )

lblDirectory = Label(root,
                     textvariable=folder_path,
                     font=("Arial", 13),
                     bg="#1e1e1e",
                     fg="#ffffff")
lblDirectory.grid(row=1, column=0, columnspan=2)

btnFind = Button(root,
                 text="Browse Folder",
                 font=("Arial", 13),
                 activeforeground="#f0f0f0",
                 activebackground="#444444",
                 command=getFolderPath,
                 bg="#333333",
                 fg="#ffffff",
                 width=17)
btnFind.grid(row=2, column=0, sticky=W+E)

btnSort = Button(root,
                 text="Sort files by type",
                 font=("Arial", 13),
                 activeforeground="#f0f0f0",
                 activebackground="#444444",
                 command=sortFileType,
                 bg="#333333",
                 fg="#ffffff",
                 width=17)
btnSort.grid(row=3, column=0, sticky=W+E)

btnDelete = Button(root,
                   text="Delete empty folders",
                   font=("Arial", 13),
                   activeforeground="#f0f0f0",
                   activebackground="#444444",
                   command=deleteEmptyFolders,
                   bg="#333333",
                   fg="#ffffff",
                   width=17)
btnDelete.grid(row=4, column=0, sticky=W+E)

root.mainloop()
