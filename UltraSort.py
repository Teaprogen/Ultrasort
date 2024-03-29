
import os
import shutil
from tkinter import Tk, Toplevel, filedialog, ttk

IMAGE_EXT = ['psd', 'webp', 'bmp', 'tif', 'jpg', 'ico', 'jpg',
             'png', 'ai', 'tiff', 'png', 'jpeg', 'heic', 'svg', 'gif']

VIDEO_EXT = ['mp4', 'webm', 'webm', 'mkv']

DOCUMENT_EXT = ['doc', 'key', 'pdf', 'xlsx', 'pps', 'pptx',
                'xls', 'docx', 'pdf', 'txt', 'docx', 'mpp', 'odp', 'ppt']

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
            None: Ask for directory, and sets path.
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

        for walk_path, _, _ in walk[::-1]:
            if len(os.listdir(walk_path)) == 0:
                os.rmdir(walk_path)
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
            ext = ext.lower()
            # avoids desktop.ini file because it's requires administrator rights to move it
            if (name != "desktop" and ext != "ini") and (ext != 'lnk'):

                if ext == '':
                    continue
                if os.path.exists(local_path + '/' + ext):
                    shutil.move(local_path + '/' + file_name,
                                local_path + '/' + ext + '/' + file_name)
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
            ext = ext.lower()
            # avoids desktop.ini file because it's requires administrator rights to move it
            if name != "desktop" and ext != "ini":

                # Moving files in subfolder
                for type_item in TYPE_LIST:
                    subFolderType = TYPE_LIST_NAME[TYPE_LIST.index(type_item)]
                    if ext in type_item or (name in type_item and ext == ''):
                        shutil.move(local_path + '/' + file_name,
                                    local_path + '/' + subFolderType + '/' + file_name)
        self.deleteEmptyFolders()


def msgWorkDone() -> None:
    '''
    Summons modal windows and locks root window

    Return: 
        None: Modal window

    '''
    if ent.path == '':
        return
    global pop
    pop = Toplevel(root)
    pop.tk.call("set_theme", "light")
    pop.title("Done!")
    pop.resizable(False, False)
    pop.grid_columnconfigure(0, weight=1)
    pop.grab_set()

    lblMsg = ttk.Label(pop,
                       text="Work done!")
    lblMsg.grid(row=0,
                padx=10,
                pady=(10, 0))

    btnMsg = ttk.Button(pop,
                        text="OK",
                        command=popDestroy)
    btnMsg.grid(row=1,
                padx=10,
                pady=(10, 10))


def popDestroy() -> None:
    pop.grab_release()
    pop.destroy()


if __name__ == "__main__":

    ent = UltraSort()
    root = Tk()
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.title("UltraSort")
    root.resizable(False, False)
    root.iconbitmap(True, 'icon.ico')

    lblHint = ttk.Label(root,
                        text="Directory: None, select one.")
    lblHint.grid(row=0,
                 column=0,
                 sticky="NSEW",
                 padx=10,
                 pady=[10, 10],
                 columnspan=2)

    btnFind = ttk.Button(root,
                         text="Browse Folder",
                         command=ent.getFolderPath,
                         width=30)
    btnFind.grid(row=2,
                 column=0,
                 sticky="NSEW",
                 padx=[10, 10],
                 pady=[0, 10])

    btnSort = ttk.Button(root,
                         text="Sort files by extension in subfolders",
                         command=ent.sortFileByExtension,
                         width=30)
    btnSort.grid(row=3,
                 column=0,
                 sticky="NSEW",
                 padx=[10, 10],
                 pady=[0, 10])

    btnDelete = ttk.Button(root,
                           text="Delete empty folders",
                           command=ent.deleteEmptyFolders,
                           width=30)
    btnDelete.grid(row=2,
                   column=1,
                   sticky="NSEW",
                   padx=[0, 10],
                   pady=[0, 10])

    btnSort1 = ttk.Button(root,
                          command=ent.sortFilesByType,
                          text="Sort files by type of file",
                          width=30)
    btnSort1.grid(row=3,
                  column=1,
                  sticky="NSEW",
                  padx=[0, 10],
                  pady=[0, 10])

    root.mainloop()
