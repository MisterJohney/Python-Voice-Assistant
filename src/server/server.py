from transform import transform
import socket
import threading
import logging

def process_file(content, output_file_path):
    logging.info("Processing the audio file")
    transform()

    return content

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

        # Process the file
        processed_content = process_file(file_content)

        # Send the processed content back
        client_socket.sendall(processed_content)
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
    finally:
        client_socket.close()
        logging.info(f"Connection closed with {client_address}")

def start_server(host='127.0.0.1', port=5000):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    logging.basicConfig(level=logging.INFO)
    start_server()
