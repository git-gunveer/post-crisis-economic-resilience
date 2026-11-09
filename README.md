# Post-Crisis Economic-Resilience Research

By Gunveer Singh, Grade 11, Castlebrooke Secondary School.

## My question
Did people panic buy in March 2020, when COVID started?

## What I did first
I started small. I took one StatCan release and checked 4 numbers.

Source: Statistics Canada, The Daily, Retail trade, March 2020, released May 22, 2020.
Link: https://www150.statcan.gc.ca/n1/daily-quotidien/200522/dq200522a-eng.htm

## What I found
- Total retail sales fell 10.0% in March 2020, to $47.1 billion.
- Food and beverage stores rose 22.8%.
- General merchandise stores rose 6.4%.
- Health and personal care stores rose 4.6%.

Food stores went up a lot while retail as a whole went down. That fits panic buying. People stocked up on food and other basic things.

## How to run my code
1. Install pandas: pip install pandas
2. Run this file: python code/01_clean_first_dataset.py
3. It reads data/march_2020_retail.csv and saves data/march_2020_retail_clean.csv

## Step 2, done 2026-11-09: 5,805 data points
I grew it from 4 rows to 5,805 real StatCan data points.
Scope: Statistics Canada Table 20-10-0008-01, seasonally adjusted, Jan 2012 to Dec 2022, 17 places, 30 industries. File: data/retail_2012_2022_clean.csv
Code: code/02_grow_to_5000.py

## What I found in the bigger dataset
- Total retail, Canada, Feb to Mar 2020: -11.66%. Feb to Apr 2020: -32.49%.
- Top panic buying, Mar 2020: supermarkets up 28.45%, panic score 40.1. Grocery stores up 26.23%, panic score 37.9. Food and beverage stores up 22.41%, panic score 34.1.
- Biggest fall, Mar 2020: shoe stores down 53.75%, clothing stores down 52.28%, clothing and accessories down 51.92%.
- By place, Mar 2020: Montreal down 21.10%, Quebec down 18.65%, Prince Edward Island down 15.52%, Canada down 11.66%, Nunavut up 3.19%.
- Note: the first release said total -10.0% and food +22.8%. This full table is a later revised version, so total is -11.66% and food is +22.41%. Same story, slightly different numbers.

## What this is not yet
This is 5,805 points, not 200,000. I have not written the 15-page paper yet.
My next step is to write up the findings, and check a second shock, not just COVID.

## Files
- data/march_2020_retail.csv - the 4 numbers I typed from StatCan
- code/01_clean_first_dataset.py - my Python code, in plain words
- README.md - this file
