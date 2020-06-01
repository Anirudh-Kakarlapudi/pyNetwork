import socket
import pickle
import argparse
import numpy as np


class NetworkClient:
    """Class for the client to receive data and simulate the domain

    Attributes:
    s (socket):
        an endpoint instance defined by an IP address and a port in the
        context of either a particular TCP connection or the listening state.
        Ref: `https://stackoverflow.com/questions/152457/
              what-is-the-difference-between-a-port-and-a-socket`
    host(str):
        Server IP address
    client_num (int):
        A unique number for client
    port (int):
        a logical construct that identifies a specific process or
        a type of network service.
        Ref:`https://en.wikipedia.org/wiki/Port_(computer_networking)`
    total_clients (num):
        Total number of clients in network
    """
    def __init__(self, server_addr, client_num, total_clients):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = server_addr  # server ip address
        self.client_num = client_num
        self.port = 9998
        self.total_clients = total_clients
        self.s.connect((self.host, self.port))

    def send_data(self, data):
        """Sends the data to the server in pickle format
        """
        print('sending data')
        pickl = pickle.dumps(data)
        self.s.send(pickl)

    def recv_data(self):
        """Receives the data to the server in pickle format
        """
        pickl = self.s.recv(4096)
        data = [0]
        if pickl:
            data = pickle.loads(pickl)
            # print(data, type(data))
        return data

    def task(self):
        pass


def main():
    parser = argparse.ArgumentParser(description='Client Program')

    parser.add_argument('server_addr', type=str,
                        help='The address of server')

    parser.add_argument('client_num', type=int,
                        help='The unique number of client between' +
                             '0 and (total clients - 1)')

    parser.add_argument('total_clients', type=int,
                        help='The number of clients')

    args = parser.parse_args()
    nc = NetworkClient(args.server_addr, args.client_num, args.total_clients)
    nc.task()

if __name__ == '__main__':
    main()
