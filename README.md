# Python Socket UDP implementation

## About

This repository implements a simulation of a distributed system in client-sever mode, using a UDP socket.

It allows you to upload, download and list text files in the server.

The server listen a specific port and handdle multiples connections.

## Project shape

```
socket-udp-text-file-manager/
├── client/
│   ├── ...
│   └── ...
├── server/
│   └── ...
└── README.md
```

## Requirements

- Python 3.8 +

A instalação de nenhuma biblioteca externa se faz necessária, pois o projeto usa apenas módulos da biblioteca padrão do Python.


## Getting started

#### Clone this repository to your local machine


```bash
git clone https://github.com/BezerraFilipe/socket-udp-text-file-manager.git
```

#### Navigate into the project directory:


```bash
cd work/directory/socket-udp-text-file-manager/
```

#### Run the server

**Linux/macOS:**

```bash
python3 server/server.py
```

#### Run the client (another terminal)

**Linux/macOS:**

```bash
python3 client/client.py
```



Saída esperada:

```text
Conectado a 127.0.0.1:8080. 

Use:
1) Upload de arquivo
2) Download de arquivo
3) Listar arquivos
4) Encerrar Execução

```

Agora você pode digitar comandos no terminal do cliente.

#### 4. Envie um arquivo (UPLOAD)

Crie um arquivo de teste na pasta `cliente/`, por exemplo `sonic.webm`.


```text
> UPLOAD cliente/sonic.webm
```

Saída esperada:

```text
OK upload de sonic.webm concluido
```

O arquivo será salvo em `servidor/arquivos/sonic.webm`. 

#### 5. Liste os arquivos (LIST)

```text
> LIST
```

O cliente mostrará o nome, o tamanho em bytes, a data de modificação e o endereço da conexão do cliente que solicitou a listagem.

#### 6. Baixe um arquivo (DOWNLOAD)

```text
> DOWNLOAD sonic.webm
```

O arquivo será salvo na pasta de onde você executou o cliente.

#### 7. Encerre a conexão

```text
> EXIT
```

Se você configurou apenas um cliente, o servidor terminará depois dessa conexão. Para iniciar outro teste, execute novamente o servidor antes do cliente.

## Comandos disponíveis

| Comando | Função | Exemplo |
| --- | --- | --- |
| `UPLOAD <caminho>` | Envia um arquivo local ao servidor | `UPLOAD cliente/sonic.webm` |
| `DOWNLOAD <nome>` | Baixa um arquivo do servidor | `DOWNLOAD sonic.webm` |
| `LIST` | Lista os arquivos armazenados | `LIST` |
| `EXIT` | Encerra a sessão do cliente | `EXIT` |

## Configuração de rede

Por padrão, ambos os scripts utilizam:

```python
HOST = "127.0.0.1"
PORTA = 8080
```
 