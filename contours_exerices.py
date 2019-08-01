import cv2
import numpy as np


""" CONSTANT DEFINITIONS """
imagePath = "resources\Contour.png"
image = cv2.imread(imagePath,1)  # need to load color image to show contours later
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_backup = image.copy()

LINE_THICKNESS = 2
CONTOUR_INDEX = -1  # -1 implies all
BLUE = (255,0,0)
RED = (0,0,255)
GREEN = (0,255,0)
YELLOW = (0, 255,255)
WHITE = (255,255,255)
FONT_SIZE = 1
FONT = 1
FONT_THICKNESS = 1
""" END """

contours, hierarchy = cv2.findContours(image_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)

# image = image_backup
# contours, hierarchy = cv2.findContours(image_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(image, contours, -1, (0,0,255), 3);
# cv2.imshow("Image2", image)

# image = image_backup
# contours, hierarchy = cv2.findContours(image_gray, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(image, contours, -1, (0,0,255), 3);
# cv2.imshow("Image3", image)

# image = image_backup
# contours, hierarchy = cv2.findContours(image_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(image, contours, -1, (0,0,255), 3);
# cv2.imshow("Image4", image)

# frame 1
cv2.drawContours(image, contours, CONTOUR_INDEX, GREEN, LINE_THICKNESS)
cv2.putText(image, "External Contours", (10,10), FONT, FONT_SIZE, WHITE, FONT_THICKNESS)
cv2.putText(image, "Press any key to continue", (10,700), FONT, FONT_SIZE, WHITE, FONT_THICKNESS)
cv2.imshow("image", image)
cv2.waitKey(0)

# frame 2
image = image_backup.copy()
cv2.drawContours(image, contours, CONTOUR_INDEX, GREEN, LINE_THICKNESS)
for index, c in enumerate(contours):
    # find centroids
    m = cv2.moments(c)
    x = round(m["m10"]/m["m00"])
    y = round(m["m01"]/m["m00"])

    # draw centroids
    cv2.circle(image, (x,y), 5, RED, -1) # 5 is outer radius, -1 is inner radius (filled)
    cv2.putText(image, f"Centroid {index+1}", (x+10, y), FONT, FONT_SIZE, RED, FONT_THICKNESS)
    
    # print area and arclength
    area = round(cv2.contourArea(c),2)
    arclength = round(cv2.arcLength(c, True),2)
    cv2.putText(image, f"area = {area}", (x+10, y+15), FONT, FONT_SIZE, RED, FONT_THICKNESS)
    cv2.putText(image, f"arclength = {arclength}", (x-10, y+30), FONT, FONT_SIZE, RED, FONT_THICKNESS)

cv2.putText(image, "Centroids", (10,10), FONT, FONT_SIZE, WHITE, FONT_THICKNESS)
cv2.putText(image, "Press any key to continue", (10,700), FONT, FONT_SIZE, WHITE, FONT_THICKNESS)
cv2.imshow("image", image)
cv2.waitKey(0)

# frame 3
image = image_backup.copy()
cv2.drawContours(image, contours, CONTOUR_INDEX, GREEN, LINE_THICKNESS)
for index, c in enumerate(contours):
    # draw bounding boxes
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image, (x,y), (x+w, y+h), BLUE, LINE_THICKNESS)

cv2.putText(image, "Bounding Boxes", (10,10), FONT, FONT_SIZE, WHITE, FONT_THICKNESS)
cv2.putText(image, "Press any key to continue", (10,700), FONT, FONT_SIZE, WHITE, FONT_THICKNESS)
cv2.imshow("image", image)
cv2.waitKey(0)

# frame 4
image = image_backup.copy()
cv2.drawContours(image, contours, CONTOUR_INDEX, GREEN, LINE_THICKNESS)
for index, c in enumerate(contours):
    
    # draw rotated bounding boxes
    box = cv2.minAreaRect(c)
    boxPts = np.int0(cv2.boxPoints(box))
    cv2.drawContours(image, [boxPts], -1, YELLOW, LINE_THICKNESS)

cv2.putText(image, "Rotated Bounding Boxes", (10,10), FONT, FONT_SIZE, WHITE, FONT_THICKNESS)
cv2.putText(image, "Press any key to continue", (10,700), FONT, FONT_SIZE, WHITE, FONT_THICKNESS)
cv2.imshow("image", image)
cv2.waitKey(0)

# frame 5
image = image_backup.copy()
cv2.drawContours(image, contours, CONTOUR_INDEX, GREEN, LINE_THICKNESS)
for index, c in enumerate(contours):
    
    # draw bounding circles
    ((x,y), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(image, (int(x),int(y)), int(round(radius)), BLUE, LINE_THICKNESS)

cv2.putText(image, "Bounding circles", (10,10), FONT, FONT_SIZE, WHITE, FONT_THICKNESS)
cv2.putText(image, "Press any key to continue", (10,700), FONT, FONT_SIZE, WHITE, FONT_THICKNESS)
cv2.imshow("image", image)
cv2.waitKey(0)