vcap = cv2.VideoCapture('small.mp4')
res, im_ar = vcap.read()
threshold=93.2
thumb_width=115
thumb_height=115
print(im_ar.mean())
while im_ar.mean() < threshold and res:
    res, im_ar = vcap.read()
    print(im_ar.mean())
im_ar = cv2.resize(im_ar, (thumb_width, thumb_height), 0, 0, cv2.INTER_LINEAR)
#to save we have two options
#1) save on a file
save_on_filename="trial"
cv2.imwrite(save_on_filename, im_ar)
#2)save on a buffer for direct transmission
res, thumb_buf = cv2.imencode('.png', im_ar)
# '.jpeg' etc are permitted
#get the bytes content
bt = thumb_buf.tostring()
