#!/usr/bin/env python
# coding: utf-8

# # Implementing market basket analysis

# Association discovery is commonly called Market Basket Analysis (MBA). MBA is widely used by grocery stores, banks, and telecommunications among others. Its results are used to optimize store layouts, design product bundles, plan coupon offers, choose appropriate specials and choose attached mailing in direct marketing. The MBA helps us to understand what items are likely to be purchased together. On-line transaction processing systems often provide the data sources for association discovery

# Basic Concepts for Association Discovery
# An association rule is written A => B where A is the antecedent and B is the consequent. Both sides of an association rule can contain more than one item. Techniques used in Association discovery are borrowed from probability and statistics. Support, confidence, and Lift are three important evaluation criteria of association discovery.
# 
# A. Support
# The level of support is how frequently the combination occurs in the market basket (database). Support is the percentage of baskets (or transactions) that contain both A and B of the association, i.e. % of baskets where the rule is true
# 
# Support(A => B) = P(A ∩ B)
# 
# B. Expected confidence
# This is the probability of the consequent if it was independent of the antecedent. Expected confidence is thus the percentage of occurrences containing B
# 
# Expected confidence (A => B) = P(B)
# 
# Confidence
# The strength of an association is defined by its confidence factor, which is the percentage of cases in which a consequent appears given that the antecedent has occurred. Confidence is the percentage of baskets having A that also contain B, i.e. % of baskets containing B among those containing A. Note: Confidence(A => B) ≠ Confidence(B => A).
# 
# Confidence(A => B) = P(B | A)
# 
# C. Lift
# 
# Lift is equal to the confidence factor divided by the expected confidence. Lift is a factor by which the likelihood of consequent increases given an antecedent. Expected confidence is equal to the number of consequent transactions divided by the total number of transactions. Lift is the ratio of the likelihood of finding B in a basket known to contain A, to the likelihood of finding B in any random basket.

# In[9]:


# Installation of necessary libraries
# !pip install apyori
# pip install mlxtend


# In[6]:


#Loading neccesary packages
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


# In[8]:


#Reading Data From Web
myretaildata = pd.read_excel('http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx')
myretaildata.head()


# # Data Preparation

# In[10]:


#Data Cleaning
myretaildata['Description'] = myretaildata['Description'].str.strip() #removes spaces from beginning and end
myretaildata.dropna(axis=0, subset=['InvoiceNo'], inplace=True) #removes duplicate invoice
myretaildata['InvoiceNo'] = myretaildata['InvoiceNo'].astype('str') #converting invoice number to be string
myretaildata = myretaildata[~myretaildata['InvoiceNo'].str.contains('C')] #remove the credit transactions 
myretaildata.head()


# In[22]:


myretaildata['Country'].value_counts().head(5)
#myretaildata.shape


# In[12]:


#Separating transactions for Germany
mybasket = (myretaildata[myretaildata['Country'] =="Germany"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))


# In[13]:


#viewing transaction basket
mybasket.head()


# In[14]:


#  Encode The Data converting all positive vaues to 1 and everything else to 0--encode the basket data into a binary data that shows whether an items is bought (1) or not (0).
def my_encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

my_basket_sets = mybasket.applymap(my_encode_units)
my_basket_sets.drop('POSTAGE', inplace=True, axis=1) #Remove "postage" as an item


# # Training Model

# In[15]:


#Generatig frequent itemsets
my_frequent_itemsets = apriori(my_basket_sets, min_support=0.07, use_colnames=True)


# In[16]:


#generating rules
my_rules = association_rules(my_frequent_itemsets, metric="lift", min_threshold=1)


# In[17]:


#viewing top 100 rules
my_rules.head(100)


# The higher the lift value, the higher the association between the items willl. If the lift value is more than 1, it is enough for us to say that those two items are associated each other. 

# # Making reecommendations

# In[18]:


my_basket_sets['ROUND SNACK BOXES SET OF4 WOODLAND'].sum()


# In[19]:


my_basket_sets['SPACEBOY LUNCH BOX'].sum()


# In[21]:


#Filtering rules based on condition
my_rules[ (my_rules['lift'] >= 2) &
       (my_rules['confidence'] >= 0.3) ]


# Conclusions
# 1. Item Placements. We could put ROUND SNACK BOXES SET OF4 WOODLAND and PLASTERS IN TIN WOODLAND ANIMALS in a closer place, maybe in a same shelf or any other closer place. Similar for products ROUND SNACK BOXES SET OF4 WOODLAND and ROUND SNACK BOXES SET OF 4 FRUITS; SPACEBOY LUNCH BOX and ROUND SNACK BOXES SET OF4 WOODLAND 
# 
# 2. Products Bundling. We could put the above found items as a single bundle of product with a lower price compare to each price combined. This way will attract more sales and generates more income.
# 
# 3. Customer Recommendation and Discounts. We could put seperate discounts for this products 

# In[ ]:




