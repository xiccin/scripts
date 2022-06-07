#!/bin/bash

tput civis
folder_location="data/fastdl/maps"

# discard un-pushed commits 
git reset HEAD~1

mkdir frag-cache
git ls-files > frag-cache/pushed.list

for filename in $folder_location/*
do
    if grep -qF "$filename" frag-cache/pushed.list
    then
        continue
    else
        clear
        echo -e "pushing: $filename \n"
        git add $filename
        git commit -m "maps fragment"
        echo "" 
        git push -f
    fi    
done

git add $folder_location
git commit -m "maps fragment"
git push -f

rm -r frag-cache
