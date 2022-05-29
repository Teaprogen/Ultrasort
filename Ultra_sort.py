import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk

IMAGE_EXT = ['png', 'jpg', 'jpeg', 'gif', 'bmp',
             'ai', 'psd', 'tif', 'tiff', 'ico', 'svg']

VIDEO_EXT = ['mp4', 'webm', 'webm']

DOCUMENT_EXT = ['pdf', 'doc', 'docx',
                'pptx', 'txt', 'ppt', 'odp', 'key', ]

AUDIO_EXT = ['mp3', 'wav', 'flac', 'aif',
             'cda', 'mid', 'mpa', 'ogg', 'wma', 'wpl']

COMPRESSED_EXT = ['rar', 'tar', 'zip', '7z', 'pkg', 'z']

FONT_EXT = ['fnt', 'fon', 'otf', 'ttf']

INTERNET_EXT = ['html', 'css']

DATA_EXT = ['csv', 'dat', 'db', 'dbf', 'log',
            'mdb', 'sav', 'sql', 'xml', 'json']

EXECUTABLE_EXT = ['exe', 'bat', 'bin', 'com', 'jar', 'msi', 'wsf']

TYPE_LIST = [IMAGE_EXT, VIDEO_EXT, DOCUMENT_EXT,
             AUDIO_EXT, COMPRESSED_EXT, FONT_EXT,
             INTERNET_EXT, DATA_EXT, EXECUTABLE_EXT]

TYPE_LIST_NAME = ['Images', 'Videos', 'Documents',
                  'Audio', 'Archives', 'Fonts',
                  'Internet files', 'Data files', 'Executable files']


def getFolderPath():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)


def deleteEmptyFolders():
    local_path = folder_path.get()
    walk = list(os.walk(local_path))
    lengthOfList = len(walk)

    for local_path, _, _ in walk[::-1]:
        if len(os.listdir(local_path)) == 0:
            os.rmdir(local_path)

    msgWorkDone()


def sortFileByExtension():

    local_path = folder_path.get()

    # creating of list_ to check for errors
    list_of_files = "none"

    # Delete Windows invisible symbols
    try:
        list_of_files = os.listdir(local_path)
    except OSError as error:
        local_path = local_path[1:]
        try:
            list_of_files = os.listdir(local_path)
        except OSError as error:
            local_path = local_path[1:]

    for file_name in list_of_files:
        name, ext = os.path.splitext(file_name)

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
                shutil.move(local_path + '/' + file_name,
                            local_path + '/' + ext + '/' + file_name)

            # This will create a new directory,
            # if the directory does not already exist
            else:
                os.makedirs(local_path + '/' + ext)
                shutil.move(local_path + '/' + file_name,
                            local_path + '/' + ext + '/' + file_name)

    msgWorkDone()

def sortFilesByType():

    local_path = folder_path.get()

    list_of_files = ""

    # Delete Windows invisible symbols
    try:
        list_of_files = os.listdir(local_path)
    except OSError as error:
        local_path = local_path[1:]
        try:
            list_of_files = os.listdir(local_path)
        except OSError as error:
            local_path = local_path[1:]

    # Create folders to move files
    for folderName in TYPE_LIST_NAME:
        if not (os.path.exists(local_path + '/' + folderName)):
            os.makedirs(local_path + '/' + folderName)

    # Sorting files in folders
    for file_name in list_of_files:
        name, ext = os.path.splitext(file_name)

        # This is going to store the extension type
        ext = ext[1:]

        # avoids desktop.ini file because it's requires administrator rights to move it
        if name != "desktop" and ext != "ini":

            # This forces the next iteration,
            # if it is the directory
            if ext == '':
                continue

            # Moving files in subfolder
            for item in TYPE_LIST:
                index = TYPE_LIST_NAME[TYPE_LIST.index(item)]
                if ext in item:
                    shutil.move(local_path + '/' + file_name,
                                local_path + '/' + index + '/' + file_name)

    msgWorkDone()


def msgWorkDone():
    if folder_path == None:
        return
    global pop
    pop = Toplevel(root)
    pop.title("Done!")
    popWindowSize = "300x100"
    pop.geometry(popWindowSize + '+{}+{}'.format(int(root.winfo_screenwidth() / 2) - 150,
                                                 int(root.winfo_screenheight() / 2) - 50))
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
                    font=("Arial", 15),
                         activeforeground="#f0f0f0",
                         activebackground="#444444",
                         bg="#333333",
                         fg="#ffffff")
    btnMsg.grid(row=1)


def popDestroy():
    pop.grab_release()
    pop.destroy()


root = Tk()
rootWindowSize = '559x148'
root.geometry(rootWindowSize+'+{}+{}'.format(int(root.winfo_screenwidth() / 2) - 279,
                                             int(root.winfo_screenheight() / 2) - 74))
root.title("ULTRASORT")
root.resizable(False, False)
root.configure(bg='#1e1e1e')
root.iconphoto(True, tk.PhotoImage(file='icon.png'))


folder_path = StringVar()

lblHint = Label(root,
                text="Directory",
                font=("Arial", 13),
                bg="#1e1e1e",
                fg="#ffffff",
                )
lblHint.grid(row=0, column=0, sticky='NW')

lblDirectory = Label(root,
                     textvariable=folder_path,
                     font=("Arial", 13),
                     bg="#1e1e1e",
                     fg="#ffffff",
                     )
lblDirectory.grid(row=1, column=0, sticky='NW')

btnFind = Button(root,
                 text="Browse Folder",
                 font=("Arial", 13),
                 activeforeground="#f0f0f0",
                 activebackground="#444444",
                 command=getFolderPath,
                 bg="#1e1e1e",
                 fg="#ffffff",
                 width=30)
btnFind.grid(row=2, column=0, sticky='NW')

btnSort = Button(root,
                 text="Sort files by extension in subfolders",
                 font=("Arial", 13),
                 activeforeground="#f0f0f0",
                 activebackground="#444444",
                 command=sortFileByExtension,
                 bg="#1e1e1e",
                 fg="#ffffff",
                 width=30)
btnSort.grid(row=3, column=0, sticky='NW')

btnDelete = Button(root,
                   text="Delete empty folders",
                   font=("Arial", 13),
                   activeforeground="#f0f0f0",
                   activebackground="#444444",
                   command=deleteEmptyFolders,
                   bg="#1e1e1e",
                   fg="#ffffff",
                   width=30)
btnDelete.grid(row=4, column=0, sticky='NW')

btnNew = Button(root,
                text="Test_Button",
                font=("Arial", 13),
                activeforeground="#f0f0f0",
                activebackground="#444444",
                bg="#1e1e1e",
                fg="#ffffff",
                width=30)
btnNew.grid(row=4, column=1, sticky='NW')

btnNew1 = Button(root,
                 text="Test_Button1",
                 font=("Arial", 13),
                 activeforeground="#f0f0f0",
                 activebackground="#444444",
                 bg="#1e1e1e",
                 fg="#ffffff",
                 width=30)
btnNew1.grid(row=3, column=1, sticky='NW')

btnNew2 = Button(root,
                 command=sortFilesByType,
                 text="Sort files by type of file",
                 font=("Arial", 13),
                 activeforeground="#f0f0f0",
                 activebackground="#444444",
                 bg="#1e1e1e",
                 fg="#ffffff",
                 width=30)
btnNew2.grid(row=2, column=1, sticky='NW')


root.mainloop()
