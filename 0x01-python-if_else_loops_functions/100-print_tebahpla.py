#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 != 0:
        i = i - 32
    print('{:s}'.format(chr(i)), end="")
