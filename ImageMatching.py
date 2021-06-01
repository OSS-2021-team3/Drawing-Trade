import cv2
import numpy as np
from numpy.core.records import array
from numpy import dot
from numpy.linalg import norm


class ImageMatching:
    #이미지에서 임계점 아래 이미지만 가져옴
    def GetThreshImg(img, sizeX, sizeY, thr):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (sizeX, sizeY))
        ret, gray = cv2.threshold(gray, thr, 255, 0)
        return gray

    #이미지를 데이터로 변환, x값마다 가장 높은 y값을 가져옴
    def Img2Data(img):
        size = img.shape[0]
        data = [0 for i in range(size)]
        for i in range(size):
            for j in range(size):
                if img[j, i] < 128:
                    data[i] = j
                    break
        return data

    #used for debug data set
    def Data2Img(data):
        size = len(data)
        img = np.full((size, size, 3), 0, dtype=np.uint8)
        for i in range(size):
            img[data[i]][i] = [255, 255, 255]
        return img
    
    def EuclideanDistance(data1, data2):
        diff = 0
        for i in range(len(data1)):
            diff += np.abs(data1[i] - data2[i])
        return diff

    #이미지를 변환한 후 유클리드 거리를 계산해 반환한다.
    def EuclideanDistanceMatching(img1, img2):
        data1 = ImageMatching.Img2Data(ImageMatching.GetThreshImg(img1, 256, 256, 128))
        data2 = ImageMatching.Img2Data(ImageMatching.GetThreshImg(img2, 256, 256, 128))
        return ImageMatching.EuclideanDistance(data1, data2)

    def CosineSimilarity(data1, data2):
        diff = 0
        for i in range(len(data1)-1):
            vec1 = np.array([i, data1[i], i+1, data1[i+1]])
            vec2 = np.array([i, data2[i], i+1, data2[i+1]])
            diff += dot(vec1, vec2)/(norm(vec1)*norm(vec2))
        return (1/diff)*1000

    #이미지를 변환한 후 코사인값을 계산해 반환한다.
    def CosineSimilarityMatching(img1, img2):
        data1 = ImageMatching.Img2Data(ImageMatching.GetThreshImg(img1, 256, 256, 128))
        data2 = ImageMatching.Img2Data(ImageMatching.GetThreshImg(img2, 256, 256, 128))
        return ImageMatching.CosineSimilarity(data1, data2)
