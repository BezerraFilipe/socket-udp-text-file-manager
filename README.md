# Python Socket UDP implementation

## About

This repository implements a simulation of a distributed system in client-sever mode, using a UDP socket.

It allows you to upload, download and list text files in the server.

The server listen a specific port and handdle multiples connections.

## Getting started

#### Clone this repository to your local machine

```bash
git clone https://github.com/BezerraFilipe/socket-udp-text-file-manager.git
```

#### Navigate into the project directory:

```bash
cd work/directory/socket-udp-text-file-manager/
```

### Requirements

- Python 3.8+

## Project shape

```
socket-udp-text-file-manager/
├── client/
│   ├── files/
│   └── client.py
├── server/
│   └── files/
│   └── server.py
└── README.md
```

## Usage

#### Run the server

**Linux/macOS:**

```bash
python3 server/server.py
```

Expected output: 
```
UDP server listening on 127.0.0.1:8080
```

#### Run the client (another terminal)

**Linux/macOS:**

```bash
python3 client/client.py
```

Expected output: 
```
Options:
1. List files in server directory
2. Upload a text file to the server
3. Download a text file from the server
4. Exit
Enter your choice (1-4): 
```

Now you can interact with server from client.

## How it works

- The files can only be transfer from client/files and server/files directories. So if you want to test (download or upload) a diferent file from the example, you must create it on the specified directory.

- The server runs on 127.0.0.1:8080

- You can open multiples clients and see the respective response from server.

- To refer a file, you only need to write it name with the file extension. e.g. "client_file00.txt"

