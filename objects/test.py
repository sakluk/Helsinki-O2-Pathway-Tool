import uuid

from objects.workLoadDetails import WorkLoadDetails

class Test(object):
    def __init__(self):
        self.id = uuid.uuid1()
        self.date = None
        self.data = None
        self.subjectDetails = None
        self.envDetails = None
        self.workLoadCount = None
        self.endWorkLoad = None
        self.workLoads = [] 

    def getWorkLoads(self):
        return self.workLoads

    def addWorkLoad(self, load):
        self.workLoads.append(load)

    def nWorkLoads(self):
        return len(self.workLoads)

    def initWorkLoad(self):
        newWorkLoadDetail = WorkLoadDetails(self)
        self.workLoads.append( newWorkLoadDetail )
        return newWorkLoadDetail