#!/bin/bash


# mode the date
#python scripts/mod_date.py

# split input into train set and test set
#python scripts/split.py

# gen prediction output
python scripts/gen_output.py

# calc nums
python scripts/calc.py
