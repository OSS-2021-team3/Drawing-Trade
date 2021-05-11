from typing import List
from AverageHashMatching import AverageHashMatching
import cv2

path = 'C:/Users/great/images/'
original = cv2.imread(path + 'original.png')
graph1 = cv2.imread(path + 'graph1.png')
graph2 = cv2.imread(path + 'graph2.png')
graph3 = cv2.imread(path + 'graph3.png')
graph4 = cv2.imread(path + 'graph4.png')
graph5 = cv2.imread(path + 'graph5.png')

graphs = [graph1,graph2,graph3,graph4,graph5]

for i in range(0,5):
    print('%d 번째 그래프와 원본의 유사도 : %f' %(i+1,AverageHashMatching(original,graphs[i])))
