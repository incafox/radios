import cv2
import numpy as np
import time

#(b,g,r)
def analiza(pixel):
    print (pixel)
    b,g,r = pixel[0],pixel[1],pixel[2]
    b = b/1.6
    if ( (b >= g) and (b>=r) ):
        return True
    else:
        return False
    pass


def main():
    w = 160
    h = 120
    
    cap = cv2.VideoCapture('particmagnet.mp4')
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    #out = cv2.VideoWriter('tar.mpg',-1,1, (240,240))
    while ret:
        ret, frame = cap.read()
        #frame = cv2.resize(frame, (240, 240), interpolation = cv2.INTER_LINEAR) 
        #(channel_b, channel_g, channel_r) = cv2.split(frame)
        #frame = channel_r
        
        frame2 = frame 
        time.sleep(0.3)

        #ret,thresh1 = cv2.threshold(frame,117,255,cv2.THRESH_BINARY)
        #output1 = thresh1.reshape((frame.shape))
        cv2.imshow("Original", frame)
        #cv2.imshow("Quantized", output1)

        #out.write(frame)
        if cv2.waitKey(1) == 27: # exit on ESC
            break

    cv2.destroyAllWindows()
    cap.release()

#if __name__ == "__main__":
main()
#print (analiza((12,4,3)))