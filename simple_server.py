from http.server import HTTPServer, BaseHTTPRequestHandler

data_struct = {
    'lat' : str(42.382540150374666),
    'lon' : str(-83.47665825397218)
    }

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        message = ''.join('{"geometry": {"type": "Point", "coordinates": [%s,%s]}, "type": "Feature", "properties": {}}' % (data_struct['lon'],data_struct['lat']))
        self.wfile.write(bytes(message,'utf-8'))
        return()

    def do_POST(self):
        params = {}
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Parse the post request
        for x in post_data.split('&'):
            key,value = x.split('=') 
            params[key] = value

        # Update class variables        
        data_struct['lat'] = params['lat']
        data_struct['lon'] = params['lon']

        self.wfile.write("POST request for {},{}".format(data_struct['lat'],data_struct['lon']).encode('utf-8'))
        return()
        
httpd = HTTPServer(('localhost', 3000), SimpleHTTPRequestHandler)
httpd.serve_forever()