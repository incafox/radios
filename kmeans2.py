import cv2
import numpy as np


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
    
    cap = cv2.VideoCapture('marcha.mpg')
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    out = cv2.VideoWriter('tar.mpg',-1,1, (240,240))
    while ret:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (240, 240), interpolation = cv2.INTER_LINEAR) 
        #(channel_b, channel_g, channel_r) = cv2.split(frame)
        #frame = channel_r
        
        frame2 = frame 
        #print (frame)
        for y in range(len(frame)):
            for x in range(len(frame[y])):
                if (analiza(frame[y][x]) and (x>40) and (y>40) and (x<(len(frame[0])-10) ) ):
                    cv2.circle(frame,(x,y), 8, (0,0,255), -1)

        #ret,thresh1 = cv2.threshold(frame,117,255,cv2.THRESH_BINARY)
        #output1 = thresh1.reshape((frame.shape))
        cv2.imshow("Original", frame)
        #cv2.imshow("Quantized", output1)

        out.write(frame)
        if cv2.waitKey(1) == 27: # exit on ESC
            break

    cv2.destroyAllWindows()
    cap.release()

#if __name__ == "__main__":
main()
#print (analiza((12,4,3)))