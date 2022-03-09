import os
import socket
import json
from time import sleep

import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import tools

UDP_IP = "192.168.162.129"
UDP_PORT = 5015
index = 0
index1 = 0


dict = {}
i=0

distance_list = []
p1 = tools.Point(0,0) # coordinate of ESP 1
p2 = tools.Point(1,3) # coordinate of ESP 2
p3 = tools.Point(5,2) # coordinate of ESP 3
TRY_DISTANCE_STEP = 0.01

def avgrrsi(init_df , ip , mac):
    init_df = init_df[['IP', 'Mac', 'Rssi']]
    init_df = init_df[-20:]
    final_df = init_df.groupby(['IP', 'Mac']).mean()
    final_df = final_df.loc[(ip,mac)]
    print(final_df['Rssi'])
    return final_df['Rssi']

# def extractavgrssi (init_df , ip , mac):
#     print(init_df)
#     print(type(init_df))
#     print(init_df['IP'])
#     final_df = init_df.loc[init_df['IP'] == ip]
#     final_df = init_df.loc[init_df['Mac'] == mac]
#     return final_df['Rssi'].values[0]

def calculate(init_df):
    #init_df['Distance'] = pow(10, ((-69 - init_df['Rssi']) / (16)))
    init_df['Distance'] = (0.882909233) * pow((init_df['Rssi'] / -58), 4.57459326) + 0.045275821
    init_df = init_df[['IP', 'Mac', 'Distance']]
    init_df = init_df[-20:]
    final_df = init_df.groupby(['IP', 'Mac']).mean()
    return final_df

def cleardataframe(df):
    #clear data from 50 sec el kdom
    t1 = datetime.now()
    t1 = t1.time().second
    index_names = df[t1 - df['Time'].time().second < 50].index
    df.drop(index_names, inplace=True)
    os.system('clear')
    print(df)

class beacon:
    url: str
    rssi: int
    mac: str
    ip : str
    def __init__(self, data: dict):
        self.url = data['URL']
        self.rssi = data['RSSI']
        self.mac = data['Mac']
        self.time = datetime.now()
        self.ip = data['IP']

    def __repr__(self):
        return (f' URL={self.url}            rssi= {self.rssi} mac={self.mac} ip={self.ip}')


sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))


#t1 = datetime.now()
#while (datetime.now()-t1).seconds <= 5:  #run for 5 seconds
while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    # print("Type:", type(data))
    # print("received message: %s" % data)
    try:
        datadict = json.loads(data.decode())
        beac = beacon(datadict)

        b_url = beac.url
        b_rssi = beac.rssi
        b_mac = beac.mac
        b_time = beac.time
        b_ip = beac.ip
        b_data = []
        b_data.extend([b_ip,b_url,b_rssi,b_mac,b_time])

        # Mac address list of ESP
        list_esp = ["24:0a:c4:ee:35:b6" , "24:6f:28:0b:9b:fe"]
        # Ignore ESP
        if b_mac in list_esp:
            continue

        dict[i] = b_data
        i = i+1

        df = pd.DataFrame.from_dict(dict, orient="index", columns=['IP', 'URl', 'Rssi', 'Mac', 'Time'])
        os.system('clear')

        #calculate avg rssi and filter
        avg_rssi_val = avgrrsi(df, b_ip, b_mac)

        print(df)
        print(avg_rssi_val)

        if (abs(b_rssi - avg_rssi_val) > 5) and (i > 10):
            print(b_rssi - avg_rssi_val)
            del dict[i-1]
            f_df = df.drop(i - 1 , axis=0)
            print("*")
            df = f_df.copy()

        print("after drop" , df)

        df = calculate(df)
        #cleardataframe(df)

        print("final " , df)

        distance_list = df['Distance'].tolist()
        print(distance_list)

        circle1 = tools.Circle(p1, distance_list[0])
        circle2 = tools.Circle(p2, distance_list[1])
        circle3 = tools.Circle(p3, distance_list[2])

        circle11 = plt.Circle((p1.x, p1.y), circle1.r, color='b', fill=False)
        circle22 = plt.Circle((p1.x, p1.y), circle2.r, color='b', fill=False)
        circle33 = plt.Circle((p1.x, p1.y), circle3.r, color='b', fill=False)

        fig, ax = plt.subplots()
        ax.set_xlim((-10, 10))
        ax.set_ylim((-10, 10))
        ax.add_artist(circle11)
        ax.add_artist(circle22)
        ax.add_artist(circle33)

        if tools.isTwoCircleIntersect(circle1, circle2):
            if distance_list[0] > distance_list[1]:
                circle1.r += TRY_DISTANCE_STEP
            else:
                circle2.r += TRY_DISTANCE_STEP

        if tools.isTwoCircleIntersect(circle1, circle3):
            if circle1.r > circle3.r and circle2.r > circle3.r:
                circle1.r += TRY_DISTANCE_STEP
                circle2.r += TRY_DISTANCE_STEP
            else:
                circle3.r += TRY_DISTANCE_STEP

        if tools.isTwoCircleIntersect(circle2, circle3):
            if circle2.r > circle3.r and circle1.r > circle3.r:
                circle1.r += TRY_DISTANCE_STEP
                circle2.r += TRY_DISTANCE_STEP
            else:
                circle3.r += TRY_DISTANCE_STEP

        temp1 = tools.getIntersectionPointsOfTwoIntersectCircle(circle1, circle2)
        temp2 = tools.getIntersectionPointsOfTwoIntersectCircle(circle2, circle3)
        temp3 = tools.getIntersectionPointsOfTwoIntersectCircle(circle3, circle1)


        # The point where the intersection of the two circles of 1 and 2 takes y > 0
        if temp1.p1.y > 0:
            resultPoint1 = p1
        else:
            resultPoint1 = p2

        #The intersection of 2, 3 and 2 circles takes the mean of the two
        resultPoint2 = tools.Point(max(temp2.p1.x, temp2.p2.x), max(temp2.p1.y, temp2.p2.y))

        plt.plot([resultPoint1.x, resultPoint2.x], [resultPoint1.y, resultPoint2.y], '.', color='green')

        #3, 1 the intersection of the two circles takes the point where x > 0
        if temp3.p1.x > 0:
            resultPoint3 = tools.Point(temp3.p1.x, temp3.p1.y)
        else:
            resultPoint3 = tools.Point(temp3.p2.x, temp3.p2.y)


        final_point = tools.getCenterOfThreePoint(resultPoint1, resultPoint2 , resultPoint3)
        print("coordinate of final point: ", final_point)
        plt.plot([final_point.x , final_point.y], '.', color="pink")

        plt.gca().set_aspect('equal', adjustable='box')
        #plt.show()

    except Exception as e:
        print('exception :', data.decode(), e)

#df=pd.DataFrame.from_dict(dict, orient="index", columns= ['URl', 'Rssi', 'Mac', 'Time'])
#print(df[['Mac', 'Rssi']])
#calculate(df)
#cleardataframe(df)
sock.close()