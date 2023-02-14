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
        old_new.append((old_name + ext, new_name + ext))

    return old_new


def add_suffix(fn, suffix):
    basename, ext = os.path.splitext(fn)
    basename += "." + suffix
    return basename + ext


def top_dir(path):
    return os.path.basename(os.path.abspath(path))


def shuffle_files(fld):
    suffix = top_dir(fld)
    os.chdir(fld)

    old_fns = os.listdir(".")
    old_new = shuffle(old_fns)
    old_fns_filtered = [old for old, new in old_new]

    tmp_for_old = "old"
    os.mkdir(tmp_for_old)
    for fn in old_fns_filtered:
        shutil.move(fn, "%s/%s" % (tmp_for_old, fn))

    for old, new in old_new:
        new_sfx = add_suffix(new, suffix)
        shutil.move("%s/%s" % (tmp_for_old, old), new_sfx)
        print("'%s' ---> '%s'" % (old, new_sfx))
    os.rmdir(tmp_for_old)


if __name__ == "__main__":
    shuffle_files(".")
