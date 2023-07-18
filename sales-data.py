#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv("fct_invoice.csv")
df


# In[3]:


json_df = pd.read_json("dim_customer.json")
json_df


# In[41]:


df["customer_id"].nunique()


# In[21]:


df["category"].unique()


# In[4]:


df["category"].nunique()


# In[42]:


df["payment_method"].unique()


# In[31]:


df["payment_method"].mode()


# In[32]:


df["payment_method"].value_counts()


# In[4]:


df['revenue'] = df['price'] * df['quantity']

df.groupby('category').sum()['revenue']


# In[10]:


merge_pd = pd.merge(json_df, df, left_on='id', right_on='customer_id', how='left')

df_new = merge_pd[merge_pd['age'] >= 45]
df_new['total_sales'] = df_new['quantity'] * df_new['price']
output = df_new[['total_sales']].sum()
print(output)


# In[59]:


import matplotlib.pyplot as plt

df['invoice_date'] = pd.to_datetime(df['invoice_date'])

grouped_dfa = df.groupby(pd.Grouper(key='invoice_date', freq='M')).apply(lambda x: (x['price'] * x['quantity']).sum())


plt.figure(figsize=(10, 6))
plt.plot(grouped_dfa.index, grouped_dfa.values, marker='o')


plt.xlabel('Invoice Date')
plt.ylabel('Total Amount Spent')
plt.title('Total Amount Spent by Customers per Invoice Date')


plt.xticks(rotation=45)


plt.show()



# Due to possibly minimal data from 2023 onwards, this could be the cause for the huge drop visualized by the graph. The years 2021-2022 have however showed almost consistent spending accross the board with peaks being found near the holiday period.
# 

# In[5]:


merged_pd = pd.merge(json_df, df, left_on='id', right_on='customer_id', how='left')
sorted_df = merged_pd.groupby(['category', pd.cut(merged_pd['age'], [10, 20, 30, 40, 50, 60, 70, 80, 90])]).sum()
sorted2_df = sorted_df[['revenue']]

pivot_table = pd.pivot_table(sorted2_df, values='revenue', index='category', columns='age', aggfunc=sum, fill_value=0)
print(pivot_table)


pd.set_option('display.max_rows', None)


# In[ ]:




