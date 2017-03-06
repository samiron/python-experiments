import SimpleHTTPServer
import SocketServer
import time
import socket

PORT = 8000


class MySocket:

    sock = None
    
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        
    def request(self, data):
        pass
        self.sock.sendall(data)
        data = self.sock.recv(1024)
        return repr(data)
        
    def close(self):
        self.sock.close()

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def _handle_date(self):        
        ts = time.localtime()
        return time.strftime("'%Y-%m-%d %H:%M:%S'", ts)
    
    def do_GET(self):
        content = ""
        if self.path == "/date":
            content = self._handle_date()
        elif self.path.startswith("/calc/"):
            expression = self.path
            expression = expression.replace('/calc/', '')
            socket = MySocket('localhost', 1298);
            reply = socket.request(expression)
            content = "Result: %s" % reply
            socket.close();
        else:
            content = "<pre><b>%s</b></pre> is a unknown request." % self.path
            

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(content))
        self.end_headers()
        self.wfile.write(content)

if  __name__ == "__main__":
    Handler = MyRequestHandler

    httpd = SocketServer.TCPServer(("localhost", PORT), Handler)

    print "serving at port", PORT
    httpd.serve_forever()
