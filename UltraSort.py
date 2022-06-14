
import os
import shutil
import sys
from tkinter import Button, Label, PhotoImage, Tk, Toplevel, filedialog, Tk
IMAGE_EXT = ['webp', 'PNG', 'HEIC', 'png', 'jpg', 'jpeg', 'gif',
             'bmp', 'ai', 'psd', 'tif', 'tiff', 'ico', 'svg', 'JPG']

VIDEO_EXT = ['mp4', 'webm', 'webm', 'mkv']

DOCUMENT_EXT = ['DOCX', 'pps', 'mpp', 'xlsx', 'PDF', 'pdf', 'doc',
                'docx', 'pptx', 'txt', 'ppt', 'odp', 'key', 'xls']

AUDIO_EXT = ['mp3', 'wav', 'flac', 'aif',
             'cda', 'mid', 'mpa', 'ogg', 'wma', 'wpl']

COMPRESSED_EXT = ['rar', 'tar', 'zip', '7z', 'pkg', 'z']

FONT_EXT = ['fnt', 'fon', 'otf', 'ttf']

INTERNET_EXT = ['html', 'css', 'torrent', 'php', 'htm']

DATA_EXT = ['siq', 'csv', 'dat', 'db', 'dbf', 'log',
            'mdb', 'sav', 'sql', 'xml', 'json']

EXECUTABLE_EXT = ['exe', 'bat', 'bin', 'com', 'jar', 'msi', 'wsf']

TYPE_LIST = [IMAGE_EXT, VIDEO_EXT, DOCUMENT_EXT,
             AUDIO_EXT, COMPRESSED_EXT, FONT_EXT,
             INTERNET_EXT, DATA_EXT, EXECUTABLE_EXT]

TYPE_LIST_NAME = ['Images', 'Videos', 'Documents',
                  'Audio', 'Archives', 'Fonts',
                  'Internet files', 'Data files', 'Executable files']


class UltraSort():
    def __init__(self) -> None:
        self.path = ''

    def __repr__(self) -> str:
        return "<...some useful description...>"

    def _flattenList(self, list_to_flatten: list) -> list:
        return [item for sublist in list_to_flatten for item in sublist]

    def getFolderPath(self) -> None:
        """Path selector.

        Returns:
            None: Ask for directory, and set path.
        """
        self.path = filedialog.askdirectory()
        if self.path != '':
            lblHint['text'] = ("Directory: " + str(ent.path))

    def deleteEmptyFolders(self) -> None:
        """Deletes empty folders in attribute path.

        Returns:
            None: In path deletes all empty folders and in subfolders
        """
        if self.path != '':
            local_path = self.path
        else:
            return
        walk = list(os.walk(local_path))

        for local_path, _, _ in walk[::-1]:
            if len(os.listdir(local_path)) == 0:
                os.rmdir(local_path)
        msgWorkDone()

    def sortFileByExtension(self) -> None:
        """Sorts files in path by extension type.

        Return:
            None: In path sorts all files by extension and moves to according folders.
            If no such folders exits, creates it.        
        """
        if self.path != '':
            local_path = self.path
        else:
            return
        list_of_files = []
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
            if (name != "desktop" and ext != "ini") and (ext != 'lnk'):

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

    def sortFilesByType(self) -> None:
        """Sorts files in path by general type.

        Return
            None: In path sorts all files by type and moves to according folders.
            If no such folders exits, creates it. 
        """
        if self.path != '':
            local_path = self.path
        else:
            return
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

                # Moving files in subfolder
                for type_item in TYPE_LIST:
                    subFolderType = TYPE_LIST_NAME[TYPE_LIST.index(type_item)]
                    if ext in type_item or (name in type_item and ext == ''):
                        shutil.move(local_path + '/' + file_name,
                                    local_path + '/' + subFolderType + '/' + file_name)
        msgWorkDone()


def msgWorkDone():
    if ent.path == '':
        return
    global pop
    pop = Toplevel(root)
    pop.title("Done!")
    popWindowSize = "300x100"
    pop.geometry(popWindowSize + '+{}+{}'.format(int(root.winfo_screenwidth() / 2) - 150,
                                                 int(root.winfo_screenheight() / 2) - 50))
    pop.resizable(False, False)
    pop.grid_columnconfigure(0, weight=1)
    pop.grab_set()

    lblMsg = Label(pop,
                   text="Work done!",
                   font=("Arial", 25))
    lblMsg.grid(row=0, column=0)

    btnMsg = Button(pop,
                    text="OK",
                    command=popDestroy,
                    font=("Arial", 15))
    btnMsg.grid(row=1)


def popDestroy():
    pop.grab_release()
    pop.destroy()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":

    ent = UltraSort()
    root = Tk()
    window_width = 590
    window_height = 130

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.title("ULTRASORT")
    root.resizable(False, False)
    root.iconphoto(True, PhotoImage(file=resource_path('icon.png')))

    lblHint = Label(root,
                    text="Directory: None, select one.",
                    font=("Arial", 13))
    lblHint.grid(row=0, column=0, sticky="NSEW",
                 padx=10, pady=(10, 0), columnspan=2)

    btnFind = Button(root,
                     text="Browse Folder",
                     command=ent.getFolderPath,
                     font=("Arial", 13),
                     width=30)
    btnFind.grid(row=2, column=0, sticky="NSEW", padx=10, pady=10)

    btnSort = Button(root,
                     text="Sort files by extension in subfolders",
                     command=ent.sortFileByExtension,
                     font=("Arial", 13),
                     width=30)
    btnSort.grid(row=3, column=0, sticky="NSEW", padx=10)

    btnDelete = Button(root,
                       text="Delete empty folders",
                       command=ent.deleteEmptyFolders,
                       font=("Arial", 13),
                       width=30)
    btnDelete.grid(row=2, column=1, sticky="NSEW", pady=10)

    btnSort1 = Button(root,
                      command=ent.sortFilesByType,
                      text="Sort files by type of file",
                      font=("Arial", 13),
                      width=30)
    btnSort1.grid(row=3, column=1, sticky="NSEW")

    root.mainloop()
