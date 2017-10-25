# -*- coding: utf-8 -*-

import numpy
from pandas.core.frame import DataFrame
import json

f=open('j1.json')
a=f.read()
b=a.split('var ')
def todict(x):
          l=[]
          for i in x:
          	n1=i.find('[')
                l.append(json.loads(i[n1:-1]))
          return l
data=todict(b[1:])
def tolist(x):
          l=[]
          for i in x:
              l.append(DataFrame(i))
          return l
c=tolist(data)

ttt=DataFrame(columns=['city','pvid','shortname','fullname','address','url','lon','lat','service'])
for i in range(584):
    city=(c[1][(c[1]['id']==c[3]['ct'][i])].iloc[0])['nz']
    pvid=(c[0][(c[0]['id']==c[3]['pv'][i])].iloc[0])['nz']
    shortname=(c[3].iloc[i])['dnz']
    fullname=(c[3].iloc[i])['nz']
    address=(c[3].iloc[i])['az']
    url=(c[3].iloc[i])['ws']
    lon=(c[1][(c[1]['id']==c[3]['ct'][i])].iloc[0])['ln']
    lat=(c[1][(c[1]['id']==c[3]['ct'][i])].iloc[0])['lt'] 
    service=''
    p=(c[4][(c[4]['br']==c[3]['id'][i])])
    for x in p.index:
        service=service+' '+ (c[2][(c[2]['id']==p['tp'].loc[x])].iloc[0])['nz']
        service=service[1:]
        ttt.loc[i]=[city,pvid,shortname,fullname,address,url,lon,lat,service]

ttt.to_csv("ouput.csv",index=False,encoding='UTF-8')
       