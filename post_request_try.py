import requests
import time

def send_multiple_requests(filename= 'gps_series.csv', interval = 0.5):
    url = 'http://localhost:3000/'
    f = open(filename)
    data = f.readlines()

    for i in range(0,len(data)):
        line = data[i]
        split_line = line.split(',')
        lat = str(split_line[0].strip())
        lon = str(split_line[1].strip())
        myobj = {'lat': lat,'lon':lon}
        requests.post(url, data = myobj)
        time.sleep(interval)

    f.close()

def send_one_request(lat = str(42.382540150374666), lon = str(-83.47665825397218) ):
    url = 'http://localhost:3000/'
    myobj = {'lat': lat,'lon':lon}
    requests.post(url, data = myobj)

if __name__ == "__main__":
    send_one_request()
    send_multiple_requests(interval = 0.00)
        
