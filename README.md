## The Goldsrc Overbright Patcher

### What is this?

This is a short Python script which changes one byte in the pre-Anniversary Update hw.dll from the steam_legacy branch (CRC32 `F7DCFFD9`), [fixing the gl_overbright command](https://github.com/ValveSoftware/halflife/issues/230) in Goldsrc games like Half-Life. Eliminates the need for third party tools like GLIntercept. Might disable detail textures, but they are not used in the base game anyway. [Put the .py script](https://raw.githubusercontent.com/54ac/goldsrc-overbright-patcher/main/hwpatcher.py) in the same folder as hw.dll and launch with `python hwpatcher.py` in the command line. The original file will be backed up as hw.bak. Would not recommend for online play, just in case.

### Slightly more detailed explanation

When hw.dll establishes GL_ARB_multitexture support, it calculates the amount of available texture units. Then, if any texture units are detected, overbright gets disabled. This patch changes one byte to keep gl_overbright available regardless of the amount of texture units. If you want to do it manually, open hw.dll with a hex editor, go to offset `290143`, and change `74` to `7D`.

### Note on Anniversary Update

The 25th Anniversary Update uses gl_use_shaders to mimic the overbright effect, rendering this script obsolete.
