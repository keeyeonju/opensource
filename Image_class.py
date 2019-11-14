class Image:
    def __init__(self, address, size_x, size_y, rotate, crop_x, crop_y):
        self.address=address
        self.func=func
        self.size_x=size_x
        self.size_y=size_y
        self.rotate=rotate
        self.crop_x=crop_x
        self.crop_y=crop_y
    def openImage(self):
        data=Image.open(self.address)
        data.show()
        print(data.size)
        return data
    def resizeImage(self):
        a=self.size_x
        b=self.size_y
        data_resized=data.resize(a, b)
        return data_resized
    def rotateImage(self):
        a=self.rotate
        pyplot.imshow(data.rotate(a))
    def cropImage(self):
        
