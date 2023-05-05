import asyncio
import threading
import json
import time
HOST = 'localhost'
PORT = 8080

buffer = []
current_item = None

lock = threading.Lock()

def buffer_push(buffer, item):
    with lock:
        buffer.append(item)
    return
def buffer_pop(buffer):
    json_ret = None
    with lock:

        if len(buffer) != 0:
            json_ret = buffer[0]
            del buffer[0]
    return json_ret

if __name__ == "__main__":
    buff = []
    buffer_push(buff, 3)