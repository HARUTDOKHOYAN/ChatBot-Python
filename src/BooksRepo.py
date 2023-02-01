import os
from telebot import types
import config

CurrentFolder = ""


class File():
    def __init__(self, name, path):
        self.Name = name
        self.Path = path


class Folder ():
    def __init__(self, name, files, folders):
        self.Name = name
        self.Files = files
        self.Folders = folders


class Repository():

    def __init__(self):
        self.__book_directory = None

    def InitDirectory(self):
        self._book_directory = self._creatFolderTree(config.MainPath)

    def CreatFolderMarkups(self, name: str):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("<--Back"))
        folder = self.FindFolder(self._book_directory, name)
        if (folder.Folders == None):
            return markup
        for folder in folder.Folders:
            markup.add(types.KeyboardButton(folder.Name))
        return markup

    def FindFolder(self, rootFolder: Folder, name):
        if name == rootFolder.Name:
            return rootFolder
        if (rootFolder.Folders == None):
            return None
        for folder in rootFolder.Folders:
            result = self.FindFolder(folder, name)
            if (result != None):
                return result
        return None

    def GetFilesList(self, folderName):
        folder = self.FindFolder(self._book_directory , folderName)
        string = "---------------------------------\n"
        count = 1
        for file in folder.Files:
            string += str(count) + "." + file.Name + "\n"
            count += 1
        string += "---------------------------------"
        return string

    def FindParentFolder(self, name):
        return self._findParentFolder(name, self._book_directory)

    def IsConteinFolder(self, name):
        return self.FindFolder(self._book_directory, name) != None

    def _findParentFolder(self, name, rootFolder: Folder):
        if (rootFolder.Folders == None):
            return None
        for folder in rootFolder.Folders:
            if folder.Name == name:
                return rootFolder
        for folder in rootFolder.Folders:
            return self._findParentFolder(name, folder)
        return None

    def _creatFolderTree(self, path: str):
        splitPath = path.split(config.OsPath)
        folder = Folder(splitPath[len(splitPath) - 1], None, None)
        list_of_files = sorted(filter(lambda x: os.path.isfile(
            os.path.join(path, x)),  os.listdir(path)))
        folder.Files = list()
        for file in list_of_files:
            folder.Files.append(File(file, os.path.join(path, file)))
        list_of_dirs = sorted(filter(lambda x: os.path.isdir(
            os.path.join(path, x)),  os.listdir(path)))
        if (len(list_of_dirs) > 0):
            folder.Folders = list()
            for dir in list_of_dirs:
                folder.Folders.append(
                    self._creatFolderTree(os.path.join(path, dir)))
            return folder
        else:
            return folder
