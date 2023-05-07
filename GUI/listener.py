import socket
import json
import threading
from helper import *

class socket_thread_c(threading.Thread):
    def __init__(self, threadID):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.start()
    def run(self):
        self.init_socket_listener(HOST, PORT, buffer)


    def init_socket_listener(self, HOST, PORT, message_buffer) -> None:
        # Create Socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Loop Boolean
        loop = True

        # Bind Socket to host:port and start listening
        sock.bind((HOST, PORT))
        sock.listen()

        request_buffer = b''
        while loop:
            # Wait for client to connect
            try:
                conn, _ = sock.accept()
            except KeyboardInterrupt:
                print("Closing socket...")
                if conn:
                    conn.close()
                loop = False
                break
            print('SOCKET LOG:\tClient Connected, Receiving Data\n')

            # Receive Data
            try:
                while loop:
                    data = conn.recv(1024)
                    if not data:
                        break

                    request_buffer += data
                    messages = request_buffer.split(b'\n')

                    # Process each message
                    for message in messages[:-1]:
                        json_data = json.loads(message)
                        buffer_push(message_buffer, json_data)
                        print(f"SOCKET LOG:\tJson Data Received: {json_data}")

                    request_buffer = messages[-1]
            except KeyboardInterrupt:
                print("Closing socket...")
                if conn:
                    conn.close()
                loop = False
            # Close connection
            conn.close()

        sock.close()