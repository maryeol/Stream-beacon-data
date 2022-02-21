def set_key(dictionary, key_ip, mac_key, value , listmac):
    if key_ip not in dictionary:
        dictionary.update({key_ip: [{mac_key : value}]})
    else:
        if mac_key in listmac: # hedha fiha ghalta
            pos = dictionary[key_ip].index('mac22')
            dictionary[key_ip][pos][mac_key].append(value)
        else:
            dictionary[key_ip].append({ mac_key: value })

def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)

word_freq = {}
value=[]
listmac=[]

key = 'ip2'
mac_key ='mac2'
value =50
set_key(word_freq, key,mac_key,value,listmac)
listmac.append(mac_key)

key = 'ip2'
mac_key = 'mac22'
value = -50
set_key(word_freq, key, mac_key, value,listmac)
listmac.append(mac_key)

key = 'ip2'
mac_key = 'mac22'
value = -60
set_key(word_freq, key, mac_key, value ,listmac)
listmac.append(mac_key)

key='ip1'
mac_key='mac1'
value=10
set_key(word_freq, key, mac_key, value, listmac)
listmac.append(mac_key)

print(word_freq)
#RSSI = sumOfList(word_freq['ip2'][0]['mac2'] ,word_freq['ip2'][0]['mac2'].len() )
#Distance = 10 ^ ((-69 -RSSI)/(10 * 2))