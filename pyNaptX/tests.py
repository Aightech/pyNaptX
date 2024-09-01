
import time 
import pyNaptX.naptX as naptX

def callback(values, dt):
    print("dt = {}".format(dt[0]))
    print("values = {}".format(values))
fsrray = naptX.FSRray()
fsrray.set_callback(callback)
fsrray.connect()
time.sleep(5)
fsrray.disconnect()