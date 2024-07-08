import pandas as pd
import os
def search_osaka(select_info):
    print(select_info)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.join(BASE_DIR,'static\\osaka_tripadvisor.csv'))
    data = pd.read_csv(os.path.join(BASE_DIR,'static\\osaka_tripadvisor.csv'))
    print(data.head(10))