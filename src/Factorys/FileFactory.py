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

DataChapters = {}
DataChapters.update({"1" :Chapter('Lessons Books',{
                                                 "brand": "Ford",
                                                 "model": "Mustang",
                                                 "year": 1964,
                                                 })})
DataChapters.update({"2" :Chapter('Programming Books',{})})
DataChapters.update({"3" :Chapter('Electronic Books',{})})
DataChapters.update({"4" :Chapter('Programing Files',{})})