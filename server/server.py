import socket
import sys
from pathlib import Path

HOST = "127.0.0.1"
PORTA = 8080

# create a UDP socket, SOCK_DGRAM is used for UDP and AF_INET is used for IPv4

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
    server_addr = (HOST, PORTA)
    udp.bind(server_addr)
    
    while True: 
        try:
            # Wait for a message from the client with a buffer size of 1024 bytes
            data, addr = udp.recvfrom(1024) 
            print(f"Mensagem recebida de {addr}: {data.decode()}")
            received_message = data.decode()
        except KeyboardInterrupt:
            print("Servidor encerrado.")
            udp.close()
            sys.exit()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        