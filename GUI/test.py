import socket
import json
import random
import time
import sys
import argparse

HOST = 'localhost'
PORT = 8080
N_ITER = 5000       # Number of JSON items to send

def generate_random_object() -> dict:
    data = {
        'phoneme': random.randrange(0, 5),
        'image_encoded': "some_random_bytes",
        'time': int(round(time.time() * 1000)) # time in miliseconds since unix epoch (Jan 1 1970) UTC
    }
    return data

def create_socket(HOST, PORT) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    return sock

def automated_testing(sock, iterations):
    for i in range(0, iterations):
        if(i % 100 == 0):
            print(f"{i}")
        data = generate_random_object()
        # Send data to server
        json_data = json.dumps(data).encode("ASCII") + b'\n'
        sock.sendall(json_data)

        # Close the connection
    sock.close()

def manual_testing(sock):
    try:
        while True:
            data = generate_random_object()
            _ = input(f"Press ENTER to send\n\t{data}\n")
            json_data = json.dumps(data).encode("ASCII") + b'\n'
            sock.sendall(json_data)
    except:
        sock.close()
        print("Closing Testing Script...")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Endpoint testing script")
    parser.add_argument("mode", help="0: Automatic Testing\n1:Manual Testing", type=int)

    args = parser.parse_args()
    mode = args.mode

    sock = create_socket(HOST, PORT)
    if mode == 0:
        # Automated Testing
        automated_testing(sock, N_ITER)
    elif mode == 1:
        # Manual testing
        manual_testing(sock)
    else:
        print("Incorrect Arguments")
        sys.exit(0)
