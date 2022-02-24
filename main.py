import socket
import json
import pandas as pd
from datetime import datetime

UDP_IP = "192.168.162.66"
UDP_PORT = 5015
index = 0
index1 = 0

def calculate(df):
    df['Distance'] = pow(10, ((-69 - df['Rssi']) / (10 * 3)))
    idf = df[['Mac', 'Distance']]
    final_df = idf.groupby('Mac').mean()
    print(final_df)

    #To Calculate with last 9 numbers
    #init_df=df[-9:]
    #print(init-df)
    #init_df['Distance'] =  pow(10, ((-69 - init_df['Rssi']) / (10 * 2)))
    #print(init-df)
    #init_df=init_df[['Mac', 'Distance']]
    #final_df=init_df.groupby('Mac').mean()
    #print(final_df)


def cleardataframe(df):
    #clear data from 60 sec el kdom
    t1 = datetime.now()
    t1 = t1.time().second
    index_names = df[t1 - df['Time'].time().second < 60].index
    df.drop(index_names, inplace=True)
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
#cleardataframe(df)
sock.close()