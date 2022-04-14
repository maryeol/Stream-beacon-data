from datetime import datetime
import time
import pandas as pd
import base64
import random

def convert2Base64(pan):
    bytes_string = pan.encode('ascii')
    #print(" ASCII : ", bytes_string)
    base_64_bytes = base64.b64encode(bytes_string)
    #print(" base 64 bytes : ", base_64_bytes)
    base64_string = base_64_bytes.decode('ascii')
    print("encoded PAN : ", base64_string)
    return base64_string

def convertBase10ToBase64(num):
    order = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"
    base = len(order)
    str = ""
    while num:
        r = int (num % base)
        num -= r
        num /= base
        str = order[r] + str
    return str

def getID(input):
    print(input[1]+input[4])
    return input[1]+input[4]

def generatePAN():
    pan = random.randint(1000000000000000000 , 9999999999999999999)
    return pan

def getTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return (current_time)

def time2String(input):
    return input[0:2]+input[3:5]+input[6:8]

def ConvertTimetoBase64(input):
    input = int(input)
    return convertBase10ToBase64(input)

idf = pd.DataFrame({'ip': ['A', 'B', 'C', 'A', 'B', 'C'],
                    'mac': ['10', '20', '30', '50', '20', '40'],
                    'data': [1, 2, 3, 6, 5, 4]}
                   , index=["i1", "i2", "i3", "i4", "i5", "i6"]
                   , columns=['ip', 'mac', 'data'])


#a = 1
# def test(a):
#     while True:
#         if (a < 5):
#             a+=1
#             print(a)
#             continue
#         if(a<10):
#             print("666")
#             a += 1
#
# print (test (a))
#
# print(idf)
# idf2 = idf.groupby(['ip', 'mac']).last()
# print(idf2)
#print(idf2.sort_values(by = ['data']))

#print(idf.sort_values(by = ['data']))


# print(idf2)
# while True:
#     a = 'A'
#     b = '10'
#     df = idf2.drop((a, b), axis=0)
#     print(df)









# print(idf.index)
# print(idf.loc["i1"]['data'])
#
# idf2 = idf.groupby(['ip', 'mac']).mean()
# print(idf2.index)
# df2 = pd.DataFrame(index=idf2.index)
# print(df2)
# print(idf2.loc[('A', '10')]['data'])
# a = 'A'
# b = '10'
# print(type(idf2.loc[(a, b)]['data']))
# idff = pd.DataFrame(idf2.copy(), index = ["i1" ,  "i2" , "i3"])
# print(idff)
# print(idf2['data'] )


# DataFrame.iat
# Series.at
