import cv2

maxScaleUp = 100
scaleFactor = 1
scaleType = 0
maxType = 1

windowName = "Resize Image"
trackbarValue = "Scale"
trackbarType = "Reverse"

# load an image
im = cv2.imread("resources/boy.jpg")
cv2.putText(im, "Press Esc anytime to quit", (10,20), fontFace=3, \
            fontScale=0.45, color=(255,255,255), thickness=1 );

# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

# Callback functions
def scaleImage(*args):
    global scaleFactor
    global scaleType
    multiplier = 1 if scaleType==0 else -1
    scaleFactor = 1+ multiplier * args[0]/100.0
    if scaleFactor == 0:
        scaleFactor = 1
    scaledImage = cv2.resize(im, None, fx=scaleFactor, fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)
    
# second callback function to solve discrepency with scaleType
# without this function, args can be (1,0) for 
# both scaleFactor or scaleType
def updateScaleType(*args):
    global scaleType
    if (args):
        scaleType = args[0]

cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, updateScaleType)

scaleImage(25)

while True:
    c = cv2.waitKey(20)
    if c==27:
        break

cv2.destroyAllWindows()
