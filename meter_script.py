#!/usr/bin/env python
# coding: utf-8

# In[3]:


import gspread
import pandas as pd
from pprint import pprint
import matplotlib
import numpy
from matplotlib.dates import date2num
import matplotlib.pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("json_data.json")

def number(data):
    if data == "" or data == "-":
        return False
  
    return data.isdigit()

def toNum(data):
    n = len(data)
    out = 0
    for i in range (n):
        
        out += int(data[i])
    return out




def complex(st):

    top = -1;
    vt = []
    ans = 0;
    i = 0
    while i < (len(st)):
        
        if i+1 < len(st) and ((st[i] == 'l'  and st[i+1] == 'o') or (st[i] == 'L' and st[i] == 'o') or (st[i] == 'L' and st[i] == 'O') ):
            if not(top == -1 or vt[top] == "*" or vt[top] == "+" or st[i] == '+' or st[i] == '*'):
                vt.append("*");
                top+=1;
            
            vt.append("logn");
            if ans == 0:
                ans = 10;
            
            else:
                if vt[top] == "*":
                    ans *=10;
                else:
                    ans += 10;
            # print("cut")
            i+=3;
            print(i)
            top+=1;
        
        elif st[i] == 'O' or st[i] == 'o' or st[i] == '(' or st[i] == ')' or st[i] == '^' or st[i] == '<' or st[i] == '>' :
            i+=1;
            continue;
        
        else:
            if not(top == -1 or vt[top] == "*" or vt[top] == "+" or st[i] == '+'or st[i] == '*'):
                vt.append("*");
                top+=1;
            
            
            
            if not(ans == 0):
                curr = 0;
                if (st[i] >= 'a' and st[i] <= 'z') or (st[i] >= 'A' and st[i] <= 'Z'):
                    curr = 100;
                
                elif st[i] >= '0' and st[i] <= '9':
                    curr = int(st[i]);
                
                if vt[top] == "*" and curr > 0:
                    if(curr < 10):
                        ans = pow(ans, curr);
                    else:
                        ans *= curr;
                    
                
                elif curr > 0:
                    if curr < 10:
                        ans += 1;
                    else:
                        ans += curr
                        
                
                
            
            else:
                if (st[i] >= 'a' and st[i] <= 'z') or (st[i] >= 'A' and st[i] <= 'Z'):
                    ans = 100;
                    
                else:
                    ans = 1;
                    
                
            ths = st[i];
                
                
            vt.append(ths);
            top+=1;
        i+=1;
            
           
        
        
    # for i in range (len(vt)):
    #     print(vt[i]);
        
    return ans;



def attempt_grph():


    client = gspread.authorize(creds)
    sheet = client.open("this")

    page = sheet.worksheet("Medium Problems")
    data = page.get_all_values()

    print(len(data))

    name_index = {}
    for i in range(len(data[0])):
        if data[0][i] != "":
    #         print(data[0][i])
         name_index[data[0][i]] = i;
    print(name_index);
    who = input("enter name")
    com1 = 0
    com_n = 0
    com_n2 = 0
    com_high = 0
    com_lg = 0
    be = 0;
    be_count = 0;
    ae = 0;
    ae_count = 0;
    lil = {}
    count = 0;
    times = []
    for i in range(5,len(data[0])):
            if number(data[i][name_index[who]+2]):
                be_count+=1;
                be += toNum(data[i][name_index[who]+2])
            if number(data[i][name_index[who]+3]):
                ae_count+=1;
                ae += toNum(data[i][name_index[who]+3])
    
            date = data[i][name_index[who]].split(" ")
    #         print(date)
            d  = date[0].split("/")
            if not(data[i][name_index[who]+4] == "" or data[i][name_index[who]+4] =="-"):
                co = complex(data[i][name_index[who]+4])
                if co >= 1000000:
                    com_high += 1               
                elif co >= 10000:
                    com_n2 += 1
                elif co >= 100:
                    com_n += 1
                elif co >= 10:
                    com_lg += 1
                else:
                    com1 += 1;
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
    pie_data = []
    pie_data.append(com_high)
    pie_data.append(com_n2)
    pie_data.append(com_n)
    pie_data.append(com_lg)
    pie_data.append(com1)

    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()

    # plt.xlim(xmin * scale_factor, xmax * scale_factor)
    lists = sorted(lil.items()) # sorted by key, return a list of tuples
    print(lil)
    x, y = zip(*lists)
    x = list(x)
    y = list(y) 
    # x =numpy.asarray(x)
    # for i in range(0,len(x)):
    #     x[i] =x[i] - x[0]

    # y = numpy.asarray(y)
    # dts = matplotlib.dates.datestr2num(x)

    print(x,y)
    print(count)

    # plt.xlabel(who, fontsize=18)
    # p = plt.plot(x,y)
    # plt.draw()


    # In[192]:


    print(data[6][name_index[who]].split(" "))
    lil = []
    lil.append(x)
    lil.append(y)
    print(lil)
    return lil,pie_data,ae,ae_count,be,be_count,count;


# 
