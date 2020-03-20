# ws1
## Misc, 30 points

### Prompt

Find my password from this recording (:

*Author: JoshDaBosh*

### Solution

We are given a `.pcap` file, but there was a lot of stuff to scroll through so I just tried `strings recording.pcapng | grep actf`, and it worked! The flag was `actf{wireshark_isn't_so_bad_huh-a9d8g99ikdf}`.
