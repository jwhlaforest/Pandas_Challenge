
### Heroes Of Pymoli Data Analysis
* Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

* Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
-----

### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()

## Player Count

* Display the total number of players


#number of unique players calculation
players_df = purchase_data.loc[:,['Gender','SN','Age']]
total_players = players_df['SN'].nunique()
pd.DataFrame({'Total Players':[total_players]})

print('Total Players:',total_players)

## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


#calculations
unique_items = len(purchase_data['Item ID'].unique())
avg_price = purchase_data['Price'].mean()
purchase_count = purchase_data['Price'].count()
total_revenue = purchase_data['Price'].sum()

#table creation
summary_table = pd.DataFrame({'Unique Items': [unique_items],
                              'Average Price': [avg_price],
                              'Number of Purchases': [purchase_count],
                              'Total Revenue': [total_revenue]})

#table cleanup
summary_table ['Average Price'] = summary_table['Average Price'].map('${:,.2f}'.format)
summary_table ['Number of Purchases'] = summary_table['Number of Purchases'].map('{:,}'.format)
summary_table ['Total Revenue'] = summary_table['Total Revenue'].map('${:,.2f}'.format)

summary_table

## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed




#calculations
demo_total = players_df['Gender'].value_counts()
demo_perc = (demo_total / total_players) * 100
demo = pd.DataFrame({'Total Count': demo_total,
                     'Percentage': demo_perc})

demo


## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

#calculations
gend_count = purchase_data.groupby(['Gender']).count()['Price'].rename('Purchase Count')
gend_avg = purchase_data.groupby(['Gender']).mean()['Price'].rename('Average Purchase Price')
gend_total = purchase_data.groupby(['Gender']).sum()['Price'].rename('Total Purchase Value')

#purchase total by gender
gend_purc_total = gend_total / demo['Total Count']

#table creation
gend_df = pd.DataFrame({'Purchase Count': gend_count,
                        'Average Purchase Price':gend_avg,
                        'Total Purchase Value': gend_total,
                        'Average Total Purchase per Person': gend_purc_total})

#table cleanup
gend_df['Purchase Count'] = gend_df['Purchase Count'].map('{:,}'.format)
gend_df['Average Purchase Price'] = gend_df['Average Purchase Price'].map('${:,.2f}'.format)
gend_df['Total Purchase Value'] = gend_df['Total Purchase Value'].map('${:,.2f}'.format)
gend_df['Average Total Purchase per Person'] = gend_df['Average Total Purchase per Person'].map('${:,.2f}'.format)

gend_df

## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

#bin/label assignment
players_df['Age Ranges'] = pd.cut(players_df['Age'], age_bins, labels=group_names)

#calculations
age_demo_total = players_df['Age Ranges'].value_counts()
age_demo_perc = (age_demo_total / total_players) * 100
age_demo = pd.DataFrame({'Total Count': age_demo_total,
                         'Percentage of Players': age_demo_perc})

age_demo.sort_index()

## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

#bin/label assignment
purchase_data['Age Ranges'] = pd.cut(purchase_data['Age'], age_bins, labels=group_names)

#calculations
age_count = purchase_data.groupby(['Age Ranges']).count()['Price'].rename('Purchase Count')
age_aver = purchase_data.groupby(['Age Ranges']).mean()['Price'].rename('Average Purchase Price')
age_total = purchase_data.groupby(['Age Ranges']).sum()['Price'].rename('Total Purchase Value')

#purchase total by age
age_purc_total = age_total / age_demo['Total Count']

#table creation
age_df = pd.DataFrame({'Purchase Count': age_count,
                       'Average Purchase Price': age_aver,
                       'Total Purchase Value': age_purc_total,
                       'Avg Total Purchase per Age Group': age_purc_total})

#table cleanup
age_df['Purchase Count'] = age_df['Purchase Count'].map('{:,}'.format)
age_df['Average Purchase Price'] = age_df['Average Purchase Price'].map('${:,.2f}'.format)
age_df['Total Purchase Value'] = age_df['Total Purchase Value'].map('${:,.2f}'.format)
age_df['Avg Total Purchase per Age Group'] = age_df['Avg Total Purchase per Age Group'].map('${:,.2f}'.format)

age_df

## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



#calculations
user_count = purchase_data.groupby(['SN']).count()['Price'].rename('Purchase Count')
user_aver = purchase_data.groupby(['SN']).mean()['Price'].rename('Average Purchase Price')
user_total = purchase_data.groupby(['SN']).sum()['Price'].rename('Total Purchase Value')

#table creations
user_df = pd.DataFrame({'Purchase Count': user_count,
                        'Average Purchase Price': user_aver,
                        'Total Purchase Value': user_total})

#sort high to low
user_sort = user_df.sort_values('Total Purchase Value', ascending=False)

#table cleanup
user_sort['Average Purchase Price'] = user_sort['Average Purchase Price'].map('${:,.2f}'.format)
user_sort['Total Purchase Value'] = user_sort['Total Purchase Value'].map('${:,.2f}'.format)

user_sort.head()

## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



#calculations
item_count = purchase_data.groupby(['Item ID', 'Item Name']).count()['Price'].rename('Purchase Count')
aver_item_purc = purchase_data.groupby(['Item ID', 'Item Name']).mean()['Price']
total_item_purc = purchase_data.groupby(['Item ID', 'Item Name']).sum()['Price'].rename('Total Purchase Value')

#table creation
item_df = pd.DataFrame({'Purchase Count': item_count,
                        'Item Price': aver_item_purc,
                        'Total Purchase Value': total_item_purc})

#sort high to low by purchase count
item_sort = item_df.sort_values('Purchase Count', ascending=False)

#table cleanup
item_sort['Purchase Count'] = item_sort['Purchase Count'].map('{:,}'.format)
item_sort['Item Price'] = item_sort['Item Price'].map('${:,.2f}'.format)
item_sort['Total Purchase Value'] = item_sort['Total Purchase Value'].map('${:,.2f}'.format)

item_sort.head()

## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame



#previous table sorted high to low by profit
item_total_purc = item_df.sort_values('Total Purchase Value', ascending=False)

#table cleanup
item_total_purc['Purchase Count'] = item_total_purc['Purchase Count'].map('{:,}'.format)
item_total_purc['Item Price'] = item_total_purc['Item Price'].map('${:,.2f}'.format)
item_total_purc['Total Purchase Value'] = item_total_purc['Total Purchase Value'].map('${:,.2f}'.format)

item_total_purc.head()
