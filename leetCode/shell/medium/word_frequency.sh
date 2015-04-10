#! /bin/bash
tr -cs 'a-z' '\n' < words.txt | sort | uniq -c | sort -rn | sed -r 's/\s*([0-9]+)\s+([a-z]+)/\2 \1/'
