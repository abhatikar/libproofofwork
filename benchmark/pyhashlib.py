#!/usr/bin/env python3
import hashlib
import itertools
import sys
funcname = sys.argv[1]
func = { 'md5': hashlib.md5, 'sha1': hashlib.sha1, 'sha256': hashlib.sha256 }[funcname]

for i in itertools.count():
    s = str(i).encode()
    digest = func(s).hexdigest()
    if digest.startswith('c0ffee'):
        break

print(funcname)
print('c0ffee')
print(i)
print(i)
