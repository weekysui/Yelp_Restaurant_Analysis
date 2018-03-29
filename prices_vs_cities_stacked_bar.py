
# coding: utf-8

# In[4]:


from config import api_key
from yelpapi import YelpAPI
import requests
import pandas as pd
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt


# In[5]:


cities = ["Anaheim,CA", "Santa Ana,CA", "Irvine,CA", "Huntington Beach,CA", "Garden Grove,CA", "Orange,CA", "Fullerton,CA", "Costa Mesa,CA", "Mission Viejo,CA","Westminster,CA"]
url = "https://api.yelp.com/v3/businesses/search"
headers = {'Authorization': 'Bearer %s' %api_key}
price_locations = {}

for city in cities:
    locations={}
    params = {"term":"restaurant",
              "location":city,
              "limit":50,
             "radius":5000}
    responses=requests.get(url,headers = headers, params = params).json()
    for response in responses["businesses"]:
        try:
            money= response["price"]
            if money not in locations:
                locations[money]=1
                
            else:
                locations[money]+=1
        except KeyError:
            continue  
    price_locations[city]=locations 
    url_params = {"term":"restaurant",
                  "location":city,
                  "limit":50,
                 "offset":50,
                  "radius":5000}
    results = requests.get(url,headers = headers, params = url_params).json()
    for r in results["businesses"]:
        try:
            m = r["price"]
            if m not in locations:
                locations[m]=1
            else:
                locations[m]+=1
        except KeyError:
            continue
    price_locations[city]=locations
print(price_locations)        
     


# In[6]:


columns = ["Cheap","Affordable","Expensive","Luxury"]
DF=pd.DataFrame.from_dict(price_locations).T #.T means transpose, switch columns and rows
DF = DF.reset_index()
# df.rename(columns = {'index':'City','$':'Cheap'}, inplace = True)
df = DF.rename(columns={"$":"Cheap","$$":"Affordable","$$$":"Expensive","$$$$":"Luxury","index":"City"})
# DF.to_csv("output.csv")

df = df.fillna(0)
df


# In[7]:


plt.rc('ytick', labelsize=25)
plt.rc('xtick', labelsize=25) 
plt.rc('axes', titlesize=25)
plt.rc('axes', labelsize=25)

x_axis = np.arange(len(cities))
df.plot.bar(x_axis,alpha=0.7, align='edge', stacked=True, figsize=(25,10))


# In[8]:


tick_locations = [value+0.3 for value in x_axis]
plt.xticks(tick_locations, cities)

plt.title('Price Range per Cities vs. Total Restaurants')
plt.xlabel('Cities')
plt.ylabel('Total Restaurants')
plt.legend(loc = 'lower right', fontsize=20)
plt.gca().yaxis.grid(True)
#plt.rcParams['axes.facecolor'] = 'lightgrey'
plt.show()

