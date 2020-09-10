import socket
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).decode().splitlines()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # self.payload = {
        #     'device_id': self.data[0],
        #     'identity_id': self.data[1],
        #     # 'sample_id': data.split('\r')[2].split('|')[0].split(':')[1],
        #     # 'atm_temp': '',
        #     # 'soil_temp': ''
        #     'data': self.data[-2]
        # }
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((ServerHOST, ServerPORT))
            sock.sendall(bytes(self.data[-2] + "\n", "utf-8"))

            # Receive data from the server and shut down
            # received = str(sock.recv(1024), "utf-8")


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    ServerHOST, ServerPORT = '', ''

    # Create the server, binding to localhost on port 9999
    with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
