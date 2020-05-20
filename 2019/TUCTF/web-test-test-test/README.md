# Test Test Test
## Web, 179 points

### Prompt

There are so many tests going on right now, why don't take a deep breath and list them out before you forget one?

### Solution

If you access the webpage, you will only see some text and an image. When you look at the page source, you can see that there is an `/img` directory. In that directory is a `TODO.txt` file that says they want to remove that flag from `flag.php`. If you `wget` that page, you will see this:

```html
<link href="test.css" rel="stylesheet" type="text/css">TODO: put more stuff here before the test<br>Then print the flag TUCTF{d0nt_l34v3_y0ur_d1r3ct0ry_h4n61n6}<meta http-equiv='refresh' content='0;url=index.html'>
```

Flag: `TUCTF{d0nt_l34v3_y0ur_d1r3ct0ry_h4n61n6}`.
