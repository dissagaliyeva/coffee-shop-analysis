# Ukrainian coffee market segments

This project is an individual attempt to tackle unsupervised learning methods in a business context. It consists
of two main notebooks:
- **analysis.ipynb** = shows the complete code and explanation 
- **report.ipynb** = summarizes the work and presents the findings in a report-type of way


#### -- Project Status: Completed

## Objective

Coffee has become an integral part of our daily lives; it not only brightens our days but also brings **a lot**
of money. By 2027, the estimated revenue of such a business will bring $201.4 billion. Therefore, the purpose
of this project is to analyze the coffee shop market segments to make the right choice for expansion.

### Methods Used
* Data Cleaning
* Machine Learning
* Data Visualization, including T-SNE 
* Unsupervised learning algorithms: K-Means & K-Prototypes

### Technologies
* Python
* Pandas, sklearn, numpy, scipy
* matplotlib, seaborn, plotly
* etc. 

## Project Description

The analysis was conducted to understand the current coffee market in Ukraine. This information 
would then be used to create marketing plans to expand the businesses. To understand the market, 
we were supplemented with a dataset consisting of 200 entries that were evenly spread across 
10 regions. 

For starters, there was a need to deal with missing values and find the proper imputation methods. 
Overall, the number of rows with at least one missing value made up **60.5%**. Since dropping such a big 
number of values was not an option, majority of the time was spent on finding the right tools.
After fixing the missing value situation, the Exploratory Data Analysis took place. The following questions were
answered:
- **What's the most common shop in each region?** 
- **Do trends differ depending on the city's size?** 
- **Do rating/review ratio change with services provided?**

Finally, model selection and evaluation took place. Since the dataset was highly categorical,
using K-Means alone seemed like a bad idea. Thus, I also included K-Prototype algorithm that deals
with both categorical and numeric values. Surprisingly enough, both yielded almost identical clusters. 


## Needs of this project

- data exploration/descriptive statistics
- data mining
- data processing/cleaning
- statistical modeling
- writeup/reporting


## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](https://github.com/dissagaliyeva/ukrainian-coffee-market-analysis/blob/master/data/coffee_shops.csv) within this repo. 
3. Data processing/transformation scripts are being kept [here](https://github.com/dissagaliyeva/ukrainian-coffee-market-analysis/blob/master/analysis.ipynb)
4. Data report is kept [here](https://github.com/dissagaliyeva/ukrainian-coffee-market-analysis/blob/master/report.ipynb)


## Contributing 

**Team Leads (Contacts) : [Dinara Issagaliyeva](https://github.com/dissagaliyeva)**
