import numpy as np
import cv2

from darkflow.net.build import TFNet
print("[INFO] loading YOLO from disk...")
options = {"load": "yolo.weights","pbLoad": "yolo.pb", "metaLoad": "yolo.meta", "threshold": 0.5,"gpu":1.0}
tfnet = TFNet(options)

class detect:
    def __init__(self,imgPath):
        self.imgPath=imgPath
    def boxing(self,original_img, predictions):
        newImage = np.copy(original_img)
    
        for result in predictions:
            top_x = result['topleft']['x']
            top_y = result['topleft']['y']
    
            btm_x = result['bottomright']['x']
            btm_y = result['bottomright']['y']
    
            confidence = result['confidence']
            label = result['label'] + " " + str(round(confidence, 3))
            
            if confidence > 0.3:
                    newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255,0,0), 3)
                    newImage = cv2.putText(newImage, label, (top_x, top_y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.8, (0, 230, 0), 1, cv2.LINE_AA)
    
                    
    
        return newImage

    def recognise(self):
        original_img=cv2.imread(self.imgPath)
        results=tfnet.return_predict(original_img) 
        img=self.boxing(original_img, results)
        label_list=[]
        for i in results:
            label_list.append(i['label'])
        return label_list,img
        
        
