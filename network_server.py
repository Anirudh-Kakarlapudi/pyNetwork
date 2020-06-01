import socket
import pickle
import argparse
import numpy as np


class NetworkServer:
    """Class for the client to receive data and simulate the domain

    Attributes:
        num_clients (int):
            Number of clients in the network
        connections (list):
            Connection between computers
        addresses (list):
            list of combination of ip addresses and ports of clients
        host (str):
            An empty string denoting the present system as server
        port (int):
            a logical construct that identifies a specific process or
            a type of network service.
            Ref:`https://en.wikipedia.org/wiki/Port_(computer_networking)`
        s (socket):
            an endpoint instance defined by an IP address and a port in
            the context of either a particular TCP connection or the
            listening state.
            Ref: `https://stackoverflow.com/questions/152457/
                  what-is-the-difference-between-a-port-and-a-socket`
    """
    def __init__(self, num_clients):
        self.num_clients = num_clients
        self.connections = []
        self.addresses = []
        self.host = ''
        self.port = 9998
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_socket(self):
        """ Binds the socket to address
        """
        print("Binding the Port: " + str(self.port))
        self.s.bind((self.host, self.port))
        self.s.listen(5)

    def accepting_connections(self):
        """Accepts the connections from all the clients"""
        while len(self.connections) != self.num_clients:
            print(f'Expecting {self.num_clients-len(self.connections)}' +
                   ' client(s) to connect')
            conn, addr = self.s.accept()
            self.connections.append(conn)
            self.addresses.append(addr)
            self.s.setblocking(True)
            print('Connection Succesful to ', addr[0])

    def receive_data(self):
        """Receives the data from the clients. Using `Data Received`,
        `Task Complete` and `Close Connection` as msgs from client to server
        """
        received_data = []
        try:
            for conn in self.connections:
                data = [0]
                print(conn)
                while(data[-1] != 'Close Connection'):
                    print(data)
                    print('Waiting to receive data from the client')
                    data = pickle.loads(conn.recv(4096))
                    if data[-1] == 'Data Received':
                        return 'Data Received'
                    elif data[-1] == 'Task Complete':
                        received_data.extend(data[0])
                        return received_data
        except:
            print('There is an error in Data transfer.\
                  All clients did not return data')

    def broadcast_data(self, data):
        """Converts the data into pickle format and then sends the data
        to all the clients
        Args:
            pickl(pickle):
                The data received from server in client format.
        """
        if len(self.connections) == self.num_clients:
            pickl = pickle.dumps(data)
            for conn in self.connections:
                conn.send(pickl)

    def task(self):
        pass


def main():
    parser = argparse.ArgumentParser(description='Server Program')
    parser.add_argument('num_clients', metavar='num_clients', type=int,
                        default=1, help='number of clients (default=1)')
    args = parser.parse_args()
    ns = NetworkServer(args.num_clients)
    ns.task()


if __name__ == "__main__":
    main()
