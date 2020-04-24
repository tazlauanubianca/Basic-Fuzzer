import ctypes
import random
import sys
from datetime import datetime

def generate(max_length=1000000, char_start=1, char_range=255):
    string_length = random.randrange(0, max_length + 1)
    out = ""

    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))

    return out

if __name__ == '__main__':
    lib_path = '/home/bianca/Desktop/thesis/Basic-Fuzzer/out-rdynamic'
    lib = None

    try:
        lib = ctypes.CDLL(lib_path)
    except OSError as e:
        print('loading out-rdynamic failed: %s', e)

    if not lib:
        print('no out-rdynamic found')

    lib.strlen.argtypes = [ctypes.c_char_p]
    
    while True:
        input_string = generate()
        print("[{}] Test with input size {} ".format(datetime.now(), len(input_string)))
        try:
            f_in = open("inputs.txt", "a")
            f_in.write("Test input [{}]: {}".format(datetime.now(), input_string))
            f_in.close()
            
            result = lib.strlen(input_string)

        except:
            f = open("crashes.txt", "a")
            f.write("Crash number [{}]: {}".format(datetime.now(), input_string))
            f.close()

            print("[{}] Crash occured for input with size {}".format(datetime.now(), len(input_string))) 
