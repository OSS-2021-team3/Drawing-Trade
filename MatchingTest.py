from ImageMatching import ImageMatching
import cv2

path = 'C:/Users/great/images/'
original = cv2.imread(path + 'original.png')
graph1 = cv2.imread(path + 'graph1.png')
graph2 = cv2.imread(path + 'graph2.png')
graph3 = cv2.imread(path + 'graph3.png')
graph4 = cv2.imread(path + 'graph4.png')
graph5 = cv2.imread(path + 'graph5.png')
graph6 = cv2.imread(path + 'graph6.png')

graphs = [graph1,graph2,graph3,graph4,graph5,graph6]

for i in range(0,6):
    print("입력값과"+str(i+1)+"번째 그래프의 유클리드 매칭 값 : " + str(ImageMatching.EuclideanDistanceMatching(original,graphs[i])))
for i in range(0,6):
    print("입력값과"+str(i+1)+"번째 그래프의 코사인 매칭 값 : " + str(ImageMatching.CosineSimilarityMatching(original,graphs[i])))
