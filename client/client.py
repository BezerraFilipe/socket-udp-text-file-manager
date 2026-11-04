import socket 


HOST = "127.0.0.1"
PORTA = 8080

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
    server_addr = (HOST, PORTA)

    message = 'aaa'
    udp.sendto(message.encode(), server_addr)

    