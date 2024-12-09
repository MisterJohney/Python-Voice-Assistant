import socket, time, os

host = '0.0.0.0' # Listen on this host
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
client, addr = server.accept()

client.settimeout(3)

payload = client.recv(1024)
decoded_payload = payload.decode()
if decoded_payload.endswith("=EOF="):
    x = str(decoded_payload).split()
    file_size = str(x[1])
    file_name = str(" ".join(x[2:-1]))
    print(f"-- Recieve file: {file_name} ({file_size})")
    file = open("./recieved/" + file_name, "wb")
    while True:
        data = client.recv(1024)
        try:
            if data.decode().endswith('=EOF='):
                break
        except:
            print("exception")
        file.write(data)
    file.close()
    if file_size == str(os.path.getsize(file_name)):
        print("Good size")
    else:
        print("Bad size")
client.close()


