#!/usr/bin/python

import threading
import time
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler

data_struct = {
    'lat' : str(42.382540150374666),
    'lon' : str(-83.47665825397218)
    }

# Initialize UDP socket
UDP_IP = "127.0.0.1"
UDP_PORT = 33000
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def udp_listener():
    while True:
        data, addr = sock.recvfrom(1024)
        data_struct['lat'],data_struct['lon'] = data.decode('utf-8').split(',')
        time.sleep(.001)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        message = ''.join('{"geometry": {"type": "Point", "coordinates": [%s,%s]}, "type": "Feature", "properties": {}}' % (data_struct['lon'],data_struct['lat']))
        self.wfile.write(bytes(message,'utf-8'))
        return()

def main():
    httpd = HTTPServer(('localhost', 34000), SimpleHTTPRequestHandler)
    t1 = threading.Thread(target=httpd.serve_forever)
    t2 = threading.Thread(target=udp_listener)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        pass

if __name__ == '__main__':
    main()
        
