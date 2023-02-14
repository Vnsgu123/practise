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
e1=24
e2=26
count=0
ter=0
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
    GPIO.setup(e1, GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(e2, GPIO.IN,pull_up_down=GPIO.PUD_UP)

    # setting initial PWM frequency for all 4 pins
    L_MOTOR1 = GPIO.PWM(L_PWM_PIN1, 27) 
    R_MOTOR1 = GPIO.PWM(R_PWM_PIN1, 30)
    L_MOTOR2 = GPIO.PWM(L_PWM_PIN2, 30)
    R_MOTOR2 = GPIO.PWM(R_PWM_PIN2, 100)
    E1 = GPIO.PWM(ENA, 100) 
    E2 = GPIO.PWM(ENA1, 100) 

    # setting initial speed (duty cycle) for each pin as 0
    L_MOTOR1.start(0)
    R_MOTOR1.start(0)
    L_MOTOR2.start(0)
    R_MOTOR2.start(0)

def button_pressed_callback(channel):
    global count
    count=count+1 
    print("count! of encoder 1",count)
    #return count
def callw(channel):

    global ter
    ter=ter+1
    if ter > 38:
        R_MOTOR1.ChangeDutyCycle(0)                        
        L_MOTOR1.ChangeDutyCycle(0)
        cv2.waitKey(3000)
    print("count! of envcoder 2",ter)
    #return ter
def signal_handler(sig, frame):
	GPIO.cleanup()
	sys.exit(0)

def left(stream):
    # k=True 
    count1=ter
    count2=count
    # while k:
        # L_MOTOR1.ChangeDutyCycle(0)
        # R_MOTOR1.ChangeDutyCycle(50)
        # L_MOTOR2.ChangeDutyCycle(50)

        # if ter > count1 + 21:
            # print("cbuycUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
            # k=False
    L_MOTOR1.ChangeDutyCycle(0)
    R_MOTOR1.ChangeDutyCycle(0)
    
    R_MOTOR1.ChangeDutyCycle(43)
    L_MOTOR2.ChangeDutyCycle(43)
    stream1 = camera.capture_continuous(rawCapture,format="bgr", use_video_port=True)

    # R_MOTOR1.ChangeDutyCycle(0)
    # L_MOTOR2.ChangeDutyCycle(0)
    #cv2.waitKey(2000)
    for frame in stream:
        image1 = frame.array
        key = cv2.waitKey(1) & 0xFF
        #R_MOTOR1.ChangeDutyCycle(43)
        #L_MOTOR2.ChangeDutyCycle(43)
        gausss1 = cv2.GaussianBlur(image1,(5,5),0)

        gray1=cv2.cvtColor(gausss1, cv2.COLOR_BGR2GRAY)
        ret,thresh11 = cv2.threshold(gray1,100,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        #th31 = cv2.adaptiveThreshold(gray1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)


        # hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # gauss = cv2.GaussianBlur(hsv,(5,5),0)

        # low_b = np.array([0,0,168])
        # high_b = np.array([172,111,255])

        # mask = cv2.inRange(gauss, low_b, high_b)

        # out1 = cv2.bitwise_and(image,image, mask= mask)

        # out3 = cv2.bitwise_not(mask)


        contours, hierarchy = cv2.findContours(thresh11, 1, cv2.CHAIN_APPROX_NONE)


        c=max(contours,key=cv2.contourArea)
        approx1 = cv2.approxPolyDP(c, 0.01* cv2.arcLength(c, True), True)

        x1,y1,w1,h1=cv2.boundingRect(c)
        
        if w1 > 140 and w1 < 163 and h1 > 460 and h1 < 500 :
            print("fnrefuyrgfygfyruyerfyurevyfuehiujoifjwu9hfywiyfhu34ty4ikr3h   ",w1)
            R_MOTOR1.ChangeDutyCycle(0)
            L_MOTOR2.ChangeDutyCycle(0)
            cv2.destroyAllWindows()
            cv2.waitKey(8000)
            print("-delay for sprint  ------------------ 0dbufbhrh")
            break 

        print("area == ======================================================================================================================================================================== ",w,h,len(c) )

        cv2.drawContours(image1, [approx1], 0, (0, 255, 255), 5)
        cv2.imshow("new turn image",image1)
        cv2.imshow("kem cho ",thresh11)
        cv2.waitKey(3)
        rawCapture.truncate(0)
        if key == ord("q"):
            cv2.destroyAllWindows()
            GPIO.cleanup()
            break



# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 64
rawCapture = PiRGBArray(camera, size=(640, 480))
stream = camera.capture_continuous(rawCapture,format="bgr", use_video_port=True)
motor_pin_setup()
#L_MOTOR1.ChangeDutyCycle(39.6)
#R_MOTOR1.ChangeDutyCycle(42.8)
#p=40.225
#pp=41.8
p=37
pp=39
r=p
l=pp
prevtime=0
preverror=0
GPIO.add_event_detect(e1, GPIO.FALLING,callback=button_pressed_callback)
GPIO.add_event_detect(e2, GPIO.FALLING,callback=callw)
flag2=0
flag1=0
fag1=0
fag2=0
fag3=0
fag4=0
check=0
fag5=0
cap=0
# capture frames from the camera
for frame in stream:
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    key = cv2.waitKey(1) & 0xFF
    kk=image.shape
    #print("uevghdcegvfgyurgvuhefgyvierru8yfg7845gfuefcvergdiufg76refhgrugyrgwuyfewgf34fgur3fg6fg5h5fbuyeryfhejhfygrghejhgeggiu4h",kk)
    frame=image[:,:]
    # clear the stream in preparation for the next frame
    gausss = cv2.GaussianBlur(frame,(5,5),0)

    gray=cv2.cvtColor(gausss, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gauss = cv2.GaussianBlur(hsv,(5,5),0)
    #ret,thresh1 = cv2.threshold(gauss,100,255,cv2.THRESH_BINARY_INV)
    
    low_b = np.array([0,0,168])
    high_b = np.array([172,111,255])
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])
    mask = cv2.inRange(gauss, low_b, high_b)
    mask1 = cv2.inRange(gauss,yellow_lower,yellow_upper)
    #mask3 = cv2.inRange(thresh1, low_b, high_b)
    #out5 = cv2.bitwise_and(image,image, mask3= mask3)
    #out4 = cv2.bitwise_not(out5)
    out1 = cv2.bitwise_and(image,image, mask= mask)
    #contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE

    out2 = cv2.bitwise_and(image,image, mask= mask1)
    #contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE
    out3 = cv2.bitwise_not(mask)
   
    #out3 = cv2.GaussianBlur(out2,(5,5),0)

    contours, hierarchy = cv2.findContours(thresh1, 1, cv2.CHAIN_APPROX_NONE)
    #rawCapture.truncate(0)

    #left(stream,rawCapture)
    U=0
    contours1, hierarchy1 = cv2.findContours(mask1, 1, cv2.CHAIN_APPROX_NONE)
    #approx = cv2.approxPolyDP(c, 0.01* cv2.arcLength(c, True), True)

    c=max(contours,key=cv2.contourArea)
    approx = cv2.approxPolyDP(c, 0.01* cv2.arcLength(c, True), True)

    x,y,w,h=cv2.boundingRect(c)

    #print("area ==  ",w,h,len(c) )
    print("area == ======================================================================================================================================================================== ",w,h,len(c) )

    #approx = cv2.approxPolyDP(c, 0.01* cv2.arcLength(c, True), True)
    #x,y,w,h=cv2.boundingRect(c)
    cv2.drawContours(image, [approx], 0, (0, 255, 255), 5)
    #contours1, hierarchy1 = cv2.findContours(mask1, 1, cv2.CHAIN_APPROX_NONE)

    M = cv2.moments(c)
    flag3=0
    qq=0
    cv2.imshow('thresh1',thresh1)
    cv2.imshow('3',th3)

    #cv2.imshow('hsv',hsv)
    #cv2.imshow('mask',mask)
    #cv2.imshow('and',out)
    cv2.imshow('not',out2)
    #cv2.imshow('thresh',thresh1)
    #cv2.imshow('thresh mask',mask3)
    #cv2.imshow('thresh',)
    #cv2.imshow('thresh not',out4)
    #cv2.imshow('thresh and',out5)

    cv2.imshow('maitrey',image)
    if cap == 0:
        cv2.waitKey(3000)
        cap=1
    cv2.waitKey(3)

    if fag4==1:
        fag1=0
        fag2=0
        fag3=0
        fag4=0
    if fag5 ==0 :
        for contour in contours1:
            print("__________________------------------------------------------------------------2345-------------------------------------------------------------------------------------------------")
            flag3=1
            flag4=1
            R_MOTOR1.ChangeDutyCycle(0)
            L_MOTOR1.ChangeDutyCycle(0)
            cv2.waitKey(2000)
            print("egfygewfggffeywfiuehfjhroir8u893263trkhou099ruouhkegtugtiueyithto23how3wht3oith32oi ",count,ter)
            wer = 35 - count
            # print(len(contour))
            qq=qq+1
            approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
            # if len(contour) >2000:
            # 	flag=1
            cv2.drawContours(image, [approx], 0, (0, 0, 255), 5)
            M = cv2.moments(contour)
            if M["m00"] !=0 :
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
            if fag1 == 0:
                fag2=1
                fag1=1
            fag5=1
            break
            # cc=count
            # while count < cc +23:
            # print("ready to turn ")
            # left()
		
    if fag2 == 1:
        fag3 = 1
        #print("1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        check = count + wer
        #print("1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",check,count)
        fag2=0

    if M["m00"] !=0 :
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        print("CX : "+str(cx)+"  CY : "+str(cy))
        time.sleep(0.4)
    er=image.shape
    er=er[1]/2
    error=cx-er
    currtime=time.time()
    dt=currtime-prevtime
    dt=currtime-prevtime

    if ter > 38 and fag3 == 1:
        
        rawCapture.truncate(0)
        cv2.destroyAllWindows()

        left(stream)
        #GPIO.cleanup()
        #print("##################################################################################################################################")
        R_MOTOR1.ChangeDutyCycle(0)
        L_MOTOR1.ChangeDutyCycle(0)
        cv2.waitKey(2000)
        check=0
        fag3=0
        fag4=1

    if error > 20:
        print("move left ",error)

        pout=0.02*error
        de=error-preverror
        dout=0.0001*de/dt
        l=pp+pout+dout
        r=p-pout+dout
        if r > 48:
            r=48
        if l < 32:
            l=32
        if r < 32:
            r=32
        if l > 48:
            l=48
        #print("r l ========================================================================================================================================== ",r,l)

        R_MOTOR1.ChangeDutyCycle(r)
        L_MOTOR1.ChangeDutyCycle(l)
        time.sleep(0.0)
        # if count > check and fag3 == 1:
            # left()
            # fag3==0

    elif error < -20:
        print("move right ",error)
        error=-error
        pout=0.002*error
        de=error-preverror
        dout=0.0001*de/dt
        ll=pp-pout+dout
        rr=p+pout+dout
        if rr > 48:
            rr=48
        if ll < 32:
            ll=32
        if rr < 32:
            rr=32
        if ll > 48:
            ll=48
        #print("rr lll ====            ================================================================================================================== ",rr,ll)
        R_MOTOR1.ChangeDutyCycle(rr)
        L_MOTOR1.ChangeDutyCycle(ll)
        time.sleep(0.4)
        # if count > check and fag3 == 1:
            # left()
            # fag3==0
    else:
        
        R_MOTOR1.ChangeDutyCycle(p)
        L_MOTOR1.ChangeDutyCycle(pp)
        time.sleep(0.4)
        # if count > check and fag3 == 1:
            # left()
            # fag3==0
    


        
        
    print("error 000000000000000000=-99t8y45g",error)
    # for contour in contours:
        # x,y,w,h=cv2.boundingRect(contour)
        # M = cv2.moments(contour)
        # if M["m00"] !=0 :
            # cx = int(M['m10']/M['m00'])
            # cy = int(M['m01']/M['m00'])
            # #print("CX : "+str(cx)+"  CY : "+str(cy))
            # time.sleep(0.4)

        # if  w > 25 and w < 45 and h > 55 and h < 220 and len(contour) <500 and  len(contour) > 130 and cx > 15 and cx < 340:

            # x,y,w,h=cv2.boundingRect(contour)
            # print("hyyyyyyyyyyyyyyyyyyyyyyyyyy",x,y,w,h,len(contour))
            # approx = cv2.approxPolyDP(c, 0.01* cv2.arcLength(contour, True), True)
            # x,y,w,h=cv2.boundingRect(contour)
            # cv2.drawContours(image, [approx], 0, (0, 255, 255), 5)
            # M = cv2.moments(contour)

            # # if M["m00"] !=0 :
                # # cx = int(M['m10']/M['m00'])
                # # cy = int(M['m01']/M['m00'])
            # print("CX : "+str(cx)+"  CY : "+str(cy))
                # # time.sleep(0.4)

            # h=image.shape
            # print(h)
            # if cx < 290 :
                # print("right")
                # r=r-2
                # l=l+2
                # #R_MOTOR1.ChangeDutyCycle(r)
                # #L_MOTOR1.ChangeDutyCycle(l)
                # time.sleep(0.4)
                # #GPIO.output(L_PWM_PIN1,GPIO.HIGH)
                # #E1.ChangeDutyCycle(100)
                # r=p
                # l=pp
                # #GPIO.output(R_PWM_PIN1,GPIO.LOW)
                # #E2.ChangeDutyCycle(100)
            # elif cx > 330 :
                # print("left")
                # r=r+2
                # l=l-2
                # #R_MOTOR1.ChangeDutyCycle(r)
                # #L_MOTOR1.ChangeDutyCycle(l)
                # #GPIO.output(L_PWM_PIN1,GPIO.LOW)
                # #E1.ChangeDutyCycle(100)
                # r=p
                # l=pp

                # #GPIO.output(R_PWM_PIN1,GPIO.HIGH)
                # #E2.ChangeDutyCycle(100)
            # else :
                # print("qwduyqfd")
                # #R_MOTOR1.ChangeDutyCycle(r)
                # #L_MOTOR1.ChangeDutyCycle(l)
                # time.sleep(0.4)

                # #GPIO.output(L_PWM_PIN1,GPIO.HIGH)

                #GPIO.output(R_PWM_PIN1,GPIO.HIGH)

                
                




    preverror=error
    prevtime=currtime
    rawCapture.truncate(0)
    #cv2.imshow('maitrey',image)
    #cv2.imshow('mask',mask)
    #cv2.imshow('mask1',mask1)
    #cv2.imshow('out',out)
    cv2.waitKey(1)
    #rawCapture.truncate(0)

    # show the frame
    #cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
   
    
    # if the `q` key was pressed, break from the loop and close display window
    if key == ord("q"):
        cv2.destroyAllWindows()
        GPIO.cleanup()
        break
