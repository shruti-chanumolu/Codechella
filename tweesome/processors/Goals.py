class Goals:
    def __init__(self,goalname, hashtag):
        self.goalname=goalname
        self.hashtag=hashtag
        self.trackInfo=None
        self.supportList=None


    def getSearchq(self):
        return self.hashtag