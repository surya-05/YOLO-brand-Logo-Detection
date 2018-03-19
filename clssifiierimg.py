import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import operator
import matplotlib.pyplot as plt
options = {
    "model":"cfg/yolo-voc.2.0.cfg",
    "load":"bin/YOLOv2_logo_detection_10000th_iteration.weights",
    "thrsehold":0.8
}
#{'label': 'Samsung_Store', 'bottomright': {'x': 389, 'y': 447},
# 'confidence': 0.55634993, 'topleft': {'x': 0, 'y': 179}}
tfnet=TFNet(options)
img=cv2.imread('smirnoff_testing/hp26.jpg')
img1=cv2.imread('smirnoff_testing/hp26.jpg',cv2.IMREAD_COLOR)
result=tfnet.return_predict(img)
print(result)
tl=(result[0]['topleft']['x'],result[0]['topleft']['y'])
br=(result[0]['bottomright']['x'],result[0]['bottomright']['y'])
label=result[0]['label']
img=cv2.rectangle(img,tl,br,(0,255,0),7)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()









'''

colors=[tuple(255* np.random.rand(3)) for _ in range(10)]
capture=cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
while True:
    stime=time.time()
    ret,frame=capture.read()
    results=tfnet.return_predict(frame)
    if ret:
        for color,result in zip(colors,results):
            tl=(result['topleft']['x'],result['topleft']['y'])
            br=(result['bottomright']['x'],result['bottomright']['y'])
            label=result['label']
            cofidence=result['confidence']
            text='{}:{:.0f}%'.format(label,cofidence*100)
            frame=cv2.rectangle(frame,tl,br,color,5)
            frame=cv2.putText(frame,text,tl,cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
                
                
        cv2.imshow('frame',frame)
'''
