import cv2, numpy as np
import matplotlib.pylab as plt

#cv2 img1,img2값 받아서 유사도 측정한다음 float 값 받아오는 함수
def CompareImage(cv2 img1,cv2 img2):

imgs = [img1,img2]
hists = []
flag = cv2.HISTCMP_CORREL
#cv2.HISTCMP_CORREL 상관관계 (1: 완전 일치, -1: 완전 불일치, 0: 무관계)
#cv2.HISTCMP_CHISQR 카이제곱 (0: 완전 일치, 무한대: 완전 불일치)
#cv2.HISTCMP_INTERSECT 교차분석 (1: 완전 일치, 0: 완전 불일치 - 1로 정규화한 경우)
#cv2.HISTCMP_BHATTACHARYYA 

for i, img in enumerate(imgs) :
    hist = cv2.calcHist([img], [0], None, [256], [0,256])    # H채널에 대한 히스토그램 계산 , 1채널 사용하여 회색조로 읽음
    cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)    #0~1로 정규화
    hists.append(hist)

ret = cv2.compareHist(hists[0], hists[1], flag)   #각 메서드에 따라 img1과 img2의 히스토그램 비교
if flag == cv2.HISTCMP_INTERSECT:   #교차 분석인 경우 
    ret = ret/np.sum(hists[0])   #비교대상으로 나누어 1로 정규화

    return ret #return 값 float임!