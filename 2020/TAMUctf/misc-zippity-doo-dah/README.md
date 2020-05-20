# Zippity Doo Dah
## Misc, ? points

### Prompt

Lorelei, a nuclear engineer, is practicing how to create folders to organize her notes. She works closely with POTUS to secure our nuclear missiles. In order for her to send the nuclear codes to the correct authorities, she needs to zip all the files and make the data hard to find. Your mission, should you choose to accept it, is to intercept and find the codes (the flag).

### Solution
We are given a ZIP archive, and if you unzip it, you are presented with another ZIP archive. Unzip again, and you get a few hundred files, one of which is an image (the rest are text files):

![](random150.png)

After `file` and `strings` didn't turn up anything, I tried plugging it into my favorite [online steganography tool](https://stylesuxx.github.io/steganography/) and got the flag: `gigem{z1pT4st1c__$kiLl$$$}`.
