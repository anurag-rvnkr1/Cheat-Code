#!/bin/bash

: '
194. Transpose File

Given a text file file.txt, transpose its content.

The file contains a matrix where each row has the same number of columns,
and columns are separated by spaces.

Print the transpose of the matrix.

Example:

Input (file.txt):
name age
alice 21
ryan 30

Output:
name alice ryan
age 21 30

Constraints:
    Each row has the same number of fields.
    Fields are separated by a single space.
'

# AWK

awk '
{
    for (i = 1; i <= NF; i++) {
        if (NR == 1)
            transpose[i] = $i
        else
            transpose[i] = transpose[i] " " $i
    }
}
END {
    for (i = 1; i <= NF; i++)
        print transpose[i]
}
' file.txt
