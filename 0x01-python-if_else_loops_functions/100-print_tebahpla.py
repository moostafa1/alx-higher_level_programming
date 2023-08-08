#!/usr/bin/python3
c = 1
diff = 0
for i in reversed(range(97, 123)):
    print("{}".format(chr(i - diff)), end='')
    c += 1
    if not c % 2:
        diff = 32
    else:
        diff = 0

