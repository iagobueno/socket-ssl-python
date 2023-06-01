import socket
import lib_client

context = lib_client.createContext()

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Víncula o client_socket com o SSL
    with context.wrap_socket(client_socket, server_hostname='localhost') as ssl_client_socket:
        # Conecta ao servidor
        ssl_client_socket.connect(('localhost', 8888))

        # Envia dados ao servidor
        message = "Hello from the client!"
        ssl_client_socket.send(message.encode())

        # Recebe resposta do servidor
        response = ssl_client_socket.recv(1024)
        print("Received response:", response.decode())
