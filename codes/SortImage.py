import cv2

class SortImage:
    #이미지와 에러로 이루어진 자료형의 리스트를 받아 초기화한다
    def __init__(self, ImageErrorList):
        self.CoinList = ImageErrorList

    #[Object(이미지,이미지 주소,오차율)]로 이루어진 리스트를 받으면 오차율을 기준으로 오름차순 정렬한다
    def Sort(self):
        sotred(CoinList, key = lambda object: object.error)

    #가장 유사도가 높은 알트코인 차트를 알려준다
    def GetMostCorrect(self):
        filename = CoinList[-1].address
        image = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)
        cv2.imshow(filename, image)
        cv2.waitKey(0)

    #가장 유사도가 높은 알트코인 차트 5개를 알려준다 -> 한 창에 모두 표시하는 방법으로 수정할 예정
    def GetFiveCorrect(self):
        for i in range(0,5):
            filename = CoinList[-1-i].address
            cv2.imshow(filename, image)
        cv2.waitKey(0)



