import socket
import json
import random
import time
import argparse

HOST = 'localhost'
PORT = 8080
N_ITER = 5000       # Number of JSON items to send

def generate_random_object():
    data = {
        'phoneme': random.randrange(0, 5),
        'image_encoded': "somer_random_bytes",
        'time': int(round(time.time() * 1000)) # time in miliseconds since epoch (Jan 1 1970) UTC
    }
 b
    return data

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Establish the connection
sock.connect((HOST, PORT))

for i in range(0, N_ITER):
    if(i % 100 == 0):
        print(f"{i}")
    data = {
        'phoneme': random.randrange(0, 5),
        'image_encoded': "somer_random_bytes",
        'time': int(round(time.time() * 1000)) # time in miliseconds since epoch (Jan 1 1970) UTC
    }

    json_data = json.dumps(data).encode("ASCII") + b'\n'
    sock.sendall(json_data)
    
    # Close the connection
sock.close()

if __name__ == "main":