class Image_save:
    def __init__(self, file):
        self.file=file
    def save_jpg(self, title):
        save_title=title+".jpg"
        self.file.save(save_title)
        print("Successfully saved!")
    def save_png(self, title):
        save_title=title+".png"
        self.file.save(save_title)
        print("Successfully saved!")
    def save_tif(self, title):
        save_title=title+".tif"
        self.file.save(save_title)
        print("Successfully saved!")
    def save_bmp(self, title):
        save_title=title+".bmp"
        self.file.save(save_title)
        print("Successfully saved!")
