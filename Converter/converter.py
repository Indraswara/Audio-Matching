import wave
import binascii

class converter: 
    def __init__(self, path: str):
        self.path = path
        self.binary_data = self.convert_to_binary()
        self.ascii_data = self.binary_to_ascii()        

    def convert_to_binary(self) -> bytes:
        w = wave.open(self.path, "rb")
        binary_data = w.readframes(20)
        w.close()
        return binary_data

    def binary_to_ascii(self) -> str:
        self.ascii_data = binascii.b2a_uu(self.binary_data)
        return self.ascii_data.decode('ascii')




# convert = converter('../Data/Speaker26_000.wav')
# print(convert.binary_to_ascii())

