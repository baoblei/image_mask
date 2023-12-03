# coding=utf-8
import cv2 as cv
import threading
import queue

flag_a = 0
flag_b = 0
def this_receive():
    global flag_a
    # URL='rtsp://192.168.8.88:554/av0_0'
    URL='rtsp://admin:abcd1234@192.168.8.108:8555/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif'
    cap = cv.VideoCapture(URL)
    
    while True:
        ret, next_frame = cap.read()
        if ret:
            # cv.imshow("xsc", next_frame)
            if flag_a:
                size = next_frame.shape
                w = size[1] #宽度
                h = size[0] #高度
                print(w,h)
                cv.imwrite(flag_a + '.jpg', next_frame)
                flag_a = 0
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            flag_b = 10086
            break


def lcd_program():
    global flag_a
    while True:
        if flag_b == 10086:
            break
        a = input("input:")
        flag_a = a
        print(flag_a)
        


if __name__ == '__main__':
    p2 = threading.Thread(target=this_receive)
    p2.start()
    p1 = threading.Thread(target=lcd_program)
    p1.start()
 




