# Misdirection
## Web, 100 points

### Prompt

Looks like someone gave you the wrong directions!

http://ctfchallenges.ritsec.club:5000/

### Solution

If you try to access the website through a browser, nothing will load. Based on the name of the challenge, I tried to access the website with `wget` and made sure it would follow redirects:


```shell
→ wget ctfchallenges.ritsec.club:5000 --max-redirect 50
--2019-11-15 11:38:31--  http://ctfchallenges.ritsec.club:5000/
Resolving ctfchallenges.ritsec.club (ctfchallenges.ritsec.club)... 129.21.228.105
Connecting to ctfchallenges.ritsec.club (ctfchallenges.ritsec.club)|129.21.228.105|:5000... connected.
HTTP request sent, awaiting response... 302 FOUND
Location: http://ctfchallenges.ritsec.club:5000/R [following]
--2019-11-15 11:38:31--  http://ctfchallenges.ritsec.club:5000/R
Reusing existing connection to ctfchallenges.ritsec.club:5000.
HTTP request sent, awaiting response... 302 FOUND
Location: http://ctfchallenges.ritsec.club:5000/S [following]
--2019-11-15 11:38:31--  http://ctfchallenges.ritsec.club:5000/S
Reusing existing connection to ctfchallenges.ritsec.club:5000.
HTTP request sent, awaiting response... 302 FOUND
Location: http://ctfchallenges.ritsec.club:5000/{ [following]
--2019-11-15 11:38:31--  http://ctfchallenges.ritsec.club:5000/%7B
Reusing existing connection to ctfchallenges.ritsec.club:5000.
HTTP request sent, awaiting response... 302 FOUND
Location: http://ctfchallenges.ritsec.club:5000/4 [following]
--2019-11-15 11:38:31--  http://ctfchallenges.ritsec.club:5000/4
Reusing existing connection to ctfchallenges.ritsec.club:5000.
HTTP request sent, awaiting response... 302 FOUND
Location: http://ctfchallenges.ritsec.club:5000/! [following]
.
.
.
```

As you can see, each request gives you a new character of the flag. After some rearranging, you can recreate the original flag: `RS{4!way5_Ke3p-m0v1ng}`.
