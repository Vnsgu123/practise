'''
    *****************************************************************************************
    *
    *        		===============================================
    *           		Pharma Bot (PB) Theme (eYRC 2022-23)
    *        		===============================================
    *
    *  This script is to implement Task 4B of Pharma Bot (PB) Theme (eYRC 2022-23).
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
# Filename:			task_4b.py
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
from zmqRemoteApi import RemoteAPIClient
import traceback
import zmq
import numpy as np
import cv2
from pyzbar.pyzbar import decode
import json
import random
import threading
##############################################################

# Import PB_theme_functions code
try:
    pb_theme = __import__('PB_theme_functions')

except ImportError:
    print('\n[ERROR] PB_theme_functions.py file is not present in the current directory.')
    print('Your current directory is: ', os.getcwd())
    print('Make sure PB_theme_functions.py is present in this current directory.\n')
    sys.exit()

except Exception as e:
    print('Your PB_theme_functions.py throwed an Exception, kindly debug your code!\n')
    traceback.print_exc(file=sys.stdout)
    sys.exit()

def task_4b_implementation(sim,maze):
    """
    Purpose:
    ---
    This function contains the implementation logic for task 4B

    Input Arguments:
    ---
    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    You are free to define additional input arguments for this function.

    Returns:
    ---
    You are free to define output parameters for this function.

    Example call:
    ---
    task_4b_implementation(sim)
    """

    ################## ADD YOUR CODE HERE	##################
    client = RemoteAPIClient()
    sim = client.getObject('sim')
    print("threading")
    maze_image = cv2.imread("config_image.png")
    t1 = threading.Thread(target=emulation, args=())
    t1.start()
    # t2 = threading.Thread(target=print_cube, args=(10,))
    traffic_signals, start_node, end_node = pb_theme.detect_all_nodes(maze_image)
    print(traffic_signals, start_node, end_node)
    path = pb_theme.detect_paths_to_graph(maze)
    print("uuuuytir")
    #traversel(path,traffic_signals,'F3','F2')
    time.sleep(5)

    # paths=pb_theme.path_planning(path, start_node, 'F2')
    # print(paths)
    # moves = pb_theme.paths_to_moves(paths, traffic_signals)
    # print(moves)
    # l=len(moves)
    # i=0
    # t1 = threading.Thread(target=emulation, args=())
    # t1.start()
    # time.sleep(2)
    # while l:
    # 	k=moves[i]
    # 	cv2.waitKey(5)
    # 	pb_theme.send_message_via_socket(connection_2,k)
    # 	cv2.waitKey(5)
    # 	i=i+1
    # 	l=l-1
    # 	time.sleep(2)
    # 	msg="null"
    # 	print("waiting")
    # 	#msg = pb_theme.receive_message_via_socket(connection_2)
    # 	while msg != "NEXT":
    # 		print("ha ha! ")
    # 		#emulation()
    # 		# cv2.waitKey(20)
    # 		# video = cv2.VideoCapture(0,cv2.CAP_DSHOW) # capturing the video from overhead camera
    # 		# cv2.waitKey(20)
    # 		# _, frame = video.read() # capturing individual frames
    # 		# #frame=frame[100:385,140:430]
    # 		# cv2.waitKey()
    # 		# cv2.imshow("Frameeee",frame) # displaying the captured frames
    # 		# cv2.waitKey(20)
    # 		print("end")
    # 		# #i=i+14.00e-02
    # 		# image=frame
    # 		# cv2.waitKey()
    # 		# cv2.imshow("gyuadf7we",image)
    # 		# cv2.waitKey()
    # 		# #scene_parameters =pb_theme.transform_values(image)
    # 		# #pb_theme.set_values(scene_parameters,sim)
    # 		# video.release()
    # 		# cv2.waitKey(2)
    # 		#video.release()
    # 		# image=frame
    # 		# scene_parameters = transform_values(image)

    # 		msg = pb_theme.receive_message_via_socket(connection_2)
    objectHandle = sim.getObject("/qr_plane")
    sim.setObjectInt32Param(objectHandle, 10, 1)
    time.sleep(2)
    m = sim.getObject("/Vision_sensor2")
    img, resX, resY = sim.getVisionSensorCharImage(m)
    time.sleep(3)

    # cv2.imshow('vidion',img)
    # cv2.waitKey(9000)
    # print(type(resX))
    # resX=resX-20
    # print(resX)
    img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 0)
    d = decode(img)
    time.sleep(3)

    sim.setObjectInt32Param(objectHandle, 10, 0)

    # print(d)
    # Dict ={}
    for i in d:
        # print(i.data)
        li = []
        k = i.data.decode('utf-8')
        print(k, "--------------------")
    res = json.loads(k)
    print(res, " 0uuuuuu ", type(res))
    m2 = sim.getObject("/Arena")
    m1 = sim.getObject("/delivery_tray")
    m3 = sim.getObject("/alphabot")

    position = sim.getObjectPosition(m1, m2)
    man1 = position[1]+0.0200
    man2 = position[1]-0.0200
    position1 = []
    position2 = []
    position1.append(position[0])
    position1.append(man1)
    position1.append(position[2])
    position2.append(position[0])
    position2.append(man2)
    position2.append(position[2])
    location1 = res['Orange_cone']
    drop1 = 'Orange_cone'
    # n = location1[1]
    location2 = res['Pink_cone']
    drop2 = 'Pink_cone'
    lens=len(res)
    u = 0
    flag=0
    for i in res:
        words = []
        print(i, "----------------------------------", res[i], type(i))
        i = str(i)
        z = '/'+i
        print("i = = ", i, '  ', type(i))
        o1 = sim.getObject(z)
        # m1=sim.getObject("/delivery_tray")
        # position=sim.getObjectPosition(m1,m2)
        if u == 0:
            sim.setObjectPosition(o1, m2, position)
            sim.setObjectParent(o1, m3, True)
            opp=i
            words = i.split('_')
            location1 = res[i]
            print("PICKED UP: ", words[0], " ", words[1], " ", location1)
            # words = i.split('_')
            print("words 0== ", words[0])
            pb_theme.send_message_via_socket(connection_2, words[0])
            msg1 = 'null'
            while msg1 != "NEXT":
                print("ha ha! ")
                # emulation()
                # cv2.waitKey(20)

                # video = cv2.VideoCapture(0,cv2.CAP_DSHOW) # capturing the video from overhead camera
                # cv2.waitKey(20)

                # _, frame = video.read() # capturing individual frames
                # #frame=frame[100:385,140:430]
                # cv2.waitKey()

                # cv2.imshow("Frameeee",frame) # displaying the captured frames
                # cv2.waitKey(20)

                # print("end")
                # #i=i+14.00e-02
                # image=frame
                # cv2.waitKey()

                # cv2.imshow("gyuadf7we",image)
                # cv2.waitKey()
                # #scene_parameters =pb_theme.transform_values(image)
                # #pb_theme.set_values(scene_parameters,sim)
                # video.release()
                # cv2.waitKey(2)
                # video.release()
                # image=frame
                # scene_parameters = transform_values(image)

                msg1 = pb_theme.receive_message_via_socket(connection_2)

            # pb_theme.send_message_via_socket(connection_2,words[0])

        if u == 1:
            sim.setObjectPosition(o1, m2, position1)
            sim.setObjectParent(o1, m3, True)
            # pb_theme.send_message_via_socket(connection_2,k)
            words1 = i.split('_')
            opp1=i
            location2 = res[i]
            print("PICKED UP: ", words1[0], " ", words1[1], " ", location2)

            print("words 1== ", words1[0])
            pb_theme.send_message_via_socket(connection_2, words1[0])
            msg1 = 'null'
            while msg1 != "NEXT":
                print("ha ha! ")
                # emulation()
                # cv2.waitKey(20)

                # video = cv2.VideoCapture(0,cv2.CAP_DSHOW) # capturing the video from overhead camera
                # cv2.waitKey(20)

                # _, frame = video.read() # capturing individual frames
                # #frame=frame[100:385,140:430]
                # cv2.waitKey()

                # cv2.imshow("Frameeee",frame) # displaying the captured frames
                # cv2.waitKey(20)

                # print("end")
                # #i=i+14.00e-02
                # image=frame
                # cv2.waitKey()

                # cv2.imshow("gyuadf7we",image)
                # cv2.waitKey()
                # #scene_parameters =pb_theme.transform_values(image)
                # #pb_theme.set_values(scene_parameters,sim)
                # video.release()
                # cv2.waitKey(2)
                # video.release()
                # image=frame
                # scene_parameters = transform_values(image)

                msg1 = pb_theme.receive_message_via_socket(connection_2)
        if u == 2:
            sim.setObjectPosition(o1, m2, position2)
            sim.setObjectParent(o1, m3, True)
            words2 = i.split('_')
            print("words 2== ", words2[0])
            location3 = res[2]
            print("PICKED UP: ", words2[0], " ", words2[1], " ", location2)

            pb_theme.send_message_via_socket(connection_2, words2[0])
            msg1 = 'null'
            while msg1 != "NEXT":
                print("ha ha! ")
                # emulation()
                # cv2.waitKey(20)

                # video = cv2.VideoCapture(0,cv2.CAP_DSHOW) # capturing the video from overhead camera
                # cv2.waitKey(20)

                # _, frame = video.read() # capturing individual frames
                # #frame=frame[100:385,140:430]
                # cv2.waitKey()

                # cv2.imshow("Frameeee",frame) # displaying the captured frames
                # cv2.waitKey(20)

                # print("end")
                # #i=i+14.00e-02
                # image=frame
                # cv2.waitKey()

                # cv2.imshow("gyuadf7we",image)
                # cv2.waitKey()
                # #scene_parameters =pb_theme.transform_values(image)
                # #pb_theme.set_values(scene_parameters,sim)
                # video.release()
                # cv2.waitKey(2)
                # video.release()
                # image=frame
                # scene_parameters = transform_values(image)

                msg1 = pb_theme.receive_message_via_socket(connection_2)
        if lens >= 3 and u == 2:
            print('mark3 ',words,words1,words2)

            traversel(path,traffic_signals, 'F2', location1)
            drop(location1, words,sim)
            traversel(path,traffic_signals, location1, location2)
            drop(location2, words1,sim)
            traversel(path,traffic_signals, location2, location3)
            drop(location2, words2,sim)
            if lens == 4:
                traversel(path,traffic_signals, location3, 'F2')
            else:
                traversel(path,traffic_signals, location3, 'end_node')
            flag = 1
        if u == 3:
            print('mark2 ',words,words1,words2)

            traversel(path,traffic_signals, 'F2', location1)
            drop(location1, words,sim)
            traversel(path,traffic_signals, location1, 'end_node')
            flag = 1

        u = u+1
    # location1 = res['Orange_cone']
    # drop1='Orange_cone'
    # #n = location1[1]
    # location2=res['Pink_cone']
    # drop2='Pink_cone'

    # rr=2-n
    # if rr < 0:
    # 	pb_theme.send_message_via_socket(connection_2,'Uturn')
    #     msg2='null'
    #     while msg2 != 'Next':
    #         msg2=pb_theme.receive_message_via_socket(connection_2)

    # print("location == ",location1,"k == ",type(k))
    # location2=res['Pink_cone']
    if flag == 0:
        traversel(path,traffic_signals, 'F2', location1)
        print('mark00 ',opp,opp1)
        drop(location1, opp,sim)
        traversel(path,traffic_signals, location1, location2)
        drop(location2, opp1,sim)
        print('mark0 ',words,words1)

        traversel(path,traffic_signals, location2, end_node)

    t1.join()
def traversel(path,traffic_signals, start_node, end_node):
    # traffic_signals, start_node, end_node =pb_theme.detect_all_nodes(maze_image)
    # print(traffic_signals, start_node, end_node)
    # path = pb_theme.detect_paths_to_graph(maze_image) 

    n = start_node[1]
    l = end_node[1]
    n = int(n)
    l = int(l)
    rr = n-l
    if rr < 0:
        pb_theme.send_message_via_socket(connection_2, 'Uturn')
        print("rukkkkkkkkkkkkkkkkkkkk")
        msg2 = 'null'
        while msg2 != 'NEXT':
            msg2 = pb_theme.receive_message_via_socket(connection_2)

    paths = pb_theme.path_planning(path, start_node, end_node)
    print(paths)
    moves = pb_theme.paths_to_moves(paths, traffic_signals)
    print(moves)
    l = len(moves)
    i = 0
    # t1 = threading.Thread(target=emulation, args=())
    # t1.start()
    time.sleep(3)
    while l:
        print("l ======================================================================== ", l)
        k = moves[i]
        cv2.waitKey(5)
        pb_theme.send_message_via_socket(connection_2, k)
        cv2.waitKey(5)
        i = i+1
        l = l-1
        time.sleep(2)
        msg = "null"
        print("waiting")
        # msg = pb_theme.receive_message_via_socket(connection_2)
        while msg != "NEXT":
            print("ha ha! ")
            # emulation()
            # cv2.waitKey(20)

            # video = cv2.VideoCapture(0,cv2.CAP_DSHOW) # capturing the video from overhead camera
            # cv2.waitKey(20)

            # _, frame = video.read() # capturing individual frames
            # #frame=frame[100:385,140:430]
            # cv2.waitKey()

            # cv2.imshow("Frameeee",frame) # displaying the captured frames
            # cv2.waitKey(20)

            # print("end")
            # #i=i+14.00e-02
            # image=frame
            # cv2.waitKey()

            # cv2.imshow("gyuadf7we",image)
            # cv2.waitKey()
            # #scene_parameters =pb_theme.transform_values(image)
            # #pb_theme.set_values(scene_parameters,sim)
            # video.release()
            # cv2.waitKey(2)
            # video.release()
            # image=frame
            # scene_parameters = transform_values(image)

            msg = pb_theme.receive_message_via_socket(connection_2)

def drop(drop_location, drop1,sim):
    print('drop1 === ',drop1," ",drop_location)
    q = drop_location[0]
    w = drop_location[1]
    default=-0.9610
    default=float(default)
    default1=-0.9670
    default=float(default1)

    if q == 'A':
        s = 0
    if q == 'B':
        s = 1
    if q == 'C':
        s = 2
    if q == 'D':
        s = 3
    if q == 'E':
        s = 4
    if q == 'F':
        s = 5
    if w == '1':
        e = 0
    if w == '2':
        e = 1
    if w == '3':
        e = 2
    if w == '4':
        e = 3
    if w == '5':
        e = 4
    if w == '6':
        e = 5
    s=float(s)
    e=float(e)
    x = default + (0.3550*s)
    y = default1 + 0.3550*e
    x=x
    y=-y
    pos=[] 
    pos.append(x)
    pos.append(y)
    pos.append(0)  # //check z value
    drop11='/'+drop1
    o1 = sim.getObject(drop11)
    m2 = sim.getObject("/Arena")
    sim.setObjectPosition(o1, m2, pos)
    sim.setObjectParent(o1, m2, True)
    drop1 = drop1.split('_')
    print("DELIVERED: ",drop1[0], " ", drop1[1], " ", "AT", ' ', drop_location)
    op = drop1[0]+'off'
    print("off ",op)
    pb_theme.send_message_via_socket(connection_2, op)
    msg5 = 'null'
    while msg5 != 'NEXT':
        print('ha bhai bhej')
        msg5 = pb_theme.receive_message_via_socket(connection_2)
        time.sleep(3)
        print(" MSG 5",msg5)

def emulation():
    while 1:
        # print("start")
        # video.release()
        # i=0
        # while i != 14 :
        # print("start")
        # video.release()
        # capturing the video from overhead camera
        video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        ku, frame = video.read()  # capturing individual frames
        # frame=frame[100:385,140:430]
        # print(ku)
        cv2.waitKey(4)
        # frame=frame[130:425,180:510]
        frame = frame[150:410, 196:480]

        cv2.imshow("Frameeee31231", frame)  # displaying the captured frames
        cv2.waitKey(3)

        # print("end")
        # i=i+1
        # image=frame
        # cv2.imshow("gyuadf7we1213",image)
        # cv2.waitKey(10000)
        scene_parameters = pb_theme.transform_values(frame)
        pb_theme.set_values(scene_parameters, coppelia_client)
        video.release()
        cv2.waitKey(5)
        # video.release()
        # image=frame
        # scene_parameters = transform_values(image)
        # set_values(scene_parameters)
        # cv2.destroyAllWindows()

    ##########################################################

if __name__ == "__main__":

    host = ''
    port = 5050

    print(socket.gethostbyname(socket.gethostname()))
    # Set up new socket server
    try:
        server = pb_theme.setup_server(host, port)
        print("Socket Server successfully created")

        # print(type(server))

    except socket.error as error:
        print("Error in setting up server")
        print(error)
        sys.exit()

    # Set up new connection with a socket client (PB_task3d_socket.exe)
    try:
        print("\nPlease run PB_socket.exe program to connect to PB_socket client")
        connection_1, address_1 = pb_theme.setup_connection(server)
        print("Connected to: " + address_1[0] + ":" + str(address_1[1]))

    except KeyboardInterrupt:
        sys.exit()

    # ## Set up new connection with Raspberry Pi
    try:
        print("\nPlease connect to Raspberry pi client")
        connection_2, address_2 = pb_theme.setup_connection(server)
        print("Connected to: " + address_2[0] + ":" + str(address_2[1]))

    except KeyboardInterrupt:
        sys.exit()

    # Send setup message to PB_socket
    pb_theme.send_message_via_socket(connection_1, "SETUP")

    message = pb_theme.receive_message_via_socket(connection_1)
    # Loop infinitely until SETUP_DONE message is received
    while True:
        if message == "SETUP_DONE":
            break
        else:
            print("Cannot proceed further until SETUP command is received")
            message = pb_theme.receive_message_via_socket(connection_1)

    try:
        # obtain required arena parameters
        config_img = cv2.imread("config_image.png")
        detected_arena_parameters = pb_theme.detect_arena_parameters(config_img)
        medicine_package_details = detected_arena_parameters["medicine_packages"]
        traffic_signals = detected_arena_parameters['traffic_signals']
        start_node = detected_arena_parameters['start_node']
        end_node = detected_arena_parameters['end_node']
        horizontal_roads_under_construction = detected_arena_parameters[
            'horizontal_roads_under_construction']
        vertical_roads_under_construction = detected_arena_parameters[
            'vertical_roads_under_construction']
        pths=detected_arena_parameters['paths']
        print(pths)
        # print("Medicine Packages: ", medicine_package_details)
        # print("Traffic Signals: ", traffic_signals)
        # print("Start Node: ", start_node)
        # print("End Node: ", end_node)
        # print("Horizontal Roads under Construction: ", horizontal_roads_under_construction)
        # print("Vertical Roads under Construction: ", vertical_roads_under_construction)
        # print("\n\n")

    except Exception as e:
        print('Your task_1a.py throwed an Exception, kindly debug your code!\n')
        traceback.print_exc(file=sys.stdout)
        sys.exit()

    try:

        # Connect to CoppeliaSim arena
        coppelia_client = RemoteAPIClient()
        sim = coppelia_client.getObject('sim')

        # Define all models
        all_models = []

        # Setting up coppeliasim scene
        print("[1] Setting up the scene in CoppeliaSim")
        all_models = pb_theme.place_packages(
            medicine_package_details, sim, all_models)
        all_models = pb_theme.place_traffic_signals(
            traffic_signals, sim, all_models)
        all_models = pb_theme.place_horizontal_barricade(
            horizontal_roads_under_construction, sim, all_models)
        all_models = pb_theme.place_vertical_barricade(
            vertical_roads_under_construction, sim, all_models)
        all_models = pb_theme.place_start_end_nodes(
            start_node, end_node, sim, all_models)
        print("[2] Completed setting up the scene in CoppeliaSim")
        print("[3] Checking arena configuration in CoppeliaSim")

    except Exception as e:
        print('Your task_4a.py throwed an Exception, kindly debug your code!\n')
        traceback.print_exc(file=sys.stdout)
        sys.exit()

    pb_theme.send_message_via_socket(connection_1, "CHECK_ARENA")

    # Check if arena setup is ok or not
    message = pb_theme.receive_message_via_socket(connection_1)
    while True:

        if message == "ARENA_SETUP_OK":
            print("[4] Arena was properly setup in CoppeliaSim")
            break
        elif message == "ARENA_SETUP_NOT_OK":
            print("[4] Arena was not properly setup in CoppeliaSim")
            connection_1.close()
            # connection_2.close()
            server.close()
            sys.exit()
        else:
            pass

    # Send Start Simulation Command to PB_Socket
    pb_theme.send_message_via_socket(connection_1, "SIMULATION_START")

    # Check if simulation started correctly
    message = pb_theme.receive_message_via_socket(connection_1)
    while True:
        # message = pb_theme.receive_message_via_socket(connection_1)

        if message == "SIMULATION_STARTED_CORRECTLY":
            print("[5] Simulation was started in CoppeliaSim")
            break

        if message == "SIMULATION_NOT_STARTED_CORRECTLY":
            print("[5] Simulation was not started in CoppeliaSim")
            sys.exit()

    # Send Start Command to Raspberry Pi to start execution
    pb_theme.send_message_via_socket(connection_2, "START")

    # emulation()
    task_4b_implementation(sim,config_img)

    # Send Stop Simulation Command to PB_Socket
    pb_theme.send_message_via_socket(connection_1, "SIMULATION_STOP")

    # Check if simulation started correctly
    message = pb_theme.receive_message_via_socket(connection_1)
    while True:
        # message = pb_theme.receive_message_via_socket(connection_1)

        if message == "SIMULATION_STOPPED_CORRECTLY":
            print("[6] Simulation was stopped in CoppeliaSim")
            break

        if message == "SIMULATION_NOT_STOPPED_CORRECTLY":
            print("[6] Simulation was not stopped in CoppeliaSim")
            sys.exit()
