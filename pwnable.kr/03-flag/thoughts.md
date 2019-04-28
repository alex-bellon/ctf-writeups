Download the binary, opening it in Vim or running `strings` just produces some gibberish. It does mention it was packed in UPX Executable Packer, so off to Google. 

Alright, so it's used to pack/unpack things (who would have guessed?), so I'm just going to try to unpack the binary they gave me. 

Install UPX, run `upx --help` to find out what flags I need, then run `upx -d flag` which seems to work. In Vim it's still gibberish, but running `strings` yields actual words now so progress is being made. 

Tried running it, realized it doesn't have execute permissions, `chmod +x`, run again. It says: 

```
I will malloc() and strcpy the flag there. take it.
```

Ok then. Tried passing in a couple things as arguments, nothing happens. GDB isn't working (although I think it's just because I broke my GDB) so just go back to `strings flag`. After lots of scrolling, right under the 'malloc' message is what look like a flag, i.e. there's a smiley at the end. Try it out and yup, that's the flag. Nice.
