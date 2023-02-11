#!/bin/python

import os
import shutil
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


def shuffle_files(fld):
    os.chdir(fld)
    old_new = shuffle(os.listdir("."))

    tmp = "tmp"
    os.mkdir(tmp)

    for old, new in old_new:
        shutil.move(old, tmp + "/" + new)
    for old, new in old_new:
        shutil.move(tmp + "/" + new, new)

    os.rmdir(tmp)


if __name__ == "__main__":
    shuffle_files(".")
