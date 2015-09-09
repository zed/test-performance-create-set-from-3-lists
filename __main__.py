#!/usr/bin/env python
"""Measure time performance of creating a set from 3 lists."""
from __future__ import print_function
import os
import random
import sys
import subprocess

seed = random.randrange(1, 4294967296)
env = dict(os.environ, PYTHONHASHSEED=str(seed))
print("PYTHONHASHSEED=%d" % seed)
for code in [
        'set(A+B+C)',
        'set(A).update(B, C)',
        's = set(A); s.update(B, C)',
        's = set(A); s.update(B, C); del s',
        'set(itertools.chain(A,B,C))']:
    print(code, end=': ')
    sys.stdout.flush()
    subprocess.check_call([sys.executable, '-m', 'timeit', '-s',"""
import itertools
import random
random.seed(%d)
n = 1000000
A = [random.randrange(1<<30) for _ in range(n)]
B = [random.randrange(1<<30) for _ in range(n)]
C = [random.randrange(1<<30) for _ in range(n)]""" % seed, code], env=env)
