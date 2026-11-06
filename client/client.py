import json
import socket
from pathlib import Path
from datetime import datetime

# the server's IP address and port number
HOST = "127.0.0.1"
PORT = 8080


CLIENT_FILE_DIRECTORY = Path(__file__).parent / "files"

# create a udp socket 
def create_udp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    # SOCK_DGRAM is used for UDP sockets and AF_INET is used for IPv4 addresses

def upload_text_file(file_name, udp_socket, server_addr):
    
    path = CLIENT_FILE_DIRECTORY / file_name
    
    if not path.is_file():
        print(f"Error: '{path.name}' was not found in '{CLIENT_FILE_DIRECTORY.resolve()}'.")
        return

    # Send the file name to the server
    header = f"UPLOAD: {path.name}"
    udp_socket.sendto(header.encode("utf-8"), server_addr)

    # Send the file content in batches of 1024 bytes
    with path.open("r", encoding="utf-8") as arquivo:
        while bloco := arquivo.read(1024):
            udp_socket.sendto(bloco.encode("utf-8"), server_addr)

    # End-of-file marker
    udp_socket.sendto("<EOF>".encode("utf-8"), server_addr)
    print(f"'{path.name}' was sent successfully from '{CLIENT_FILE_DIRECTORY.name}'!")

def list_files_in_server_directory(udp_socket, server_addr):
    # Send a request to the server to list files
    udp_socket.sendto("LIST_FILES".encode("utf-8"), server_addr)

    # Receive the list of files from the server
    data, _ = udp_socket.recvfrom(4096)
    file_list = json.loads(data.decode("utf-8"))

    print("\nFiles in server directory:")

    if not file_list:
        print("No files available.")
        return

    for file in file_list:
        print(f"\nName: {file['name']}")
        print(f"Size: {file['size']} bytes")
        print(f"Extension: {file['extension']}")
        print(f"Last modified: "f"{datetime.fromtimestamp(file['last_modified'])}")
        
def download_text_file(file_name, udp_socket, server_addr):
    # Send the file name to the server
    header = f"DOWNLOAD: {file_name}"
    udp_socket.sendto(header.encode("utf-8"), server_addr)

    # Receive the file content in batches of 1024 bytes
    path = CLIENT_FILE_DIRECTORY / file_name
    with path.open("w", encoding="utf-8") as arquivo:
        while True:
            data, _ = udp_socket.recvfrom(1024)
            content = data.decode("utf-8")
            
            # Check for the end-of-file marker
            if content == "<EOF>":
                break
                
            arquivo.write(content)

    print(f"'{path.name}' was downloaded successfully into '{CLIENT_FILE_DIRECTORY.name}'!")

def main():
    try:
        server_addr = (HOST, PORT)
        udp_socket = create_udp_socket()
        while True:
            print("\nOptions:")
            print("1. List files in server directory")
            print("2. Upload a text file to the server")
            print("3. Download a text file from the server")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                list_files_in_server_directory(udp_socket, server_addr)
            elif choice == "2":
                file_name = input("Enter the name of the text file to upload: ").strip()
                upload_text_file(file_name, udp_socket, server_addr)
            elif choice == "3":
                file_name = input("Enter the name of the text file to download: ").strip()
                download_text_file(file_name, udp_socket, server_addr)
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    
