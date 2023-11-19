import os
import binascii

HW_FILENAME = "hw.dll"
HW_BACKUP_FILENAME = "hw.bak"

CRC = 0xF7DCFFD9
PATCHED_CRC = 0xEE0C834E
POS = 290143

if not os.path.isfile(HW_FILENAME):
    input("hw.dll not found")
    quit()

# read hw.dll and calculate crc
with open(HW_FILENAME, "rb") as f:
    content = f.read()
    file_crc = binascii.crc32(content) & 0xFFFFFFFF
    f.close()

if file_crc == PATCHED_CRC:
    input("hw.dll is already patched")
    quit()
elif file_crc != CRC or content[POS] != 0x74:
    input("can't recognize hw.dll")
    quit()

# patch hw.dll
content = content[:POS] + b"\x7D" + content[POS + 1 :]

if content[POS] != 0x7D:
    input("unable to patch hw.dll")
    quit()

# delete hw.bak if it exists
if os.path.isfile(HW_BACKUP_FILENAME):
    os.remove(HW_BACKUP_FILENAME)

# rename hw.dll to hw.bak and write patched hw.dll
os.rename(HW_FILENAME, HW_BACKUP_FILENAME)
with open(HW_FILENAME, "wb") as f:
    f.write(content)
    f.close()
    input("hw.dll successfully patched")
