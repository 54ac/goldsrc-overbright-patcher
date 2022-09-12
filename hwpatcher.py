import os

orig = b"\x83\xC4\x04\x3B\xC6\x74\x14\x56\x68\x28\x73"
repl = b"\x83\xC4\x04\x3B\xC6\x7D\x14\x56\x68\x28\x73"
fname = "hw.dll"

try:
    with open(fname, "rb") as f:
        content = f.read()
        newcontent = content.replace(orig, repl)
        f.close()
except:
    input("hw.dll not found")
    quit()

if (newcontent.find(repl) > -1):
    os.rename(fname, "hw.bak")
    with open(fname, "wb") as f:
        f.write(newcontent)
        f.close()
        input("hw.dll successfully patched")
else:
    input("couldn't find necessary data in hw.dll")