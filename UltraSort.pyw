
import os
import shutil
from tkinter import Tk, Toplevel, filedialog, ttk

IMAGE_EXT = ['psd', 'webp', 'bmp', 'tif', 'jpg', 'ico', 'jpg',
             'png', 'ai', 'tiff', 'png', 'jpeg', 'heic', 'svg', 'gif']

VIDEO_EXT = ['mp4', 'webm', 'webm', 'mkv']

DOCUMENT_EXT = ['doc', 'key', 'pdf', 'xlsx', 'pps', 'pptx',
                'xls', 'docx', 'pdf', 'txt', 'docx', 'mpp', 'odp', 'ppt']

AUDIO_EXT = ['mp3', 'wav', 'flac', 'aif',
             'cda', 'mid', 'mpa', 'ogg', 'wma', 'wpl', 'mpeg']

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

# TODO msgError Fnction


class UltraSort():
    def __init__(self) -> None:
        self.path = ''

    def __repr__(self) -> str:
        return f"{self.path}"
    
    def __str__(self) -> str:
        return f"Path: {self.path}"

    def get_path(self):
        return self.path

    def set_path(self, newPath):
        self.path = newPath

    def _flattenList(self, list_to_flatten: list) -> list:
        """funtion to to unpack list of lists in to single list

        Args:
            list_to_flatten (list): list of lists to unpack

        Returns:
            list: list
        """

        return [item for sublist in list_to_flatten for item in sublist]

    def getFolderPath(self) -> None:
        """Path selector.

        Returns:
            None: Ask for directory, and sets it to path.
        """
        self.path = filedialog.askdirectory()
        if (os.path.isdir(self.path)):
            lblHint['text'] = ("Directory: " + str(ent.path))

    def deleteEmptyFolders(self) -> None:
        """Deletes empty folders in attribute path.

        Returns:
            None: In path deletes all empty folders and in subfolders
        """
        if (os.path.isdir(self.path)):
            local_path = self.path

            walk = list(os.walk(local_path))

            for walk_path, _, _ in walk[::-1]:
                if len(os.listdir(walk_path)) == 0:
                    os.rmdir(walk_path)
            msgWorkDone()

    def sortFileByExtension(self) -> None:
        """Sorts files in path by extension type.

        Return:
            None: In the path, sorts all files by extension and moves them to the appropriate folders.
            If there is no such folder, creates one.        
        """
        if (os.path.isdir(self.path)):
            localPath = self.path
            listOfFiles = os.listdir(localPath)
            for files in listOfFiles:
                fileName, fileExtetion = os.path.splitext(files)
                fileExtetion = fileExtetion[1:]
                if fileExtetion in UltraSort._flattenList(self, TYPE_LIST):
                    if not (os.path.isdir(f"{localPath}/{fileExtetion}")):
                        os.mkdir(f"{localPath}/{fileExtetion}")
                    shutil.move(f"{localPath}/{files}",
                                f"{localPath}/{fileExtetion}")
            msgWorkDone()
        else:
            msgError()

    def sortFilesByType(self) -> None:
        """Sorts files in path by general type.

        Return
            None: In path sorts all files by type and moves to according folders.
            If no such folders exits, creates it. 
        """
        if (os.path.isdir(self.path)):
            localPath = self.path
            listOfFiles = os.listdir(localPath)
            for types in TYPE_LIST:
                types_name = TYPE_LIST_NAME[TYPE_LIST.index(types)]
                for files in listOfFiles:
                    fileName, fileExtetion = os.path.splitext(files)
                    fileExtetion = fileExtetion[1:]
                    if fileExtetion in types:
                        if not (os.path.isdir(f"{localPath}/{types_name}")):
                            os.mkdir(f"{localPath}/{types_name}")
                        shutil.move(f"{localPath}/{files}",
                                    f"{localPath}/{types_name}")
            msgWorkDone()
        else:
            msgError()


def msgWorkDone(text: str = "Work done!") -> None:
    '''
    Summons modal windows and locks root window

    Return: 
        None: Modal window

    '''
    if ent.path == '':
        return
    pop = Toplevel(root)
    pop.tk.call("set_theme", "light")
    pop.title(text)
    pop.resizable(False, False)
    pop.grid_columnconfigure(0, weight=1)
    pop.grab_set()

    lblMsg = ttk.Label(pop,
                       text=text)
    lblMsg.grid(row=0,
                padx=10,
                pady=(10, 0))

    btnMsg = ttk.Button(pop,
                        text="OK",
                        command=lambda: popDestroy(pop))
    btnMsg.grid(row=1,
                padx=10,
                pady=(10, 10))


def popDestroy(pop) -> None:
    pop.grab_release()
    pop.destroy()


def msgError():
    msgWorkDone("Erorr: Somthing goes wrong")


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
