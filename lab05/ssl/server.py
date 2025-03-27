import socket
import ssl
import threading

server_address = ('localhost', 12345)

# Danh sách các client đã kết nối
clients = []


def handle_client(client_socket):
    """ Xử lý tin nhắn từ client """
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")

            # Gửi tin nhắn đến tất cả client khác
            for client in clients:
                if client != client_socket:
                    client.send(data)

        except Exception as e:
            print(f"Error: {e}")
            break

    # Xóa client khỏi danh sách khi ngắt kết nối
    clients.remove(client_socket)
    client_socket.close()


# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)
print(f"Listening on {server_address}")

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="./certificates/server-cert.crt",
                        keyfile="./certificates/server-key.key")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"New connection from {client_address}")

    # Tạo kết nối SSL
    ssl_socket = context.wrap_socket(client_socket, server_side=True)

    # Thêm vào danh sách client
    clients.append(ssl_socket)

    # Tạo luồng xử lý riêng
    client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
    client_thread.start()
