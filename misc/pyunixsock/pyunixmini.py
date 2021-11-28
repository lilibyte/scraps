(l := __import__("ctypes").CDLL("rakunix.so"), (s := l.create_socket(), l.connect_socket(s, b"socket"), l.write_to_sock(s, b'hello', 5), l.close_socket(s)))
