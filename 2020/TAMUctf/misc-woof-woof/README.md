# Woof Woof
## Misc, 50 points

### Prompt
![](reveille.jpg)

### Solution

As I usually do with image files, I first ran `file` on the photo:

```shell
→ file reveille.jpg
reveille.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 300x300, segment length 16, comment: "woof woof bark ruff bark bark ruff woof woof bark ruff bark ruff woof woof ruff woof bark bark", progressive, precision 8, 480x720, components 3
```

The comment caught my eye, so I ran `strings` on the file and this was the whole "ciphertext":
```
woof woof bark ruff bark bark ruff woof woof bark ruff bark ruff woof woof ruff woof bark bark bark bark woof ruff woof bark bark ruff woof woof woof woof woof ruff woof woof bark ruff woof ruff bark woof woof bark woof bark ruff bark bark bark ruff woof ruff bark woof woof woof woof ruff woof bark woof bark ruff bark woof woof woof ruff woof woof woof woof woof ruff woof bark bark bark ruff woof bark bark bark bark woof
```

At first I thought it couldn't be binary or Morse code since there were three types of "characters" (woof, bark, ruff), but after trying different esolangs to no avail, I came back to that idea. I wrote a Python script to convert the different words into 1s, 0s and spaces so I could try replacing them to see what worked and what didn't:

```python
a ="woof woof bark ruff bark bark ruff woof woof bark ruff bark ruff woof woof ruff woof bark bark bark bark woof ruff woof bark bark ruff woof woof woof woof woof ruff woof woof bark ruff woof ruff bark woof woof bark woof bark ruff bark bark bark ruff woof ruff bark woof woof woof woof ruff woof bark woof bark ruff bark woof woof woof ruff woof woof woof woof woof ruff woof bark bark bark ruff woof bark bark bark bark woof"

a = a.replace("woof", "0")
a = a.replace("bark", "1")
a = a.replace(" ", "")
a = a.replace("ruff", " ")

print(a)
```

After some trial and error, this was the Morse code that worked:

```
--. .. --. . -- -....- -.. ----- --. - .--.-. ... - .---- -.-. .--- ----- -... -....-
```

which translated to the flag `GIGEM-D0GT@ST1CJ0B-`.
