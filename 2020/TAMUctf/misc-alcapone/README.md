# ALCAPONE
## Misc, 50 points

### Prompt

Eliot Ness is the lead on taking down Al Capone. He has gained access to Capone's personal computer but being the good detective he is, he got the disk image of the computer rather than look through the actual computer. Can you help Ness out and find any information to take down the mob boss?

(hint: Al Capone knew his computer was going to be taken soon, so he deleted all important data to ensure no one could see it. Little did he know that Ness was smarter than him.)

Direct Download link: https://tamuctf.com/themes/core/static/img/WindowsXP.img.xz

### Solution

The image we were given was huge, and I actually didn't know how to preoperly mount it so I could look through it manually. So of course, I tried the low hanging fruit and checked if `strings` would work:

```shell
→ strings WindowsXP.img | grep gigem
dgkjsdhfgiohsdfiohsodfghsogigemshdrogihaorhgo
sdfgkgigemhuisrgkjshdfiguhsiurgsjkrhgisuheri
avjkdfvkndkmfnvauerhgioqhaegnalgigemgadgadg
asgjahgigemuergauirgluarguiawHEIGHWeog
sdfgksdioghuisrgkjshdfiguhsgigemgsjkrhgisuheri
dgkjsdhfgiohsdfiohsodfghsogigemshdrogihaorhgo
sdfgkgigemhuisrgkjshdfiguhsiurgsjkrhgisuheri
avjkdfvkndkmfnvauerhgioqhaegnalgigemgadgadg
asgjahgigemuergauirgluarguiawHEIGHWeog
sdfgksdioghuisrgkjshdfiguhsgigemgsjkrhgisuheri
oigigem{Ch4Nn3l_1Nn3R_3l10t_N3$$}khsutrghsiserg
sdkjfghsifvjkgigemuerghiuerhgijkjno0uihoh
sdkjfghsifvjksndgigemuerghiuerhgijkjno0uihoh
```

Turns out it did! The flag was `gigem{Ch4Nn3l_1Nn3R_3l10t_N3$$}`.
