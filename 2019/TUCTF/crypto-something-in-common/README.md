# Something In Common
## Crypto, 403 points

### Prompt

We've managed to gather the details in the given file. We need a professional cryptographer to decipher the message. Are you up to the task?

### Solution
We are given the following information in a file:

```
n = 5196832088920565976847626600109930685983685377698793940303688567224093844213838345196177721067370218315332090523532228920532139397652718602647376176214689

e1 = 15

e2 = 13

c1 = 2042084937526293083328581576825435106672034183860987592520636048680382212041801675344422421233222921527377650749831658168085014081281116990629250092000069

c2 = 199621218068987060560259773620211396108271911964032609729865342591708524675430090445150449567825472793342358513366241310112450278540477486174011171344408
```

This looks like RSA judging from the name of the variables. Based on the name of the challenge, you can probably exploit the fact that both ciphertexts used a common modulus (n) to encrypt. You can read more about the technique [here](https://medium.com/bugbountywriteup/rsa-attacks-common-modulus-7bdb34f331a5), but luckily people have already developed programs to automate this. I used [this one](https://github.com/a0xnirudh/Exploits-and-Scripts/blob/master/RSA%20Attacks/RSA:%20Common%20modulus%20attack.py), written by Anirudh Anand. I plugged in the values, ran the scipt, did some decoding, and then got the flag: `TUCTF{Y0U_SH0ULDNT_R3US3_TH3_M0DULUS}`.
