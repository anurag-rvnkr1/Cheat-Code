#!/bin/bash

: '
193. Valid Phone Numbers

Given a text file file.txt that contains one phone number per line,
print all valid phone numbers.

A valid phone number must appear in one of the following formats:

    (xxx) xxx-xxxx
    xxx-xxx-xxxx

Where x is a digit (0-9).

Example:

Input (file.txt):
987-123-4567
123 456 7890
(123) 456-7890
(123)456-7890

Output:
987-123-4567
(123) 456-7890

Constraints:
    file.txt contains one phone number per line.
'

# Regular Expression using grep

grep -E '^([0-9]{3}-[0-9]{3}-[0-9]{4}|\([0-9]{3}\)[[:space:]][0-9]{3}-[0-9]{4})$' file.txt
