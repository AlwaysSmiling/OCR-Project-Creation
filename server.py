import sys
import http.server
import socketserver
import time
import os
import cgi


PORT = 8080

MyHandler = http.server.SimpleHTTPRequestHandler


if __name__ == '__main__': 
    server_class = http.server.HTTPServer 
    httpd = server_class(("", PORT), MyHandler) 
    print(time.asctime(), 'Server Starts - %s:%s' % ("", PORT)) 
    try: 
        httpd.serve_forever() 
    except KeyboardInterrupt: 
        pass 
    httpd.server_close() 
    print(time.asctime(), 'Server Stops - %s:%s' % ("", PORT)) 