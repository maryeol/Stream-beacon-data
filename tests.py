import sys
import time
import os

from tabulate import tabulate



for i in range(50):
    #sys.stdout.flush()
    time.sleep(0.5)
    os.system('clear')
    print(tabulate([['Alice', 0+i], ['Bob', 10+i]], headers=['Name', 'Age']))


#for i in range(10):
#    print(i, end=' ')
#    sys.stdout.flush()
#    time.sleep(1)