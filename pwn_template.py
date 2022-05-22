from pwn import *

context.arch = 'amd64'
context.terminal = "kitty"
ASLR=True

exe = ELF("./binary")
libc = ELF("/usr/lib/libc.so.6")
HOST = "127.0.0.1"
PORT = 1337

gdbinit = '''
continue
'''

#io = gdb.debug(exe.path, gdbscript=gdbinit, aslr=ASLR)
#io = remote(HOST, PORT)
io = process(exe.path)

offset=0

payload = flat({
    offset:[
        b"AAAAAAAAAAAAAAA"
    ]
})

io.interactive()