import sys
import http.server as httpserver
import socketserver
import time
import os
import cgi


PORT = 8080

def pythonScriptMethod(x, y):
    comand = "python OCR.py" + x + " " + y
    os.system(comand)
    if y == "txt":
        result = "final_output.txt"
    elif y == "pdf":
        result = "final.pdf"
    else:
        result = "final_doc.docx"
    return result


class MyHandler(httpserver.CGIHTTPRequestHandler): 
    
    cgi_directories = [""]
    def do_POST(self): 
        if "hin txt" in self.path:  
            content = pythonScriptMethod("hin", "txt") 
            self.respond(content)
        elif "hin pdf" in self.path:  
            content = pythonScriptMethod("hin", "pdf") 
            self.respond(content)
        elif "hin doc" in self.path:  
            content = pythonScriptMethod("hin", "doc") 
            self.respond(content)
        elif "eng txt" in self.path:
            print("shit")  
            content = pythonScriptMethod("eng", "txt") 
            self.respond(content)
        elif "eng pdf" in self.path:  
            content = pythonScriptMethod("eng", "pdf") 
            self.respond(content)
        elif "eng doc" in self.path:  
            content = pythonScriptMethod("eng", "doc") 
            self.respond(content) 
        else: 
            super(MyHandler, self).do_GET() 
 
 

if __name__ == '__main__': 
    server_class = httpserver.HTTPServer 
    httpd = server_class(("", PORT), MyHandler) 
    print(time.asctime(), 'Server Starts - %s:%s' % ("", PORT)) 
    try: 
        httpd.serve_forever() 
    except KeyboardInterrupt: 
        pass 
    httpd.server_close() 
    print(time.asctime(), 'Server Stops - %s:%s' % ("", PORT)) 