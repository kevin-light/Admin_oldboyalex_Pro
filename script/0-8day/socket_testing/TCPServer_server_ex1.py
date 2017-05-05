import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data.decode("utf-8"))

                # just send back the same data, but upper-cased
                self.request.send(self.data.upper())    #sendall改为send
            except ConnectionResetError as e:
                print("err",e)
                break
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
# ThreadingTCPServer多线程，
    server.serve_forever()