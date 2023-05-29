import socket
import ssl

# Cria um contexto SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.ssl_version = ssl.PROTOCOL_TLSv1_2

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(('localhost', 35412))
    server_socket.listen(1)

    # Víncula o server_socker com o SSL
    with context.wrap_socket(server_socket, server_side=True) as ssl_server_socket:
        print("Server is listening...")

        while True:
            # Aguarda conexão
            with ssl_server_socket.accept() as client_socket:
                client_address = client_socket.getpeername()
                print("Client connected:", client_address)

                # Recebe os dados do cliente
                data = client_socket.recv(1024)
                print("Received data:", data.decode())

                # Envia resposta de volta
                response = "Hello from the server!"
                client_socket.send(response.encode())
