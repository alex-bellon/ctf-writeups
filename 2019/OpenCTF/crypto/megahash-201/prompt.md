Ok, I figured out my problem. As always, the algorithm doesn't fail, it's just an implementation bug in my challenge! I was supposed to be using something called "salt" which I think is like a secret. That makes sense, since I gave you the algorithm, there was nothing secret protecting our password! Well I fixed it. Now we use a standard RFC 2014 HMAC to hash our passwords. The webserver has a random master secret, so even with whatever trick you found you won't know how your submission will be evaluated! Defense-in-depth baby, it never fails!

challenges.openctf.cat:9024

