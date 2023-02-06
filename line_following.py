# import the necessary packages
import picamera
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import RPi.GPIO as GPIO


L_PWM_PIN1 = 38
L_PWM_PIN2 = 40
R_PWM_PIN2 = 32
R_PWM_PIN1 = 33
ENA = 31
ENA1 =37

# declare motor pins as output pins
# motors get input from the PWM pins
def motor_pin_setup():
    global L_MOTOR1, L_MOTOR2, R_MOTOR1, R_MOTOR2,E1,E2
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(R_PWM_PIN1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(R_PWM_PIN2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(L_PWM_PIN1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(L_PWM_PIN2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(ENA1, GPIO.OUT, initial=GPIO.HIGH)

    # setting initial PWM frequency for all 4 pins
    L_MOTOR1 = GPIO.PWM(L_PWM_PIN1, 100) 
    R_MOTOR1 = GPIO.PWM(R_PWM_PIN1, 100)
    L_MOTOR2 = GPIO.PWM(L_PWM_PIN2, 100)
    R_MOTOR2 = GPIO.PWM(R_PWM_PIN2, 100)
    E1 = GPIO.PWM(ENA, 100) 
    E2 = GPIO.PWM(ENA1, 100) 

    # setting initial speed (duty cycle) for each pin as 0
    L_MOTOR1.start(0)
    R_MOTOR1.start(0)
    L_MOTOR2.start(0)
    R_MOTOR2.start(0)



# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
stream = camera.capture_continuous(rawCapture,format="bgr", use_video_port=True)
motor_pin_setup()
R_MOTOR1.ChangeDutyCycle(5.8)
L_MOTOR1.ChangeDutyCycle(5.6)

time.sleep(0.2)

prevtime=0
preverror=0
q=0

# capture frames from the camera
for frame in stream:
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    img = frame.array
    k=img.shape
    print("k ====",k[1])
    image = img
    key = cv2.waitKey(1) & 0xFF
    
    # clear the stream in preparation for the next frame
    hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    low_b = np.array([0,0,168])
    high_b = np.array([172,111,255])
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, low_b, high_b)
    mask1 = cv2.inRange(hsv,yellow_lower,yellow_upper)
    out = cv2.bitwise_and(image,image, mask= mask)
    out1 = cv2.bitwise_and(image,image, mask= mask1)
    contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)
    print("patelllll")
    #rawCapture.truncate(0)

    #left(stream,rawCapture)
    U=0
    contours1, hierarchy1 = cv2.findContours(mask1, 1, cv2.CHAIN_APPROX_NONE)
    m=k[1]/2
    for contour in contours:
        x,y,w,h=cv2.boundingRect(contour)
        if len(contour) >50 and len(contour) < 650 and w < 90 and w > 19 and  h > 20 and h < 300:
        
           if q ==0 :
               q=1
               R_MOTOR1.ChangeDutyCycle(5.8)
               L_MOTOR1.ChangeDutyCycle(5.6)

               time.sleep(0.2)


               L_MOTOR1.ChangeDutyCycle(10.6)
               R_MOTOR1.ChangeDutyCycle(10.8)
               time.sleep(0.2)


               R_MOTOR1.ChangeDutyCycle(20.8)
               L_MOTOR1.ChangeDutyCycle(20.6)

               time.sleep(0.2)
               R_MOTOR1.ChangeDutyCycle(33.8)               
               L_MOTOR1.ChangeDutyCycle(33.6)
               #R_MOTOR1.ChangeDutyCycle(33.8)
               time.sleep(0.2)

               #R_MOTOR1.ChangeDutyCycle(39.65)
               R_MOTOR1.ChangeDutyCycle(39.65)
               L_MOTOR1.ChangeDutyCycle(42.6)
               #R_MOTOR1.ChangeDutyCycle(39.65)


               p=39.65
               pp=42.6
               r=p
               l=pp
               rr=p
               ll=pp

           #x,y,w,h=cv2.boundingRect(contour)
           print("hyyyyyyyyyyyyyyyyyyyyyyyyyy",x,y,w,h,len(contour))
           approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
           x,y,w,h=cv2.boundingRect(contour)
           cv2.drawContours(image, [approx], 0, (0, 255, 255), 5)
           flag1=0
           M = cv2.moments(contour)
           if M["m00"] !=0 :
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                print("CX : "+str(cx)+"  CY : "+str(cy))
           error=cx-m
           currtime=time.time()

           dt=currtime-prevtime

           de=error - preverror
           if dt > 0.0001:
               flag1 = 1
               #dt=currtime-prevtime
               dout=0.0001*de/dt
               #dout=0
               pout=0.02*error
               #if pout > 4:
               #pout=4
               #if pout < -4:
               #pout=-4
               print("------------------------------------------------------------------------------------------",de,"---",dt,"----",dout ,"  ",pout," ++++++++++ ",m)

           if cx-m > 10  and flag1 ==1:
                print("move right",error)
                #GPIO.output(L_PWM_PIN1,GPIO.HIGH)
                #E1.ChangeDutyCycle(100)

                #GPIO.output(R_PWM_PIN1,GPIO.LOW)
                #E2.ChangeDutyCycle(100)
                # k=cx-m
                # r=r-k*0.78
                # l=l+k*0.78
                # if rr > 100:
                    # rr=100
                # if ll > 100:
                    # ll=100
                w=cx-m
                r=r-pout + dout
                l=l+pout + dout
                if r > 100:
                    r=100
                if l < 0:
                    l=0
                if r < 0:
                    r=0
                if l > 100:
                    l=100
                print(rr,ll,cx ,error,"-------------###################################################################################################+")

                #R_MOTOR1.ChangeDutyCycle(r)
                L_MOTOR1.ChangeDutyCycle(l)
                time.sleep(0.01)
                
                r=p
                l=pp

           elif cx-m < -10 and flag1 == 1:
                print("move left",error)
                #GPIO.output(L_PWM_PIN1,GPIO.LOW)
                #E1.ChangeDutyCycle(100)

                #GPIO.output(R_PWM_PIN1,GPIO.HIGH)
                #E2.ChangeDutyCycle(100)
                # kk=cx-m
                # rr=rr+kk*0.78
                # ll=ll-kk*0.78
                # if rr > 100:
                    # rr=100
                # if ll > 100:
                    # ll=100
                q=m-cx
                rr=rr-pout + dout
                ll=ll+pout + dout
                if ll >= 100 :
                    ll = 99
                if ll < 0:
                    ll=0
                if rr >= 100:
                    rr = 99
                if rr < 0:
                    rr =0
                print(rr,ll,cx ,error,"-------------###################################################################################################+")
                R_MOTOR1.ChangeDutyCycle(rr)
                #L_MOTOR1.ChangeDutyCycle(ll)
                time.sleep(0.01)

                rr=p
                ll=pp



                # L_MOTOR2.ChangeDutyCycle(42)
                # R_MOTOR2.ChangeDutyCycle(38)
            
           else:
                print("move straight")
                #GPIO.output(L_PWM_PIN2,GPIO.HIGH)
                #E1.ChangeDutyCycle(100)

                #GPIO.output(R_PWM_PIN2,GPIO.HIGH)
                #E2.ChangeDutyCycle(100)
                L_MOTOR1.ChangeDutyCycle(pp)
                R_MOTOR1.ChangeDutyCycle(p)
                time.sleep(0.01)


           preverror=error
           prevtime=currtime   
           #time.sleep(1)
                





    rawCapture.truncate(0)
    cv2.imshow('maitrey',img)
    #cv2.imshow('mask',mask)
    #cv2.imshow('mask1',mask1)
    #cv2.imshow('out',out)
    cv2.waitKey(1)
    rawCapture.truncate(0)

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
   
    
    # if the `q` key was pressed, break from the loop and close display window
    if key == ord("q"):
        cv2.destroyAllWindows()
        break

