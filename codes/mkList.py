from crawler import carwl
import numpy as np
import cv2

# import algorithms
from AverageHashMatching import AverageHashMatching


# make [ [name,diff] , [name,diff]  ... ]
def mkList(user_img,case=1,data_path = "./datas/"):
    #  update price datas
    tickers = carwl(data_path)

    # maybe add loading page
    
    # choose one algorithm
    if case == 1:
        compare = AverageHashMatching
    # elif case == 2:
    #     compare = comp2

    values = []
    # valid data space
    x= 100;y=70;w=455;h=345

    # compare each graph with a choosen algorithm 
    for i in tickers:
        # from .png file to opencv for input file
        graph = cv2.imread(data_path+i+".png")[y:y+h,x:x+w].copy()

        # make 2nd dimension array
        temp = [i]
        temp.append(compare(graph, user_img))
        values.append(temp)
    
    # sort least diffrence
    values.sort(key = lambda x:x[1])

    return values