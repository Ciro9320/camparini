from pwn import *

p = process('./CrossTheBridge_patched')

p.sendline(b'Y') #all'inizio il programma richiede Y per continuare
p.sendline() #richiede inoltre invio per continuare
p.sendline(b'L\n' * 16)
#p.interactive()
print(p.recvline_regex(rb".*{.*}.*").decode("ascii")) #stampa la flag