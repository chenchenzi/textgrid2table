# !/usr/bin/python
# tgshort2txt.py C. Xu 2020.04.08

# Input: short form TextGrid
# Output: txt table with praat information

# ----------------------------------------------------------
# Import standard modules

import os
import re
import sys

# ----------------------------------------------------------
# Input TextGrid from CLII

if len(sys.argv) < 4:
    print("Usage:", sys.argv[0], '<filename> <tiername1> <tiername2>')
    exit()
fname = sys.argv[1]
tname1 = sys.argv[2]
tname2 = sys.argv[3]

if not os.path.isfile(fname):
    print("File", fname, "does not exist.")
    exit()

textgrid = open(fname, 'r').read().split('\n')
print("Reading the Textgrid file..." + fname)
fname = sys.argv[1].split('.')[0]

# ----------------------------------------------------------
# Remove initial and final spaces

nugrid = []
for line in textgrid:
    # a = ''
    line = re.sub(' *$', '', line)  # final spaces
    # line = re.sub('^\t+', '', line)  # initial spaces
    line = re.sub('\"', '', line)  # remove quotation marks
    line = re.sub('IntervalTier', '0', line)
    line = re.sub(tname1, '0', line)
    line = re.sub(tname2, '0', line)
    if line != '':
        nugrid += [line]

# ----------------------------------------------------------
# Parse TextGrid for tiers-interval tuples

output = ''

for i in range(len(nugrid)):

    text = nugrid[i]
    xmax = nugrid[i-1]

    if text.isalpha() and xmax.replace('.', '').isdigit():

        xmin = "{:.4f}".format(float(nugrid[i-2]))
        xmax = "{:.4f}".format(float(xmax))
        dur = "{:.4f}".format(float(xmax)-float(xmin))
        interval = text+'\t'+xmin+'\t'+xmax+'\t'+dur+'\t'+fname+'\n'
        output += interval

print(output)
with open(fname + '.txt', 'w') as f:
    f.write(output)
