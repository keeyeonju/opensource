class Youtube:
    def __init__(self, address):
        self.address=address
    def getTitle(self):
        import pafy
        video=pafy.new(self.address)
        return video.title
    def getRating(self):
        import pafy
        video=pafy.new(self.address)
        return video.rating
    def getDescription(self):
        import pafy
        video=pafy.new(self.address)
        print(video.description)
    def download(self):
        import pafy
        video=pafy.new(self.address)
        best=video.getbest()
        best.download(quiet=False)
        print("Successfully downloaded!")
