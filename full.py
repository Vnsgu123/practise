'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 3D of Pharma Bot (PB) Theme (eYRC 2022-23).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			socket_client_rgb.py
# Functions:
# 					[ Comma separated list of functions in this file ]

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv)                    ##
##############################################################
import socket
import time
import os
import sys
import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################


##############################################################
# initializing the pin numbers where motors are connected
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

def left(stream):
    for frame in stream:
        k=True 
        count1=ter
        while k:
            L_MOTOR1.ChangeDutyCycle(0)
            R_MOTOR1.ChangeDutyCycle(55)
            L_MOTOR2.ChangeDutyCycle(55)

            if ter > count1 + 10:
                print("cbuycUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
                k=False
                L_MOTOR1.ChangeDutyCycle(0)
                R_MOTOR1.ChangeDutyCycle(0)
                L_MOTOR2.ChangeDutyCycle(0)
                rawCapture.truncate(0)
                traversel(stream)
                faag1=1
        if faag1 == 1:
            break
    return

def right(stream):
    for frame in stream:
        kk=True 
        count11=ter
        while kk:
            L_MOTOR1.ChangeDutyCycle(55)
            R_MOTOR1.ChangeDutyCycle(0)
            L_MOTOR2.ChangeDutyCycle(0)
            R_MOTOR2.ChangeDutyCycle(55)

            if ter > count11 + 10:
                print("cbuycUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
                kk=False
                L_MOTOR1.ChangeDutyCycle(0)
                R_MOTOR1.ChangeDutyCycle(0)
                L_MOTOR2.ChangeDutyCycle(0)
                rawCapture.truncate(0)
                traversel(stream)
                faag1=1
        if faag1 == 1:
            break
    return

def straight(stream):
    for frame in stream:
        # kk=True
        # count11=ter
        # rawCapture.truncate(0)
        traversel(stream)
        faag1=1
        rawCapture.truncate(0)

        if faag1 == 1:
            break
    return
def wait(stream):
    L_MOTOR1.ChangeDutyCycle(0)
    R_MOTOR1.ChangeDutyCycle(0)
    print("wait")
    motor_pause(5)
def motor_pause(secs):
    L_MOTOR1.ChangeDutyCycle(0)
    R_MOTOR1.ChangeDutyCycle(0)
    L_MOTOR2.ChangeDutyCycle(0)
    R_MOTOR2.ChangeDutyCycle(0)
    time.sleep(secs)
    print(motor_pause)
def traversel():
    # camera = PiCamera()
    # camera.resolution = (640, 480)
    # camera.framerate = 32
    # rawCapture = PiRGBArray(camera, size=(640, 480))
    # stream = camera.capture_continuous(rawCapture,format="bgr", use_video_port=True)
    # motor_pin_setup()
    # L_MOTOR1.ChangeDutyCycle(39.6)
    #R_MOTOR1.ChangeDutyCycle(42.8)
    p=40.225
    pp=41.8
    r=p
    l=pp
    prevtime=0
    preverror=0
    GPIO.add_event_detect(e1, GPIO.FALLING,callback=button_pressed_callback, bouncetime=50)
    GPIO.add_event_detect(e2, GPIO.FALLING,callback=callw, bouncetime=50)
    flag2=0
    flag1=0
    fag1=0
    fag2=0
    fag3=0
    fag4=0
    check=0
    # capture frames from the camera
    for frame in stream:
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        key = cv2.waitKey(1) & 0xFF
        kk=image.shape
        print("uevghdcegvfgyurgvuhefgyvierru8yfg7845gfuefcvergdiufg76refhgrugyrgwuyfewgf34fgur3fg6fg5h5fbuyeryfhejhfygrghejhgeggiu4h",kk)
        frame=image[:,:]
        # clear the stream in preparation for the next frame
        out3 = cv2.GaussianBlur(frame,(5,5),0)

        hsv=cv2.cvtColor(out3, cv2.COLOR_BGR2HSV)
        low_b = np.array([0,0,168])
        high_b = np.array([172,111,255])
        yellow_lower = np.array([20, 100, 100])
        yellow_upper = np.array([30, 255, 255])
        mask = cv2.inRange(hsv, low_b, high_b)
        mask1 = cv2.inRange(hsv,yellow_lower,yellow_upper)
        #out = cv2.bitwise_and(image,image, mask= mask)
        #out1 = cv2.bitwise_and(image,image, mask= mask1)
        #contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE
        out2 = cv2.bitwise_not(mask)
        cv2.imshow('out3',out2)
        out3 = cv2.GaussianBlur(out2,(5,5),0)

        contours, hierarchy = cv2.findContours(out2, 1, cv2.CHAIN_APPROX_NONE)
        #rawCapture.truncate(0)

        #left(stream,rawCapture)
        U=0
        contours1, hierarchy1 = cv2.findContours(mask1, 1, cv2.CHAIN_APPROX_NONE)
        c=max(contours,key=cv2.contourArea)
        approx = cv2.approxPolyDP(c, 0.01* cv2.arcLength(c, True), True)
        x,y,w,h=cv2.boundingRect(c)
        cv2.drawContours(image, [approx], 0, (0, 255, 255), 5)
        contours1, hierarchy1 = cv2.findContours(mask1, 1, cv2.CHAIN_APPROX_NONE)

        M = cv2.moments(c)
        flag3=0
        qq=0
        if fag4==1:
            fag1=0
            fag2=1
            fag3=0
            fag4=0
        for contour in contours1:
            flag3=1
            flag4=1
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
            # cc=count
            # while count < cc +23:
                # print("ready to turn ")

            # left()
            
        if fag2 == 1:
            fag3 = 1
            #print("1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            check = count +28
            
            print("1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",check,count)
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
        if count > check and fag3 == 1:
            # left()
            return 
            #GPIO.cleanup()
            print("##################################################################################################################################")
            
            fag3=0
            fag4=1

        if error > 20:
            print("move left ",error)

            pout=0.02*error
            de=error-preverror
            dout=0.0001*de/dt
            l=pp+pout+dout
            r=p-pout+dout
            if r > 45:
                r=45
            if l < 35:
                l=35
            if r < 35:
                r=35
            if l > 45:
                l=45
            print("r l ==== ",r,l)

            R_MOTOR1.ChangeDutyCycle(r)
            L_MOTOR1.ChangeDutyCycle(l)
            time.sleep(0.0)
            # if count > check and fag3 == 1:
                # left()
                # fag3==0

        elif error < -20:
            print("move right ",error)
            error=-error
            pout=0.009*error
            de=error-preverror
            dout=0.0001*de/dt
            ll=pp-pout+dout
            rr=p+pout+dout
            if rr > 45:
                rr=45
            if ll < 35:
                ll=35
            if rr < 35:
                rr=35
            if ll > 45:
                ll=45
            print("rr lll ==== ",rr,ll)
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
        #rawCapture.truncate(0)
        cv2.imshow('maitrey',image)
        #cv2.imshow('mask',mask)
        #cv2.imshow('mask1',mask1)
        #cv2.imshow('out',out)
        cv2.waitKey(1)
        # rawCapture.truncate(0)

        # show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
    
        
        # if the `q` key was pressed, break from the loop and close display window
        if key == ord("q"):
            cv2.destroyAllWindows()
            GPIO.cleanup()
            break


def setup_client(host, port):
    """
    Purpose:
    ---
    This function creates a new socket client and then tries
    to connect to a socket server.

    Input Arguments:
    ---
    `host` :	[ string ]
            host name or ip address for the server

    `port` : [ string ]
            integer value specifying port name
    Returns:

    `client` : [ socket object ]
                a new client socket object
    ---


    Example call:
    ---
    client = setup_client(host, port)
    """

    client = None

    ################## ADD YOUR CODE HERE	##################
    # client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(client)
    print(host, port)
    client.connect((host, port))

    ##########################################################

    return client


def receive_message_via_socket(client):
    """
    Purpose:
    ---
    This function listens for a message from the specified
    socket connection and returns the message when received.

    Input Arguments:
    ---
    `client` :	[ socket object ]
            client socket object created by setup_client() function
    Returns:
    ---
    `message` : [ string ]
            message received through socket communication

    Example call:
    ---
    message = receive_message_via_socket(connection)
    """

    message = None

    ################## ADD YOUR CODE HERE	##################
    message = client.recv(256).decode('utf-8')

    ##########################################################

    return message


def send_message_via_socket(client, message):
    """
    Purpose:
    ---
    This function sends a message over the specified socket connection

    Input Arguments:
    ---
    `client` :	[ socket object ]
            client socket object created by setup_client() function

    `message` : [ string ]
            message sent through socket communication

    Returns:
    ---
    None

    Example call:
    ---
    send_message_via_socket(connection, message)
    """

    ################## ADD YOUR CODE HERE	##################
    msg = message.encode('utf-8')
    client.send(msg)

    ##########################################################

    ##########################################################
if __name__ == "__main__":

    host ="10.25.2.249"
    port = 5050
    #
    # 		##
    # 		redPin = 24
    # 		gndPin = 23
    # 		greenPin = 5
    # 		bluePin = 18
    #
    # 		## PWM values to be set for rgb led to display different colors
    # 		pwm_values = {"Red": (255, 0, 0), "Blue": (0, 0, 255), "Green": (0, 255, 0), "Orange": (255, 35, 0), "Pink": (255, 0, 122), "Sky Blue": (0, 100, 100)}
    #
    #
    # 		## Configure rgb led pins
    # 		rgb_led_setup()
    #
    #
        # Set up new socket client and connect to a socket server
    try:
        client = setup_client(host, port)

    except socket.error as error:
        print("Error in setting up server")
        print(error)
        sys.exit()

    # Wait for START command from socket_server_rgb.pys
    message = receive_message_via_socket(client)
    if message == "START":
        print("\nTask 3D Part 3 execution started !!")
    motor_pin_setup()
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    stream = camera.capture_continuous(rawCapture,format="bgr", use_video_port=True)

    while True:
        ## Receive message from socket_server_rgb.py
        # camera = PiCamera()
        # camera.resolution = (640, 480)
        # camera.framerate = 32
        # rawCapture = PiRGBArray(camera, size=(640, 480))
        # stream = camera.capture_continuous(rawCapture,format="bgr", use_video_port=True)

        message = receive_message_via_socket(client)

        ## If received message is STOP, break out of loop
        if message == "STOP":
            print("\nTask 3D Part 3 execution stopped !!")
            break
        else:
            print("Color received: " + message)
        if message == "LEFT":
            left(stream)
            # time.sleep(2)
            motor_pause(0.5)

        if message == "RIGHT":
            right(stream)
            # time.sleep(2)
            motor_pause(0.5)

        if message == "STRAIGHT":
            straight(stream)
            time.sleep(2)
            motor_pause(0.5)

        if message == "WAIT_5":
            wait()
            time.sleep(0.5)

    print("maitrey")
