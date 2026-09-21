#!/bin/bash

: '
192. Word Frequency

Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity:
    - Words consist only of lowercase characters.
    - Words are separated by one or more spaces.
    - Output should be sorted by descending frequency.

Example:

Input (words.txt):
the day is sunny the the
the sunny is is

Output:
the 4
is 3
sunny 2
day 1

Constraints:
    words.txt contains only lowercase English letters and spaces.
'

# Word Frequency using tr + sort + uniq

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{print $2, $1}'
