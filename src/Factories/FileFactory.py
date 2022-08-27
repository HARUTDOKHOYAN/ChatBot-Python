from distutils.filelist import FileList


class Chapter(object):
    def __init__(self , name , filesList):
        self.Name = name
        self.FilesList = filesList
    def GetFile(self,name):
        return self.FilesList[name]
    def GetFilesList(self):
        string = "---------------------------------\n"
        count = 1
        for item in self.FilesList.keys():
            string += str(count)  + "." + item  + "\n"
            count+=1
        string += "---------------------------------"
        return string 

def GetChaptersLIst():
    string = "---------------------------------\n"
    count = 1
    for item  in DataChapters.values():
         string += str(count)  + "." + item.Name  + "\n"
         count+=1
    string += "---------------------------------"
    return string 

def GetAllFilesList():
    FileNamelist = []
    for chapter in DataChapters.values():
        FileNamelist.extend(chapter.FilesList.keys())
    return FileNamelist
    
def GetFilePath(text):
        for chapter in DataChapters.values():
             if text.lower() in chapter.FilesList:
                        return chapter.FilesList[text.lower()]
        return None


DataChapters = {}
DataChapters.update({"1" :Chapter('Lessons Books',{
                                                 "python": "PYTHON\\NLP\\TelegramBot\\BotEnams.py",
                                                 "model": "Mustang",
                                                 "year": 1964,
                                                 })})
DataChapters.update({"2" :Chapter('Programming Books',{})})
DataChapters.update({"3" :Chapter('Electronic Books',{})})
DataChapters.update({"4" :Chapter('Programing Files',{})})