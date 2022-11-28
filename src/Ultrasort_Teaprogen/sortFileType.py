"""File selection dialog classes.

Classes:

- FileDialog
- LoadFileDialog
- SaveFileDialog

This module also presents tk common file dialogues, it provides interfaces
to the native file dialogues available in Tk 4.2 and newer, and the
directory dialogue available in Tk 8.3 and newer.
These interfaces were written by Fredrik Lundh, May 1997.
"""
__all__ = [
    "FileTypeExtension",
]


class FileTypeExtension:
    IMAGE_EXT = [
        "psd",
        "webp",
        "bmp",
        "tif",
        "jpg",
        "ico",
        "jpg",
        "png",
        "ai",
        "tiff",
        "png",
        "jpeg",
        "heic",
        "svg",
        "gif",
    ]

    VIDEO_EXT = ["mp4", "webm", "webm", "mkv", "mpeg"]

    DOCUMENT_EXT = [
        "doc",
        "key",
        "pdf",
        "xlsx",
        "pps",
        "pptx",
        "xls",
        "docx",
        "pdf",
        "txt",
        "docx",
        "mpp",
        "odp",
        "ppt",
    ]

    AUDIO_EXT = [
        "mp3",
        "wav",
        "flac",
        "aif",
        "cda",
        "mid",
        "mpa",
        "ogg",
        "wma",
        "wpl",
        "mpeg",
    ]

    COMPRESSED_EXT = ["rar", "tar", "zip", "7z", "pkg", "z"]

    FONT_EXT = ["fnt", "fon", "otf", "ttf"]

    INTERNET_EXT = ["html", "css", "torrent", "php", "htm"]

    DATA_EXT = [
        "siq",
        "csv",
        "dat",
        "db",
        "dbf",
        "log",
        "mdb",
        "sav",
        "sql",
        "xml",
        "json",
    ]

    EXECUTABLE_EXT = ["exe", "bat", "bin", "com", "jar", "msi", "wsf"]

    TYPE_LIST = [
        IMAGE_EXT,
        VIDEO_EXT,
        DOCUMENT_EXT,
        AUDIO_EXT,
        COMPRESSED_EXT,
        FONT_EXT,
        INTERNET_EXT,
        DATA_EXT,
        EXECUTABLE_EXT,
    ]

    TYPE_LIST_NAME = [
        "Images",
        "Videos",
        "Documents",
        "Audio",
        "Archives",
        "Fonts",
        "Internet files",
        "Data files",
        "Executable files",
    ]
