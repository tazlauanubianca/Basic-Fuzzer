import ctypes
import random

def generate(max_length=1000000000, char_start=1, char_range=255):
    """A string of up to `max_length` characters
       in the range [`char_start`, `char_start` + `char_range`]"""
    #string_length = random.randrange(0, max_length + 1)
    string_length = max_length
    print(string_length)
    out = ""

    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))

    print(len(out))
    return out

if __name__ == '__main__':
    libPath = '/home/bianca/Desktop/thesis/Basic-Fuzzer/out-rdynamic'
    lib = None

    try:
        lib = ctypes.CDLL(libPath)
    except OSError as e:
        print('loading out-rdynamic failed: %s', e)

    if not lib:
        print('no out-rdynamic found')

    lib.strlen.argtypes = [ctypes.c_char_p]
    inputString = generate()
    #print(inputString)
    result = lib.strlen(inputString)

    print("Result is {}".format(int(result)))

