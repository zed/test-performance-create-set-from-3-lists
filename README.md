# [Why is creating a set from a concatenated list faster than using `.update`?](http://stackoverflow.com/q/32483539/4279)

[![build status on travis-ci.org][2]][1]

[1]: https://travis-ci.org/zed/test-performance-create-set-from-3-lists
[2]: https://api.travis-ci.org/zed/test-performance-create-set-from-3-lists.svg?branch=master

To measure time performance of creating a set from 3 lists, run `tox`.

### [Python 2.7 results](https://travis-ci.org/zed/test-performance-create-set-from-3-lists/jobs/79507962)

    set(A+B+C): 10 loops, best of 3: 643 msec per loop
    set(A).update(B, C): 10 loops, best of 3: 565 msec per loop
    set(itertools.chain(A,B,C)): 10 loops, best of 3: 612 msec per loop

### [Pypy results](https://travis-ci.org/zed/test-performance-create-set-from-3-lists/jobs/79507967)

    set(A+B+C): 10 loops, best of 3: 472 msec per loop
    set(A).update(B, C): 10 loops, best of 3: 572 msec per loop
    set(itertools.chain(A,B,C)): 10 loops, best of 3: 783 msec per loop
