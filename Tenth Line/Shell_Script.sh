#!/bin/bash

: '
195. Tenth Line

Given a text file file.txt, print just the 10th line of the file.

If the file has fewer than 10 lines, print nothing.

Example:

Input (file.txt):
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Line 11

Output:
Line 10

Constraints:
    file.txt contains one or more lines of text.
'

# sed

sed -n '10p' file.txt
