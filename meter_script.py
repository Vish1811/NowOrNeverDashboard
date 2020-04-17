#!/usr/bin/env python
# coding: utf-8

# In[3]:


import gspread
import pandas as pd
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials


# In[4]:


scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("json_data.json")


# In[5]:


client = gspread.authorize(creds)
name = "Easy Problems"


# In[36]:


sheet = client.open("this")

page = sheet.worksheet("Hard Problems")

# print(sheet[2])


# In[37]:


import matplotlib
import numpy
from matplotlib.dates import date2num
import matplotlib.pyplot as plt

# data = sheet.get_all_records()
data = page.get_all_values()
# headers = data.pop()
# print(headers)
# df = pd.DataFrame(data, columns=headers)

print(len(data))


# In[38]:


name_index = {}
for i in range(len(data[0])):
    if data[0][i] != "":
#         print(data[0][i])
        name_index[data[0][i]] = i;
print(name_index);
who = input("enter name")


# In[39]:




lil = {}
count = 0;
times = []
for i in range(5,len(data[0])):
#     if data[i][name_index[who]] == "":
#         break
#     else:
#         print(data[i][5],data[i][6])
        date = data[i][name_index[who]].split(" ")
#         print(date)
        d  = date[0].split("/")
        
        if len(d) < 2:
            continue;
        count+=1;
        print(d)
        ths = int(d[0])+int(d[1])*31+int(d[2])*365;
        if data[i][name_index[who]+1] != "":
            print(data[i][name_index[who]+1])
            if ths in lil.keys(): 
                
                lil[ths]+=1
            else:
                lil[ths] = 1
#         else:
#             lil.append(0);
# type(times[0])  
plt.style.use("seaborn")
# dts = matplotlib.dates.datestr2num(times)
# print(dts)
# dts = matplotlib.dates.date2num(dts)
# scale_factor = 10

xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()

# plt.xlim(xmin * scale_factor, xmax * scale_factor)
lists = sorted(lil.items()) # sorted by key, return a list of tuples
print(lil)
x, y = zip(*lists)
x =numpy.asarray(x)
x =x - x[0]

y = numpy.asarray(y)
# dts = matplotlib.dates.datestr2num(x)

print(x,y)
print(count)

plt.xlabel(who, fontsize=18)
plt.plot(x,y)


# In[192]:


print(data[6][name_index[who]].split(" "))


# 
