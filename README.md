# Textgrid2table
Converting a Textgrid file to a more readable table format in `.txt` or `.csv`.

## Introduction

The three `.py` files are all Python 3 snippets.

`tg2txt.py` and `tgtier2txt.py` take the **long form** Textgrid, and return a `.txt` file for **the desired tier**.
These two have the same function but you need to install the [package](https://pypi.org/project/praat-textgrids/) `praat-textgrids 1.3.1` for the first script to work.
Alternatively, you can use the second script, which is modified from D. Gibbon's [script](http://wwwhomes.uni-bielefeld.de/gibbon/Forms/Python/PHONETICS/textgrid2csv.html).

`tgshort2txt.py` takes the **short form** Textgrid, and return a `.txt` file for **all the tiers**. It was used for post-alignment processing for me, so I assume that there are two tiers in total.

## Demonstration
It is fairly straightforward to run them.
In your Terminal, first navigate to the `/textgrid2table/` directory.

If you have:
- [x] Long form `.Textgrid`
- [x] Interested in one particular tier
- [x] Installed `praat-textgrids 1.3.1`

```
Python tg2txt.py filename tiername
```
or 
- [x] Long form `.Textgrid`
- [x] Interested in one particular tier

```
Python tgtier2txt.py filename tiername
```

or

- [x] Short form `.Textgrid`
```
Python tgtier2txt.py filename tiername1 tiername2
```
