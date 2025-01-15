import socket
import os
import logging

OUTPUT_PATH = "./data/output.mp3"

def send_file(file_path, host='192.168.8.117', port=5000):
    try:
        if not os.path.exists(file_path):
            logging.error("File does not exist.")
            return
        with open(file_path, 'rb') as f:
            file_content = f.read()

        # Connect to server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        # Send file size
        client.send(str(len(file_content)).encode())
        client.recv(1024) # Wait for acknowledgment
        # Send file content
        client.sendall(file_content)

        # Receive processed content
        file_size = int(client.recv(1024).decode())
        client.send(b"SIZE_RECEIVED")
        processed_content = b""
        while len(processed_content) < file_size:
            data = client.recv(1024)
            if not data:
                break
            processed_content += data
        logging.info("Processed Content Received:")
            
        with open(OUTPUT_PATH, 'wb') as f:
            f.write(processed_content)

        client.close()

    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        client.close()
