import socket
import json
import signal
import sys
import asyncio
import functools

def keyboardInterrupt_handler(sock, loop, sig, frame):
    loop = False
    print("KeyboardInterrupt: Closing Socket")
    
def init_socket_listener(HOST, PORT, message_buffer) -> None:
    # Create Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Loop Boolean
    loop = True

    # Bind Socket to host:port and start listening
    sock.bind((HOST, PORT))
    sock.listen()

    buffer = b''
    while loop:
        # Wait for client to connect
        try:
            conn, _ = sock.accept()
        except KeyboardInterrupt:
            if conn:
                conn.close()
            loop = False
            break
        print('SOCKET LOG:\tClient Connected, Receiving Data\n')

        # Receive Data
        while loop:
            data = conn.recv(1024)
            if not data:
                break

            buffer += data
            messages = buffer.split(b'\n')

            # Process each message
            for message in messages[:-1]:
                json_data = json.loads(message)
                message_buffer.append(json_data)
                print(f"SOCKET LOG:\tJson Data Received: {json_data}")

            buffer = messages[-1]
        # Close connection
        conn.close()

    sock.close()

if __name__ == "__main__":
    buff = []
    init_socket_listener('localhost', 8080, buff)