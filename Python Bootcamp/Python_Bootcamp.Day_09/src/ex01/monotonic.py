import ctypes
import sys


def monotonic():
    if sys.platform.startswith('linux'):
        libc = ctypes.CDLL('libc.so.6')

        class timespec(ctypes.Structure):
            _fields_ = [
                ('tv_sec', ctypes.c_long),
                ('tv_nsec', ctypes.c_long),
            ]
        ts = timespec()
        libc.clock_gettime(1, ctypes.byref(ts))
        return ts.tv_sec + ts.tv_nsec / 1e9

    elif sys.platform == 'darwin':
        libc = ctypes.CDLL('libSystem.dylib')

        class timespec(ctypes.Structure):
            _fields_ = [
                ('tv_sec', ctypes.c_long),
                ('tv_nsec', ctypes.c_long),
            ]
        ts = timespec()
        libc.clock_gettime(5, ctypes.byref(ts))
        return ts.tv_sec + ts.tv_nsec / 1e9
    elif sys.platform.startswith('win'):
        kernel32 = ctypes.windll.kernel32
        return kernel32.GetTickCount() / 1000.0
    else:
        raise NotImplementedError(f"Monotonic clock not implemented for platform {sys.platform}")


if __name__ == "__main__":
    print(f"Monotonic time: {monotonic():.2f} seconds")
