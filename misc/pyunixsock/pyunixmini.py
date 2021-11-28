(lib := __import__("ctypes").CDLL("rakunix.so"), (s := lib.create_socket(), lib.connect_socket(s, b"socket"), lib.write_to_sock(s, b'hello', 5), lib.close_socket(s)))
