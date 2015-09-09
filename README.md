# [Why is creating a set from a concatenated list faster than using `.update`?](http://stackoverflow.com/q/32483539/4279)

[![build status on travis-ci.org][2]][1]

[1]: https://travis-ci.org/zed/test-performance-create-set-from-3-lists
[2]: https://api.travis-ci.org/zed/test-performance-create-set-from-3-lists.svg?branch=master

To measure time performance of creating a set from 3 lists, run `tox`.

### [Python 2.7 results](https://travis-ci.org/zed/test-performance-create-set-from-3-lists/jobs/79513761)

    set(A+B+C): 10 loops, best of 3: 656 msec per loop
    set(A).update(B, C): 10 loops, best of 3: 602 msec per loop
    s = set(A); s.update(B, C): 10 loops, best of 3: 701 msec per loop
    s = set(A); s.update(B, C); del s: 10 loops, best of 3: 614 msec per loop
    set(itertools.chain(A,B,C)): 10 loops, best of 3: 671 msec per loop

### [Pypy results](https://travis-ci.org/zed/test-performance-create-set-from-3-lists/jobs/79513768)

    set(A+B+C): 10 loops, best of 3: 470 msec per loop
    set(A).update(B, C): 10 loops, best of 3: 586 msec per loop
    s = set(A); s.update(B, C): 10 loops, best of 3: 560 msec per loop
    s = set(A); s.update(B, C); del s: 10 loops, best of 3: 566 msec per loop
    set(itertools.chain(A,B,C)): 10 loops, best of 3: 766 msec per loop
