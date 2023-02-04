#!/bin/python

import sys
import os


def smooth_share(fns, in_one_bucket):
    dir_cnt = len(fns) // in_one_bucket
    addition = len(fns) / dir_cnt
    
    cnt_threshold = int(addition)
    bucket_idx = 0
    bs = [[] for i in range(dir_cnt)]
    
    for i in range(len(fns)):
        if i >= cnt_threshold:
            bucket_idx += 1
            cnt_fl = addition * (bucket_idx + 1)
            cnt_threshold = int(cnt_fl)
        bs[bucket_idx].append(fns[i])
            
    return bs
    
    
def ut():
    print("expected:", [['x', 'x'], ['x', 'x', 'x']])
    print("actual:", smooth_share(['x' for i in range(5)], 2))
    print()
    print("expected:", [['x', 'x'], ['x', 'x'], ['x', 'x']])
    print("actual:", smooth_share(['x' for i in range(6)], 2))
    print()
    
    buckets = smooth_share([str(i) for i in range(2744)], 100)
    print("actual:", [len(buck) for buck in buckets])
    
   
def actual_func():
    with open(sys.argv[1], "r") as inp:
       fns = inp.readlines()
    
    buckets = smooth_share(fns, 100)
    
    for i, buck in enumerate(buckets):
        cmd = ""
        
        dir = "%02d" % (i + 1)
        cmd += "mkdir %s; " % dir
        
        basenames = ["'%s'" % os.path.basename(fn.rstrip()) for fn in buckets[i]]
        names_str = " ".join(basenames)
        cmd += "mv %s %s" % (names_str, dir)
        
        print(cmd)


if __name__ == "__main__":
    # ut()
    actual_func()
    
