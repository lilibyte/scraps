import ctypes

# <qorg> pick my .c code which is a lib to write to
#        open, write, read and close a UNIX socket and put
#        it in python
# <qorg> like use that C code in python
# <qorg> like call those funcs from py

# cc -fPIC -shared -o rakunix.so rakunix.c
lib = ctypes.CDLL("rakunix.so")


class Suckit:

    def __init__(self, path: str):
        self.path = path.encode()
        self.suck = lib.create_socket()
        lib.connect_socket(self.suck, self.path)

    def write_suck(self, msg: str):
        lib.write_to_sock(self.suck, msg.encode(), len(msg))

    def close_suck(self):
        lib.close_socket(self.suck)


# socat - UNIX-LISTEN:socket
suckit = Suckit("socket")
suckit.write_suck("hello world!")
suckit.close_suck()
