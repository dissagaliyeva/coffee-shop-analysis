# Project: Ukrainian coffee market segments

### Introduction
The analysis was conducted to understand the current coffee market in Ukraine. This information 
would then be used to create marketing plans to expand the businesses. To understand the market, 
we were supplemented with a dataset consisting of 200 entries that were evenly spread across 
10 regions. It’s also important to mention that, even though there are ten cities, the number 
of unique regions is nine. There are two cities, Khrivoy Rog and Dnipro, that represent the 
same Dnipropetrovsk region.

This notebook discusses the methods that were used for data cleaning, exploratory data analysis, 
feature engineering and model selection. Since the end-goal was to find the segments, there was a need to select 
an appropriate unsupervised algorithm. The dataset had more categorical values than numeric, 
there were two algorithms implemented: K-Means and K-Prototype.

