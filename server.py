import socket
import ssl

# Cria um contexto SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(('localhost', 35423))
    server_socket.listen(5)

    # Víncula o server_socker com o SSL
    with context.wrap_socket(server_socket, server_side=True) as ssl_server_socket:
        print("Server is listening...")

        while True:
        # Aguarda conexão
            client_socket,client_address = ssl_server_socket.accept()
            print("Client connected:", client_address)

            # Recebe os dados do cliente
            data = client_socket.recv(1024)
            print("Received data:", data.decode())

            # Envia resposta de volta
            response = "Hello from the server!"
            client_socket.send(response.encode())
            client_socket.close()