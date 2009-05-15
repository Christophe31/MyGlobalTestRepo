#/usr/bin/env python
import math

message=raw_input('message?')
k=int(raw_input('clef'))
mk=""
for i in [chr(ord(i)+k%256) for i in message]:
    mk+=i
print mk
