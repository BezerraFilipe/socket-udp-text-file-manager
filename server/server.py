import socket
from pathlib import Path

# the server's IP address and port number to bind the server socket
HOST = "127.0.0.1" 
PORT = 8080

SERVER_FILE_DIRECTORY = Path(__file__).parent / "files"

def create_udp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def handle_upload_request(udp_socket, file_name, client_addr):
    path = SERVER_FILE_DIRECTORY / file_name
    print(f"Receiving '{path.name}' from {client_addr}...")
    with path.open("w", encoding="utf-8") as file:
        while True:
            data, _ = udp_socket.recvfrom(1024)
            content = data.decode("utf-8")
            
            # Check for the end-of-file marker
            if content == "<EOF>":
                break
            
            file.write(content)
    
    print(f"'{path.name}' was sent by {client_addr} and saved in '{SERVER_FILE_DIRECTORY.name}'!")

def handle_download_request(udp_socket, file_name, client_addr):
    path = SERVER_FILE_DIRECTORY / file_name
    print(f"Sending '{path.name}' to {client_addr}...")
    
    if not path.is_file():
        print(f"Error: '{path.name}' was not found in '{SERVER_FILE_DIRECTORY.resolve()}'.")
        udp_socket.sendto("ERROR: File not found".encode("utf-8"), client_addr)
        return
    with path.open("r", encoding="utf-8") as file:
        while bloco := file.read(1024):
            udp_socket.sendto(bloco.encode("utf-8"), client_addr)
    udp_socket.sendto("<EOF>".encode("utf-8"), client_addr)
    
    print(f"'{path.name}' was sent to {client_addr}!")

def handle_list_files_request(udp_socket, client_addr):
    print(f"Listing files for {client_addr}...")

    files = [f.name for f in SERVER_FILE_DIRECTORY.iterdir() if f.is_file()]
    
    response = "\n".join(files) if files else "No files available."
    udp_socket.sendto(response.encode("utf-8"), client_addr)

def main():
    udp_socket = create_udp_socket()
    udp_socket.bind((HOST, PORT))
    print(f"UDP server listening on {HOST}:{PORT}")

    while True:
        try:
    
            data, client_addr = udp_socket.recvfrom(1024)
            request = data.decode("utf-8").strip()

            parts = request.split(":", 1)
            command = parts[0].strip().upper()
            # the argument does not exist when the command is LIST_FILES
            argument = parts[1].strip() if len(parts) > 1 else None 

            if command == "UPLOAD" and argument:
                handle_upload_request(udp_socket, argument, client_addr)
            elif command == "DOWNLOAD" and argument:
                handle_download_request(udp_socket, argument, client_addr)
            elif command == "LIST_FILES":
                handle_list_files_request(udp_socket, client_addr)
            else:
                print(f"Unknown command received: {request}")
                udp_socket.sendto("ERROR: Unknown command".encode("utf-8"), client_addr)
        except Exception as e:
            print(f"Error handling request: {e}")
            udp_socket.sendto(f"ERROR: {str(e)}".encode("utf-8"), client_addr)

if __name__ == "__main__":
    main()
