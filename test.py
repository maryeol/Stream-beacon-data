from datetime import datetime
import time
import pandas as pd
import base64
import random

# def convert2Base64(pan):
#     bytes_string = pan.encode('ascii')
#     #print(" ASCII : ", bytes_string)
#     base_64_bytes = base64.b64encode(bytes_string)
#     #print(" base 64 bytes : ", base_64_bytes)
#     base64_string = base_64_bytes.decode('ascii')
#     return base64_string

def convertBase10ToBase64(num):
    num = int(num)
    order = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"
    base = len(order)
    str = ""
    while num:
        r = int(num % base)
        num -= r
        num /= base
        str = order[r] + str
    return str

def getID(input):
    return input[7:11]

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

def getLane(x):
    if x<2 and x>=0:
        return 1
    if x<4 and x>=2 :
        return 2
    if x<6 and x>=6:
        return 3

print(getLane(0.99))

input="http://2509/"

print ("Emitted ID is: " ,getID(input))
print("encoded ID is :" , convertBase10ToBase64(getID(input)) )

print("generated PAN is :", generatePAN())
print("encoded PAN is : ", convertBase10ToBase64(generatePAN()))

print("time :", time2String(getTime()))
print("encoded time", convertBase10ToBase64(time2String(getTime())))

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
Ec2zrq
Ec2_jljSRgEQ4zn5

Ec
2
_jljSRgEQ4
zn5
8H78Mi9SG00
8H78Mi9SG00
XCID-
9k2_f-
#3C:61:05:32:28:DA
14y4fj08Xsj
14y4fj08Xsj
14y4fj08Xs0
14y4fj08Xs0
14y4fj08Xs0
14y4fj08Xs0
14y4fj08Xsj
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
