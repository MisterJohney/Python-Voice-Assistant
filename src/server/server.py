from transform import transform

import socket
import threading
import logging
import sqlite3

def handle_client(client_socket, client_address):
    logging.info(f"Connection established with {client_address}")
    
    try:
    # Receive file data
        file_size = int(client_socket.recv(1024).decode())
        client_socket.send(b"SIZE_RECEIVED") # Acknowledge

        file_content = b""
        while len(file_content) < file_size:
            data = client_socket.recv(1024)
            if not data:
                break
            file_content += data

        # Saving file because whisper wants file path not the data itself
        with open("./input.wav", "wb") as f:
            f.write(file_content)

        transform("./input.wav", "./output.mp3")

        # Send the processed content back
        with open("./output.mp3", "rb") as f:
            processed_content = f.read()

            client_socket.send(str(len(processed_content)).encode())
            client_socket.recv(1024)
            client_socket.sendall(processed_content)

    except Exception as e:
        logging.error(f"Exception occurred: {e}")
    finally:
        client_socket.close()
        logging.info(f"Connection closed with {client_address}")

def start_server(host='192.168.8.117', port=5000):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(5)
        logging.info(f"Server started on {host}:{port}")

        while True:
            client_socket, client_address = server.accept()
            client_handler = threading.Thread(
                target=handle_client, args=(client_socket, client_address)
                )
            client_handler.start()

    except KeyboardInterrupt:
        server.close()
        logging.info("Closing server...")


if __name__ == "__main__":
    logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
    start_server()
