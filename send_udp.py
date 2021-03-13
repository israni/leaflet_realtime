import socket
import time 

UDP_IP = "127.0.0.1"
UDP_PORT = 33000
#MESSAGE = b"42.1030303,-83.09080800"
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP 


with open('gps_series.csv','r') as f:
    data = f.readlines()


for i in range(0,len(data)):
    line = data[i]
    MESSAGE = bytes(line,'utf-8')
    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("message: %s" % MESSAGE)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    time.sleep(0.05)