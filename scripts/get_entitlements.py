import json

with open('C:\\Program Files (x86)\\Zwift\\ZwiftApp.exe', 'rb') as f:
    za = f.read()
data = []
s = 0
while True:
    p = za.find(b'\x45\x4E\x54\x49\x54\x4C\x45\x4D\x45\x4E\x54\x5F', s)
    if p != -1:
        i = p
        while za[i] != 0 and za[i] != 16:
            i += 1
        if za[i] == 0:
            data.append(za[p:i].decode("utf-8"))
        s = i
    else:
        break
with open('entitlements.txt', 'w') as f:
    json.dump(sorted(data), f, indent=2)
