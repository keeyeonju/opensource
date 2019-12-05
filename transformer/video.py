import cv2
class video:
    def __init__(self, address):
        self.address=address
        
    def videoOpen(self):
        import cv2
        cap=cv2.VideoCapture(self.address)
        if (cap.isOpened()==False):
            print("Error opening video stream or file")
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                cv2.imshow('Frame', frame)
                if cv2.waitKey(25) & 0xFF==ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        
    def videoCapture(self):
        import cv2
        cap=cv2.VideoCapture(self.address)
        if (cap.isOpened()==False):
            print("Error opening video stream or file")
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                cv2.imshow('Frame', frame)
                if cv2.waitKey(25) & 0xFF==ord('s'):
                    ret, frame = cap.read()
                    cv2.imwrite('capture_'+str(i)+'.jpg',frame)
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        
    def videoCut(self, format):
        import cv2
        cap = cv2.VideoCapture(self.address)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("size: {0} x {1}".format(320, 240))
        while cap.isOpened():
            success, frame = cap.read()
            if success:
                cv2.imshow('Video Window', frame) # 보여주기 part
                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break
                else:
                    break
        if(format == "avi"):
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            writer = cv2.VideoWriter(fileName+".avi", fourcc, 24, (int(width), int(height)))
        elif(format == "mp4"):
            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            writer = cv2.VideoWriter(fileName+".mp4", fourcc, 24, (int(width), int(height)))
        elif(format == "wmv"):
            fourcc = cv2.VideoWriter_fourcc(*'WMV2')
            writer = cv2.VideoWriter(fileName+".wmv", fourcc, 24, (int(width), int(height)))
        elif(format == "flv"):
            fourcc = cv2.VideoWriter_fourcc(*'KMV')
            writer = cv2.VideoWriter(fileName+".flv", fourcc, 24, (int(width), int(height))) 
        else:
            print("FILE EXT ERROR")
        while cap.isOpened():
            success, frame = cap.read()
            if success:
                writer.write(frame)
            else:
                break
        cap.release()
        writer.release()
        cv2.destroyAllWindows()
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