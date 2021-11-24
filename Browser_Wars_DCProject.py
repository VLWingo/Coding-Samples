# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:14:36 2021

@author: Victoria Wingo

datacamp Unguided Project: Comparing Search Interest with Google Trends
"""
# packages
import pandas as pd

location = "worldwide_browser_trends.csv"
browser_df = pd.read_csv(location, index_col = 0)

# #1 Find the six month rolling average (a.k.a. simple moving average) for each
# date and browser in the dataset. Save your answer as pandas DataFrame called
# rolling_six with the column Month as the index. Null values are acceptable for
# dates where a rolling six month average can't be generated.

# The following code was done by hand before discovering the pd.rolling method
# 
# rolling_six = pd.DataFrame(index = months)
# for col in browser_df.columns:
#     results = []
#     for n in range(browser_df.shape[0]):
#         if n in range(5):
#             results.append(None)
#         else:
#             results.append(sum(browser_df[col].iloc[(n-5):n+1]) / 6)
#     rolling_six[col] = results

rolling_six = browser_df.rolling(window = 6).mean()
rolling_six.plot(title="6 Month Rolling Avg")

# #2 Similar to above, create a DataFrame called pct_change_quarterly with the
# percentage change from the previous quarter for each date and browser.
# The values should be in percentage format, so 5 instead of 0.05. Since Chrome
# launched in late 2008, only include dates during or after 2009.

# The following code was done by hand before discovering the pd.pct_change method
# 
# pct_change_quarterly = pd.DataFrame(index = browser_df.index)
# for col in cols:
#     results = []
#     for n in range(browser_df.shape[0]):
#         if n == 0:
#             results.append(None)
#         else:
#               results.append(((
#                              browser_df[col].iloc[n] 
#                              -
#                              browser_df[col].iloc[n-3]) 
#                              / 
#                              browser_df[col].iloc[n-3]) 
#                              * 100)
#     pct_change_quarterly[col] = results
# pct_change_quarterly = pct_change_quarterly['2009-01':]

pct_change_quarterly = browser_df.pct_change(3) * 100
pct_change_quarterly = pct_change_quarterly['2009-01':]
pct_change_quarterly.plot(subplots=True, figsize=(12,8))

# #3 From the earlier questions, you can see that even though Chrome eventually
# overtook Firefox, Chrome's growth has had its fair share of ups and downs.
# You will illustrate this by comparing Chrome's annual Google Trends performance
# in 2009, 2012, 2015, and 2018 in a DataFrame called chrome_trends. It should
# hold the search interest for Chrome with four columns for each year and twelve
# rows for each month of the year.

years = columns=['2009', '2012', '2015', '2018']
chrome_trends = pd.DataFrame(index=range(1,13))
for year in years:
    months = [month for month in browser_df.index if year in month]
    chrome_trends[year] = list(browser_df['Google Chrome'].loc[months])
chrome_trends.plot(title="Chrome Search Performance in 2009, 2012, 2015 & 2018")


