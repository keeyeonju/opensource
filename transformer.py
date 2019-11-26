import cv2
import os

##video class##
class video:
    def video_cv2():
        string = input().split()
        fileName = os.path.splitext(string[0])[0]
        ext = string[1]
        print(fileName,ext)
        cap = cv2.VideoCapture(string[0])

        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("size: {0} x {1}".format(320, 240))
        
        # 영상 저장을 위한 VideoWriter 인스턴스 생성


        while cap.isOpened():
            success, frame = cap.read()
            if success:
                cv2.imshow('Video Window', frame) # 보여주기 part
        
                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break
            else:
                break

        if(ext == "avi"):
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            writer = cv2.VideoWriter(fileName+".avi", fourcc, 24, (int(width), int(height)))
        elif(ext == "mp4"):
            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            writer = cv2.VideoWriter(fileName+".mp4", fourcc, 24, (int(width), int(height)))
        elif(ext == "wmv"):
            fourcc = cv2.VideoWriter_fourcc(*'WMV2')
            writer = cv2.VideoWriter(fileName+".wmv", fourcc, 24, (int(width), int(height)))
        elif(ext == "flv"):
            fourcc = cv2.VideoWriter_fourcc(*'KMV')
            writer = cv2.VideoWriter(fileName+".flv", fourcc, 24, (int(width), int(height))) 
        elif(ext == "mov"):
            fourcc = cv2.VideoWriter_fourcc(*'BMP')
            writer = cv2.VideoWriter(fileName+".mov", fourcc, 24, (int(width), int(height)))
        elif(ext == "asf"):
            fourcc = cv2.VideoWriter_fourcc(*'DIVX')
            writer = cv2.VideoWriter(fileName+".asf", fourcc, 24, (int(width), int(height)))   
        else:
            print("FILE EXT ERROR")
        while cap.isOpened():
            success, frame = cap.read()
            if success:
                writer.write(frame)  # 프레임 저장
            else:
                break

        
        cap.release()
        writer.release()  # 저장 종료
        cv2.destroyAllWindows()