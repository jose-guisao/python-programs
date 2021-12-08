import urllib2
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import matplotlib.pyplot as plt
plt.style.use('ggplot')

url = 'https://www.uefa.com'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

html_structure = soup.find_all('div', class_ = 'ranking-card')
container=html_structure[0].ul

data=[]
name = container.find_all('span', class_ = 'ranking-name')
value = container.find_all('span', class_ = 'ranking-value')
for i,j in zip(name,value):
    x=i.text
    y=j.text
    data.append([str(x),str(y)])
    
df=pd.DataFrame(data,columns=("Name","Value"))
df['Value']=pd.to_numeric(df['Value'], errors='coerce')

def club_rankling_bar_chart(value,club):
    fig, ax = plt.subplots()
    labels=np.array(club)
    colors = ['red','green','yellow','blue','cyan','gold','teal','orangered','magenta','skyblue']
    y_pos = np.arange(len(labels))
    x_pos = np.array(value)
    plt.bar(y_pos, x_pos, color=colors, align='center' ,edgecolor='green')
    plt.xticks(y_pos, labels,rotation='vertical')
    plt.xlabel('Club',fontsize=18)
    plt.ylabel('Ranking Coefficient',fontsize=18)
    ax.set_title('UEFA Clubs Ranking Coefficient\n',fontsize=20)
    plt.show()
    
value=df['Value']
club=df['Name']
club_rankling_bar_chart(value,club)