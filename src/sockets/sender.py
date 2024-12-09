import socket, time, os, sys
host = "localhost"
PORT = 9999
file = "./recording.wav"

sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender.connect((host, PORT))

file_len = str(os.path.getsize(file))
file_string = 'FILE: ' + file_len + ' ' + os.path.basename(file) + ' =EOF='
print(f"- Send file: {file} ({file_len}) =EOF=") 
sender.send(file_string.encode())
# time.sleep(1)
try:
    with open(file, 'rb') as f:
        file_data = f.read()
        # Begin sending file
        sender.sendall(file_data)
        time.sleep(2)
        sender.send("=EOF=".encode())
    f.close
    print(f"Transfer {file} comleate")
except:
    print("error sending file")

sender.close()
