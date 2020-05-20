# Authy
## Forensics, ? points

### Prompt

I don't have the original prompt, but we were given the file `challenge.pcap`.

### Solution

We are given a `.pcap` file, so I opened it in Wireshark. There was a lot of TCP traffic, but there was also a GET request that stuck out at the beginning:

![](auth-header.png)

Considering the challenge is called Authy, I looked first at the Authorization field. It looked like Base64, so I decoded it and got the flag: `flag{bad_auth_headers_suck}`.
