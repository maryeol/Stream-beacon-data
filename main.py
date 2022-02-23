import socket
import json
import pandas as pd
from datetime import datetime

UDP_IP = "192.168.162.66"
UDP_PORT = 5015
index = 0
index1 = 0

def calculate(df):
    idf = df.groupby('Mac').mean()
    idf['Distance'] = pow(10, ((-69 - idf['Rssi']) / (10 * 2)))
    print(idf)

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

dict = {}
i = 0

t1 = datetime.now()
while (datetime.now()-t1).seconds <= 5:  #run for 5 seconds
#while True:
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
        b_data.extend([b_url,b_rssi,b_mac,b_time])

        dict[i] = b_data
        i = i+1

        df=pd.DataFrame.from_dict(dict, orient="index", columns= ['URl', 'Rssi', 'Mac', 'Time'])
        print(df[['Rssi', 'Mac']])

    except Exception as e:
        print('exception :', data.decode(), e)

#df=pd.DataFrame.from_dict(dict, orient="index", columns= ['URl', 'Rssi', 'Mac', 'Time'])
#print(df[['Mac', 'Rssi']])
calculate(df)
sock.close()