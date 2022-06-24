# Sum Columns

## First step

1. Go to https://www.learnpython.org and perform the "Learn the Basics" tutorials
2. Read https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

## Assignment

The milestone is to write a program that parses a CSV.

What is a CSV?
A csv (Comma Separated Values) is a comma delimited file. For example:
"Name","Gender","Age"
"John","M","12"
"Sean","M","43"
"Victoria","F","39"

Note:

- The first line is column titles
- All values are in double-quotes and separated by commas

Write a program in python:
sum-columns <filename> <column-number>

Example:

```
$ sum-columns expenses.csv 3
The total 'amount' is 5,384.2
```

The program will:
(a) Open a csv text file.
(b) Go over all values in the column
(c) Return the sum, formatted nicely.

Few csv files with real data are attached, please use them.

The source of the data is:
https://catalog.data.gov/dataset?res_format=CSV

Enjoy, and feel free to ask any question.
