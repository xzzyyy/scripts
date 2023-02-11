#!/bin/python

import os
import random

EXTENSIONS = [".jpg", ".png", ".mp4", ".m4v", ".mov", ".webm"]


def shuffle(all_files):
    filt_files = []
    old_new = []

    for fn in all_files:
        name, ext = os.path.splitext(fn)
        if ext.lower() in EXTENSIONS:
            filt_files.append((name, ext))

    random.shuffle(filt_files)
    frmt = "%%0%dd" % len(str(len(filt_files)))

    for i, (old_name, ext) in enumerate(filt_files):
        new_name = frmt % i
        print("%s%s > %s%s" % (old_name, ext, new_name, ext))
        old_new.append((old_name + ext, new_name + ext))

    return old_new


if __name__ == "__main__":
    randomized = shuffle(os.listdir())
    for old, new in randomized:
        os.rename(old, new)
