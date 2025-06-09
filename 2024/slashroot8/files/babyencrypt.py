from pwn import *

conn = remote('157.230.251.184', 10011)

for i in range(0x0000, 0x10000):
    ciphertext = i.to_bytes(2, byteorder='big')
    conn.sendline(ciphertext.hex())
    response = conn.recvline(timeout=1)
    
    if b"slashroot8" in response:
        print(f"Flag: {response.decode().strip()}")
        break

print(response)