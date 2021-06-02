from mkList import mkList
import cv2

# coin price datas path
data_path = "./datas/"
extension = ".png"

# img to match
original = cv2.imread('original.png')

# parameters = user_img, algorithm number, data_path
# defaults =             1                 ./datas/
# now only 1,2
list  = mkList(original,1)

# load files up to 3 
graph1 = cv2.imread(data_path+list[0][0]+extension)
graph2 = cv2.imread(data_path+list[1][0]+extension)
graph3 = cv2.imread(data_path+list[2][0]+extension)

# display up to 3
cv2.imshow("first "+list[0][0], graph1)
cv2.imshow("second "+list[1][0],graph2)
cv2.imshow("third "+list[2][0],graph3)
cv2.imshow("user_img",original)
cv2.waitKey()
cv2.destroyAllWindows()