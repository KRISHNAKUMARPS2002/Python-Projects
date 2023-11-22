import cv2

source = "python-style.jpg"
destination = "newImage.png"
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)


new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

output = cv2.resize(src, (new_width, new_height))

cv2.imwrite("newImage.png", output)
# cv2.waitKey(0)