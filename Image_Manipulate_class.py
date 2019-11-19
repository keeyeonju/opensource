class Image:
    def __init__(self, address,):
        self.address=address
    def openImage(self):
        from PIL import Image
        data=Image.open(self.address)
        print(data.size)
        return data
    def imageArray(self):
        from matplotlib import image
        from matplotlib import pyplot
        data=image.imread(self.address)
        print(data.dtype)
        print(data.shape)
        return pyplot.imshow(data)
    def resizeImage(self, x, y):
        from PIL import Image
        data=Image.open(self.address)
        print(data.size)
        data_resized=data.resize((x, y))
        print(data_resized.size)
        return data_resized
    def rotateImage(self, rotate):
        from PIL import Image
        from matplotlib import pyplot
        data=Image.open(self.address)
        pyplot.imshow(data.rotate(rotate))
        pyplot.show()
    def flipImage(self, direc):
        from PIL import Image
        from matplotlib import pyplot
        data=Image.open(self.address)
        if direc=="hoz":
            hoz_flip=data.transpose(Image.FLIP_LEFT_RIGHT)
            pyplot.imshow(hoz_flip)
        elif direc=="ver":
            ver_flip=data.transpose(Image.FLIP_TOP_BOTTOM)
            pyplot.imshow(ver_flip)
        else:
            print("Please insert either 'hoz' or 'ver'")
    def cropImage(self, x1, x2, y1, y2):
        from PIL import Image
        data=Image.open(self.address)
        cropped=data.crop((x1, x2, y1, y2))
        return cropped
