# EC2 Findings: Post-Crisis Economic-Resilience Research
Gunveer Singh, Grade 11, Castlebrooke Secondary School
Date: 2026-11-09

## Links to save
- GitHub: https://github.com/git-gunveer/post-crisis-economic-resilience
- StatCan source: https://www150.statcan.gc.ca/n1/tbl/csv/20100008-eng.zip
- StatCan Daily, March 2020: https://www150.statcan.gc.ca/n1/daily-quotidien/200522/dq200522a-eng.htm

## Question
Did people panic buy in March 2020, when COVID started?

## Data, real and counted
- 5,805 data points
- Source: Statistics Canada Table 20-10-0008-01, Retail trade sales by industry
- Scope: seasonally adjusted, Jan 2012 to Dec 2022, 17 places, 30 industries
- File: data/retail_2012_2022_clean.csv
- Code: code/02_grow_to_5000.py, Grade 11 Python with pandas

## Method, in plain words
Panic score = industry change Feb to Mar 2020, minus total retail change Feb to Mar 2020.
If a store type went up while retail as a whole went down, its panic score is high.
If it fell even more than retail as a whole, its panic score is low, negative.

## Findings
Total retail, Canada:
- Feb to Mar 2020: -11.66%
- Feb to Apr 2020: -32.49%

Top panic buying, March 2020:
- Supermarkets: +28.45%, panic score 40.1
- Grocery stores: +26.23%, panic score 37.9
- Food and beverage stores: +22.41%, panic score 34.1
- Cannabis stores: +19.86%, panic score 31.5
- Beer, wine and liquor stores: +13.87%, panic score 25.5

Biggest fall, March 2020:
- Shoe stores: -53.75%, panic score -42.1
- Clothing stores: -52.28%, panic score -40.6
- Clothing and accessories: -51.92%, panic score -40.3
- Jewellery, luggage and leather goods: -47.23%, panic score -35.6
- New car dealers: -40.85%, panic score -29.2

By place, total retail, Feb to Mar 2020:
- Montreal: -21.10%
- Quebec: -18.65%
- Prince Edward Island: -15.52%
- Canada: -11.66%
- Ontario: -9.19%
- British Columbia: -6.84%
- Nunavut: +3.19%, the only place up

## Note on the numbers
The first StatCan release in May 2020 said total -10.0% and food +22.8%.
This full table is a later revised version, so total is -11.66% and food is +22.41%.
Same story, slightly different numbers. I am using the revised table numbers here.

## What this is not yet
- 5,805 points, not 200,000
- No 15-page paper yet
- One shock only, COVID March 2020, no second shock checked yet

## Common App, Activity 2, now true
"Analyzed 5,000+ StatCan data points in Python to model consumer panic in March 2020; published code and findings on GitHub."
123 characters. Research, Independent Researcher, Grades 11-12, 4 hrs/week, 40 weeks/year, During the school year.
