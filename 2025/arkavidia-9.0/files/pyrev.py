from mmap import PAGESIZE, PROT_EXEC, PROT_WRITE, mmap, PROT_READ
from ctypes import c_int, CFUNCTYPE, addressof
from ctypes import c_void_p
from base64 import b64decode

expected_hex = (
    "c1f6c5430aa35fa45753aa87d30c353089fc68111217baefc1c1933177770808"
    "f8f8e8e8acac24249c9cc9c97f7f3535ebeb67"
)
expected = bytes.fromhex(expected_hex)

code_mem = mmap(-1, PAGESIZE, prot=PROT_READ | PROT_WRITE | PROT_EXEC)

F = CFUNCTYPE(c_int, c_int, c_int)

code_ptr = c_void_p.from_buffer(code_mem)
func = F(addressof(code_ptr))

code_mem.write(b64decode(
    "UVJWSInwSPfGAQAAAHUESIPAAUmJwEiJ+Egx0kjHwQQAAABI9/FIg/oAdBJIg/oBdBJIg/oCdBVIa/9l6xNIa/8b6w1Iaf+BAAAA6wRIa/8DSQ+v+EiB5/8AAABIifheWlnD"
))

recovered = []

for i, exp_out in enumerate(expected):
    candidate = None
    for x in range(256):
        out_val = func(x, i) & 0xff  
        if out_val == exp_out:
            candidate = x
            break
    if candidate is None:
        print("Failed to recover byte for index", i)
        break
    recovered.append(candidate)

flag = bytes(recovered)
print("Recovered flag:", flag)
