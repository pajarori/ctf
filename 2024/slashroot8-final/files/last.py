key, _key = "asdghkashdfclkamsdfjalxsdkjfxhcaksvjnalsckuqpoiewt", []
array = [
    26, 27, 8, 7, 11, 25, 42, 24, 85, 94,
    21, 57, 21, 3, 67, 7, 0, 53, 24, 64,
    21, 86, 26, 86, 85, 52, 88, 29, 80, 86,
    8, 87, 87, 19, 93, 1, 93, 59, 74, 67,
    83, 5, 18, 10, 13, 50, 59, 60, 40, 12
]
for i in range(0, 0x15D, 7):
    j = i % len(key)
    _key.append(key[j])
for i, v in enumerate(array):
    print(chr(v ^ ord(_key[i])), end='')