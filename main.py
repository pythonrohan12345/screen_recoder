import numpy as np
import cv2
import pyautogui as gui

filename = input("enter filename: ")
cc = cv2.VideoWriter_fourcc(*"XVID")
screen = gui.size()
output = cv2.VideoWriter("C:\\Users\\rohan\\python\\screen_recoder\\"+filename+".avi",cc,20.0,screen)
while True:
    img = gui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output.write(frame)
    cv2.imshow("screen",frame)
    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()    
output.release()