import base64
import gzip

s='secret'

x=base64.b64decode(s)
y=gzip.decompress(x).decode('UTF-8')

print(y)