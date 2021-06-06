import crawler
import numpy as np
import cv2

# import algorithms
from ImageMatching import ImageMatching

# make [ [name,diff] , [name,diff]  ... ]
def mkList(user_img_url,case=1,data_path = "./datas/"):
    #  update price datas
    tickers = crawler.gettickers()

    # maybe add loading page
    # choose one algorithm
    if case == 1:
        compare = ImageMatching.EuclideanDistanceMatching
        print("Euclide matching start")
    elif case == 2:
        print("Cosine matching start")
        compare = ImageMatching.CosineSimilarityMatching

    values = []
    # valid data space
    x= 100;y=70;w=455;h=345

    # compare each graph with a choosen algorithm 
    for i in tickers:
        # from .png file to opencv for input file
        graph = cv2.imread(data_path+i+".png")[y:y+h,x:x+w].copy()
        user_data = cv2.imread(user_img_url)
        # make 2nd dimension array
        temp = [i]
        temp.append(compare(user_data,graph))
        values.append(temp)
    
    # sort least diffrence
    values.sort(key = lambda x:x[1])

    return values

def refreshDatas():
    return crawler.carwl(data_path = "./datas/")
