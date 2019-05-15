# Zippy
## Forensics, 50 points

### Prompt

Got a zip file, but our stupid admin, Blue, couldn't even open it. Can you?

### Solution

If you try to unzip the ZIP archive that we are provided with, we get an error:

```
→ unzip flag.zip
Archive:  flag.zip
file #1:  bad zipfile offset (local header sig):  0
```

Based on the fact it mentions something about the `local header`, there's probably an issue with the file header. If we run `xxd` on the ZIP archive, we see that the first 4 bytes, where the header normally is, are zeroes:

```
→ xxd flag.zip
00000000: 0000 0000 1400 0200 0800 ca90 7c4e 2b7d  ............|N+}
00000010: d22d 1400 0000 1600 0000 0800 1c00 666c  .-............fl
00000020: 6167 2e74 7874 5554 0900 036b 539d 5c6b  ag.txtUT...kS.\k
.
.
.
```

Luckily this is an easy fix. First, get the 4 bytes that *should* be at the beginning of the file, which can be found on the [Wikipedia article](https://en.wikipedia.org/wiki/Zip_(file_format)#File_headers) for the ZIP file format. The ZIP archive should have the 4 bytes `504b0304` (big endian) starting at the 0th byte. We can open up the ZIP file in your favorite hex editor (I used Bless) and replace the 4 zero bytes with the correct header.

Now unzip the archive and you can `cat` the flag: `CSACTF{z1ppy_z1p_z1p}`
