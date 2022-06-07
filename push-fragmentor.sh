#!/bin/bash

folder_location="data/fastdl/maps"

# discard un-pushed commits 
git reset HEAD~1 >& /dev/null

for filename in $folder_location/*
do
    clear
    git add $filename
    git commit -m "maps fragment"
    git push
done

