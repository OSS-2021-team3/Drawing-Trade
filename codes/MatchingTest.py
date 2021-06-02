from mkList import mkList
import cv2

# coin price datas path
data_path = "./datas/"
extension = ".png"

# img to match
original = cv2.imread('original.png')

# user_img, algorithm number, data_path
list  = mkList(original,1)

# list up to 3 
graph1 = cv2.imread(data_path+list[0][0]+extension)
graph2 = cv2.imread(data_path+list[1][0]+extension)
graph3 = cv2.imread(data_path+list[2][0]+extension)

# display up to 3
cv2.imshow("first "+list[0][0], graph1)
cv2.imshow("second "+list[1][0],graph2)
cv2.imshow("third "+list[2][0],graph3)
cv2.imshow("origin",original)
cv2.waitKey()
cv2.destroyAllWindows()