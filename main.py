import socket
import json
import pandas as pd
from datetime import datetime

def set_key(dictionary,key_ip,mac_key,value):
    if key_ip not in dictionary:
        dictionary.update({key_ip: [{mac_key: value}]})
    else:
        pos = [{mac_key: value}].index({mac_key: value})
        if mac_key in dictionary[key_ip][pos]:
            dictionary[key_ip][pos][mac_key].append(value)
        else:
            dictionary[key_ip].append({mac_key: value})

UDP_IP = "192.168.162.170"
UDP_PORT = 5015
index = 0
index1 = 0

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

dict_ip = {}

#i = 0

t1 = datetime.now()
#while True:
while (datetime.now() - t1).seconds <= 5: # run for 5 seconds
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
        #b_data = []
        #b_data.extend([b_url,b_rssi,b_mac,b_time])
        b_list_rssi = []
        b_list_rssi.append(b_rssi)
        set_key(dict_ip, b_ip, b_mac, b_list_rssi)
        #i = i+1

        #df=pd.DataFrame.from_dict(dict, orient="index", columns= ['URl', 'Rssi', 'Mac', 'Time'])
        #print(df[['URl', 'Rssi']].tail(1))

    except Exception as e:
        print('exception :', data.decode(), e)

print(dict_ip)
#df=pd.DataFrame.from_dict(dict, orient="index", columns= ['URl', 'Rssi', 'Mac', 'Time'])
#print(df[['URl', 'Rssi']].tail(1))
#print("hello world!")
sock.close()
