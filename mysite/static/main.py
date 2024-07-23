import pandas as pd
import os
from static.LinkedList import LinkedList


def init_osaka():
    global list1 #can use list1 outside the fuction
    list1 = LinkedList()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print(os.path.join(BASE_DIR,'static\\osaka_tripadvisor.csv'))
    data = pd.read_csv(os.path.join(BASE_DIR,'static\\osaka_tripadvisor.csv'))

    for row in data.iterrows(): #separate by rows
        cur = []

        for d in row[1][['cuisines/0','cuisines/1', 'cuisines/2', 'cuisines/3', 'cuisines/4', 'cuisines/5','cuisines/6', 'cuisines/7']]:
            if not pd.isna(d): #isna: if it is N/A(blank), not isna: if it isn't N/A(blank)
                cur.append(d.lower())

        list1.add_node(row[1]['name'],row[1]['address'],row[1]['rankingPosition'],row[1]['numberOfReviews'],cur) 

        """
        row[1]=index
        Index(['name', 'address', 'rankingPosition',...
        """

    
def search_osaka(select_info): #the keyword you type in is in select_info's 'search'
    global list1
    return list1.find_list(select_info['search'],select_info['selectedOption'],select_info['orderOption'],select_info['Vegan option'],select_info['Vegetarian friendly'],select_info['Gluten free'])