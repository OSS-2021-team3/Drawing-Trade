import cv2
import numpy

#이미지 HuMomentMatching, 0 ~ -∞ float 값 리턴 
#0에 가까울 수록 더 잘맞는 값
#두이미지의 윤곽선을 구하고 Humoment를 사용하는 방식
def HuMomentMatching(img1,img2):
    #이미지를 흑백에 같은 사이즈로 변환
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img1 = cv2.resize(img1, (256, 256))

    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img2 = cv2.resize(img2, (256, 256))
    
    imgList = [img1,img2]
    contours = []
    for img in imgList:
        thr = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#임계점 아래 뽑아내기
        conts,hierarchy = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#윤곽선 뽑아내기
        contours.append(conts[0])
    #휴모멘트를 이용한 매칭
    return -cv2.matchShapes(contours[0],contours[1],1,0) 