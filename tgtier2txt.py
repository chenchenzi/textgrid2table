# !/usr/bin/python
# textgridtier2csv.py D. Gibbon 2015.02.12
# modified by C. Xu 2020.04.07

# Description: Convert long, short and csv/txt format Praat information

# ----------------------------------------------------------
# Import standard modules

import os
import re
import sys

# ----------------------------------------------------------
# Input TextGrid from CLII

if len(sys.argv) < 3:
    print("Usage:", sys.argv[0], '<filename> <tiername>')
    exit()
fname = sys.argv[1]
tname = sys.argv[2]

if not os.path.isfile(fname):
    print("File", fname, "does not exist.")
    exit()

textgrid = open(fname, 'r').read().split('\n')
fname = sys.argv[1].split('.')[0]
print("Reading the Textgrid file..." + fname)

# ----------------------------------------------------------
# Remove initial and final spaces

nugrid = []
for line in textgrid:
    # a = ''
    line = re.sub(' *$', '', line)  # final spaces
    line = re.sub('^\t+', '', line)  # initial spaces
    line = re.sub('\"', '', line)  # remove quotation marks
    if line != '':
        nugrid += [line]

# ----------------------------------------------------------
# Parse TextGrid for tiers-interval tuples


def extracttiers(nugrid, outflag):
    tierkey = ''
    returnstring = ''
    output = ''
    val = ''
    start = 0

    if outflag not in ['file', 'string']:
        tierkey = outflag

    for i in range(len(nugrid)):
        l1 = nugrid[i].split(' = ')  # split when there is a =

        if len(l1) > 1:
            val = l1[1]  # the second item after the split

        if val == 'IntervalTier':
            if start > 0:
                if tierkey == tname:  # the right tier that's asked for
                    with open(fname + '.txt', 'w') as f:
                        f.write(output)
                    return output

            output = ''
            tierkey = nugrid[i+1].split(' = ')[1]
            print("The tier name is " + tierkey)
            start = 1  # having found one tier and then enter the if above

# actual output in the csv file
        l2 = nugrid[i].split(' ')  # intervals: VS intervals
        if l2[0] == 'intervals':  # the first item after the split
            xmin = nugrid[i+1].split(' = ')[1]
            xmax = nugrid[i+2].split(' = ')[1]
            text = nugrid[i+3].split(' = ')[1]
            dur = str("{:.4f}".format(float(xmax)-float(xmin)))
            interval = text+'\t'+xmin+'\t'+xmax+'\t'+dur+'\t'+fname+'\n'
            output += interval


print(extracttiers(nugrid, tname))
