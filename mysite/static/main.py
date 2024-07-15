import pandas as pd
import os
from static.LinkedList import LinkedList


def init_osaka():
    global list1
    list1 = LinkedList()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.join(BASE_DIR,'static\\osaka_tripadvisor.csv'))
    data = pd.read_csv(os.path.join(BASE_DIR,'static\\osaka_tripadvisor.csv'))
    #print(data.columns)

    for row in data.iterrows(): #row 단위로 자르기
        cur = []
        for d in row[1][['cuisines/0','cuisines/1', 'cuisines/2', 'cuisines/3', 'cuisines/4', 'cuisines/5','cuisines/6', 'cuisines/7']]:
            if not pd.isna(d): #isna: N/A 가 있으면, not isna: N/A가 없으면
                cur.append(d.lower())

        list1.add_node(row[1]['name'],row[1]['address'],row[1]['rankingPosition'],row[1]['numberOfReviews'],cur) 

        """
        row[0]=index
        Index(['name', 'address', 'rankingPosition',...
        """

    
def search_osaka(select_info): #검색어가 select_info의 'search'에 있음
    global list1
    print(select_info)
    return list1.find_list(select_info['search'],select_info['selectedOption'],select_info['orderOption'],select_info['Vegan option'],select_info['Vegetarian friendly'],select_info['Gluten free'])