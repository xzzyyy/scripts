#!/bin/bash

for f in $@; do
	name=`stat $f | grep "Modify" | sed -E 's/^.+: [[:digit:]]{2}([[:digit:]]{2})-([[:digit:]]{2})-([[:digit:]]{2}) ([[:digit:]]{2}):([[:digit:]]{2}):([[:digit:]]{2})\..+$/\1\2\3-\4\5\6/'`
	new_fn=`echo $f | sed -E "s/^.+\./$name./"`
	cp $f $new_fn
done
