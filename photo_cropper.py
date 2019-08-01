import cv2

pt1 = []  # top left corner of selection
pt2 = [] # bottom right corner of selection

# read image
img = cv2.imread("resources/boy.jpg", 1)
img_original = img.copy()
cv2.putText(img, "Choose top left corner and drag to select a region." , (10,20), \
            fontFace=3, fontScale=0.45, color=(255,255,255), thickness=1)

# callback function
def cropSelection(action, x, y, flags, userdata):
    global pt1, pt2, cropped, img
    if action==cv2.EVENT_LBUTTONDOWN:
        pt1 = [(x,y)]
        
    elif action==cv2.EVENT_LBUTTONUP:
        pt2=[(x,y)]
        img = img_original.copy()
        cv2.rectangle(img, pt1[0], pt2[0], (0,255,0), 2, cv2.LINE_AA)
        cv2.putText(img, "Image cropped. Press Esc to exit." , (10,20), \
                    fontFace=3, fontScale=0.45, color=(255,255,255), thickness=1 );
        croppedImg = img_original[pt1[0][1]:pt2[0][1], pt1[0][0]:pt2[0][0]]
        cv2.imwrite("cropped_selection.jpg", croppedImg)
    
cv2.namedWindow("Image Cropper")
cv2.setMouseCallback("Image Cropper", cropSelection)

# main loop
while True:
    cv2.imshow("Image Cropper", img)
    c = cv2.waitKey(2)
    if c == 27:
        break 
        
cv2.destroyAllWindows()