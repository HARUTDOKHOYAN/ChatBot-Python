from config import BotState


def FindPatern(doc):
    for Patern in PaternsList:
        if(Patern.Detect(doc)):
            return Patern.Name
    return BotState.FindPatern
class BasePatern():
    def __init__(self):
        self.name = None
    def Detect(doc):
        return None
class DocPatern(BasePatern):
    def __init__(self):
        super().__init__()
        self.name = "Doc"
class VasPatern(BasePatern):
    def __init__(self):
        super().__init__()
        self.name = "Vas"
PaternsList = []


PaternsList.append(DocPatern())
PaternsList.append(VasPatern())