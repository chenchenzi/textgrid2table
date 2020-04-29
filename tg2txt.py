# !/usr/bin/python
# tg2txt.py C. Xu 2020.04.08

# Install Package: praat-textgrids 1.3.1
# The package descrption says that it works with all three forms of textgrids
# but there seems to be some errors when read/parse the short form
# Input: long form TextGrid
# Output: txt table with praat information

# ----------------------------------------------------------
# Import standard modules

import os
import sys
import textgrids

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

try:
    grid = textgrids.TextGrid(fname)
    print("Reading the Textgrid file..." + fname)
except (textgrids.ParseError, textgrids.BinaryError):
    print("Not a recognised file format!", file=sys.stderr)

fname = sys.argv[1].split('.')[0]
# grid = grid.write(fname+'.TextGrid', fmt=TEXT_LONG).TextGrid()

tier = ''
for syll in grid[tname]:
    label = syll.text.transcode()
    smin = '{:.4f}'.format(syll.xmin)
    smax = '{:.4f}'.format(syll.xmax)
    sdur = '{:.4f}'.format(syll.dur)
    interval = label+'\t'+smin+'\t'+smax+'\t'+sdur+'\t'+fname+'\n'
    tier += interval

print(tier)
with open(fname + '.txt', 'w') as f:
    f.write(tier)
# write a new txt file. You can change the extension  to .csv too.
