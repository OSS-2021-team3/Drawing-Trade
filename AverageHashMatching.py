import cv2
import numpy as np

# 이미지를 32x32크기의 평균 해쉬로 변환
def img2hash(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (32, 32))
    avg = gray.mean()
    bi = 1 * (gray > avg)
    return bi

# hamming distance 구하기
def hamming_distance(a, b):
    a = a.reshape(1,-1)
    b = b.reshape(1,-1)
    # 같은 자리의 값이 서로 다른 것들의 합
    distance = (a !=b).sum()
    return distance

# 이미지 HashMathcing, 0~1사이의 float값 리턴
# 1에 가까울 수록 잘맞음
# 이미지를 binary형태로 만들고 hamming distance 값 구하는거 
def AverageHashMatching(img1,img2):
    img1_hash = img2hash(img1)
    img2_hash = img2hash(img2)
    dst = hamming_distance(img1_hash,img2_hash)/1024
    return dst