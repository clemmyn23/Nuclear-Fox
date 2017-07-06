
class FileWriter:
    def write(self, x) -> None:
        print(str(x))
    def fun(self) -> None:
        print("EXAM PERIOD SEND HELP")

class EncryptedFileWriter(FileWriter):
    def __init__(self, fw:FileWriter, key:str):
        self.fw = fw
        self.key = key

    def write(self, stuff:str) -> None:
        encrypted = self.encrypt_function(stuff)
        self.fw.write(encrypted)

    def encrypt_function(self, text) -> str:
        key = self.key
        return "==={}==={}===".format(key, text)

##########################################
out = FileWriter()
encryptedout = EncryptedFileWriter(out, "123123")

x = "hello world"
encryptedout.write(x)

encryptedout.fun()
