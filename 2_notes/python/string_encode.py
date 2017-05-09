words = "hello world\ncats are cute"

print(words)

enc = words.encode('utf-8')

print(enc[4:13])

print(enc.decode('utf-8'))
